from io import BytesIO
import sys
from sys import argv
from os import path
import re
from xxhash import xxh64
from zipfile import ZIP_DEFLATED, ZipFile
from pyritofile import BIN,WAD,WADChunk, BINField, BINType, BINEntry
from pyritofile.structs import Vector, Matrix4
import tempfile
import json
from urllib import request
from functions import stream2tex 

from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn, TimeElapsedColumn

import time
# check if process called "cslol-manager.exe" is running
import psutil


def wait_ps(process_name, kill=False):
    #check if process is running
    running = False
    p_path = ""
    
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            running = True
            p_path = proc.exe()
            if kill:
                proc.kill()
                while proc.is_running():
                    time.sleep(1)
                print(f"{process_name} is closed")
            break
    return p_path


if len(argv) < 2:
    input('Do not run this program directly,\ndrag and drop file/folder on to the fixer')
    exit()
print(f"Running on: {argv[1]}")

input_path = argv[1]
cslol_path = ""

def compute_hash(s: str):
    if s.startswith("0x"):
        return s[2:]
    
    h = 0x811c9dc5
    for b in s.encode('ascii').lower():
        h = (h ^ b) * 0x01000193
    return f"{h & 0xffffffff:08x}"


files_in_wad = set()
class CACHED_BIN_HASHES(dict):
    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        else:
            super().__setitem__(key, compute_hash(key))
            return super().__getitem__(key)
cached_bin = CACHED_BIN_HASHES()


allowed_chars_path = None
hashes_path = None
allowed_chars = []
hashes = dict()

if getattr(sys, 'frozen', False):
    allowed_chars_path = path.join(sys._MEIPASS, 'AllowedChars.txt')
    hashes_path = path.join(sys._MEIPASS, 'hashes.game.txt')
else:
    allowed_chars_path = 'AllowedChars.txt'
    hashes_path = 'hashes.game.txt'

if path.exists(allowed_chars_path) and allowed_chars_path != None:
    with open(allowed_chars_path, 'r') as file:
        allowed_chars = [line.strip() for line in file.readlines()]
        
if path.exists(hashes_path) and hashes_path != None:
    with open(hashes_path, "r", encoding="utf-8") as file:
        for line in file:
            hash = line.split(" ")[0]
            hashes[hash] = line.split(" ")[1].strip()


def parse_bin(bin_path, bin_file, is_standalone=False):
    for entry in bin_file.entries:
        if entry.type == cached_bin['SkinCharacterDataProperties']:
            is_champion = False
            for field in entry.data:
                if field.hash == cached_bin['IconSquare']:
                    for char in allowed_chars:
                        if len(field.data.lower().split(f"/{char}/")) > 1:
                            is_champion = True
                            break
                if is_champion:
                    break
                    
            if is_champion:
                for HealthBarData in entry.data:
                    if HealthBarData.hash == cached_bin['HealthBarData']:
                        for UnitHealthBarStyle in HealthBarData.data:
                            if(UnitHealthBarStyle.hash == cached_bin['UnitHealthBarStyle']):
                                UnitHealthBarStyle.data = 12
                                break  
        if entry.type == cached_bin['StaticMaterialDef']:
            for field in entry.data:
                if field.hash == cached_bin['SamplerValues']:
                    for sampler_def in field.data:
                        tName = -1
                        tPath = -1
                        sName = -1
                        tNameIsPath = False

                        for id,value in enumerate(sampler_def.data):
                            if value.hash == cached_bin['TextureName']:
                                tName = id
                                if value.data.find("/") != -1:
                                    tNameIsPath = True
                            if value.hash == cached_bin['TexturePath']:
                                tPath = id
                            if value.hash == cached_bin['SamplerName']:
                                sName = id
                            
                        if tName != -1 and tPath != -1 and not tNameIsPath:
                            continue
                        elif tPath != -1 and sName != -1 and not tNameIsPath:
                            sampler_def.data[sName].hash = cached_bin['TextureName']
                        elif tName != -1 and sName != -1 and tNameIsPath:
                            sampler_def.data[tName].hash = cached_bin['TexturePath']
                            sampler_def.data[sName].hash = cached_bin['TextureName']
    if not(is_standalone):
        for entry in bin_file.entries:
            if entry.type == cached_bin['SpellObject'] or entry.type == cached_bin['ResourceResolver']:
                continue
            for item in entry.data:
                item.data = traverse_bin(item.data)             
    return bin_file


def rename(obj):
    obj = obj.lower()
    pattern = re.compile(r"assets/(characters/[a-r])", re.IGNORECASE)
    is_affected_asset = (re.match(pattern, obj) != None)
    if obj.endswith(".dds"):
        if is_affected_asset and (not (xxh64(obj).hexdigest()  in files_in_wad)):
            ext = re.compile(r"\.dds$", re.IGNORECASE)
            # print(f"Couldn't find {obj} in the wad renaming to .tex {xxh64(obj).hexdigest()}")
            obj = re.sub(ext, ".tex", obj)
    elif obj.endswith(".tex") and (not (xxh64(obj).hexdigest()  in files_in_wad)):
        ext = re.compile(r"\.tex$", re.IGNORECASE)
        newobj = re.sub(ext, ".dds", obj)
        if is_affected_asset and (xxh64(newobj).hexdigest() in files_in_wad):
            # print(f"Couldn't find {obj} in the wad renaming to .dds {xxh64(newobj).hexdigest()}")
            obj = newobj
    return obj

def find_missing_hashes(obj):
    obj = obj.lower()
    if xxh64(obj).hexdigest() not in hashes and obj.find(".") != -1:
        hashes[xxh64(obj).hexdigest()] = obj
    return obj
#recursively search for string type values
def traverse_bin(obj, function=rename):
    if isinstance(obj, str):
        return function(obj)

    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = traverse_bin(obj[i], function)
        return obj
    
    if isinstance(obj, BINField):
        if obj.type == BINType.String:
            obj.data = function(obj.data)
        elif obj.type == BINType.List:
            for i in range(len(obj.data)):
                if hasattr(obj.data[i], 'data'):
                    obj.data[i].data = traverse_bin(obj.data[i].data, function)
                else:
                    obj.data[i] = traverse_bin(obj.data[i], function)
        elif obj.type in (BINType.List2, BINType.Embed, BINType.Pointer):
            obj.data = traverse_bin(obj.data, function)
    return obj

def parse_wad(wad_path: str,wad_name: str,standalone=False) -> bytes:
    wad_file = WAD()
    wad_file.read(wad_path)
    chunks_dict = {}

    wad_champion = None

    with wad_file.stream(wad_path, "rb+") as bs:
        files_in_wad.clear()
        has_bin = False

        champ_name = ""
        skin_number = 0
        
        for chunk in wad_file.chunks:
            chunk.read_data(bs)
            if chunk.extension == "bin":
                bin_file = BIN()
                bin_file.read(path="", raw=chunk.data)
                for entry in bin_file.entries:
                    for item in entry.data:
                        traverse_bin(item.data, find_missing_hashes)
        
        # determine the champion name
        for char in allowed_chars:
            regex = re.compile(f"(WAD/)?{char}\.wad.client", re.IGNORECASE)
            if re.match(regex, wad_name) != None:
                print(f"Found {char} in {wad_name}")
                champ_name = char
        
        failed_conversion = False
        
        pattern = re.compile(r"^[a-r]", re.IGNORECASE)
        
        asset_pattern = re.compile(r"assets/(characters/[a-r])", re.IGNORECASE)
        #! convert dds to tex
        if(re.match(pattern, champ_name) != None) and champ_name != "":
            for chunk in wad_file.chunks:
                chunk.read_data(bs)
                if chunk.extension == "dds":
                    
                    try:
                        if hashes[chunk.hash].split("/")[-1].startswith("2x") or hashes[chunk.hash].split("/")[-1].startswith("4x"):
                            continue
                        
                        if "hud/icons2d" in hashes[chunk.hash]:
                            files_in_wad.add(chunk.hash)
                            continue
                        if re.match(asset_pattern, hashes[chunk.hash]) == None:
                            files_in_wad.add(chunk.hash)
                            continue
                        
                        newdata = stream2tex(chunk.data)
                        newpath = hashes[chunk.hash].replace(".dds",".tex")
                        newhash = xxh64(newpath).hexdigest()
                        hashes[newhash] = newpath
                        chunk.hash = newhash
                        chunk.extension = "tex"
                        chunk.data = newdata
                        files_in_wad.add(chunk.hash)
                    except Exception as e:
                        print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION {e}')
                        files_in_wad.add(chunk.hash)
                        failed_conversion = True
                elif chunk.extension == "bin":
                    # determine if the wad has a bin file
                    has_bin = True
                elif chunk.extension == "tex":
                    files_in_wad.add(chunk.hash)
        else:
            for chunk in wad_file.chunks:
                if chunk.extension == "dds":
                    files_in_wad.add(chunk.hash)
        
        #! fix bin files and remap the remaining dds files
        for chunk in wad_file.chunks:
            if chunk.extension == "bnk" and champ_name != "":
                try:
                    if hashes[chunk.hash].endswith("sfx_events.bnk"):
                        chunk.hash = hashes[chunk.hash].replace("sfx_events.bnk", f"sfx_events.old.bnk")
                except Exception as e:
                    print(f'File Hash: "{chunk.hash}" bnk could not be fixed {e}')
            elif chunk.extension == "bin":
                try:
                    bin_file = BIN()
                    bin_file.read(path="", raw=chunk.data)
                    bin_file = parse_bin(chunk.hash, bin_file)
                    chunk.data = bin_file.write(path="", raw=True)
                except Exception as e:
                    print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION {e}')
            chunks_dict[chunk.hash] = chunk.data

    wad = WAD()
    wad.chunks = [WADChunk.default() for _ in range(len(chunks_dict))]

    with wad.stream("", "rb+", raw=wad.write("", raw=True)) as bs:
        for idx, (chunk_hash, chunk_data) in enumerate(chunks_dict.items()):
            wad.chunks[idx].write_data(
                bs,
                idx,
                chunk_hash,
                chunk_data,
                previous_chunks=(wad.chunks[i] for i in range(idx))
            )
            wad.chunks[idx].free_data()

        final_bytes = bs.raw()

    return final_bytes

def parse_fantome(fantome_path: str) -> None:
    with open(fantome_path, 'rb') as file:
        zip_file = ZipFile(file, 'r')
        zip_name_list = zip_file.namelist()

        # Check if there's at least a wad file to parse
        if (not any(x.lower().endswith('.wad.client') for x in zip_name_list)):
            # if doesnt include "META/info.json"
            print("No WADs found in this fantome.")
            zip_file.close()
            return

        wads_dict, final_wads_dict, extra_files = {}, {}, {}

        for name in zip_name_list:
            if name.lower().endswith('.wad.client'):
                with zip_file.open(name, 'r') as f:
                    wads_dict[name] = f.read()
            else:
                with zip_file.open(name, 'r') as f:
                    extra_files[name] = f.read()
                    if name.endswith('META/info.json'):
                        data = json.loads(extra_files[name])
                        Name = data['Name']
                        author = data['Author']
                        print(f'Fixing "{Name}" by "{author}"')

    # Reuse parse_wad by writing the WAD bytes to a temp file
    
    for wad_name, wad_bytes in wads_dict.items():
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wad.client") as tmp_file:
            tmp_file.write(wad_bytes)
            tmp_file.flush() 
            final_wads_dict[wad_name] = parse_wad(tmp_file.name, wad_name)

    final_zip_buffer = BytesIO()
    final_zip_file = ZipFile(final_zip_buffer, 'w', ZIP_DEFLATED, False)

    for final_wad_name, final_wad_bytes in final_wads_dict.items():
        final_zip_file.writestr(final_wad_name, final_wad_bytes)
    for extra_name, extra_byte in extra_files.items():
        final_zip_file.writestr(extra_name, extra_byte)

    
    zip_file.close()
    final_zip_file.close()

    with open(fantome_path, 'wb') as file:
        print(f"Writing Fantome: {fantome_path}")
        file.write(final_zip_buffer.getvalue())
    
if path.isfile(input_path) and input_path.endswith('.bin'): # input is a bin file
    try:
        bin_file = BIN()
        bin_file.read(input_path)
        bin_file = parse_bin(input_path, bin_file, True)
        bin_file.write(input_path)
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(input_path) and input_path.endswith('.wad.client'): # input is a wad file
    try:
        print(f"Parsing Wad: {input_path}...")
        print(path.join("WAD",path.basename(input_path)))
        wad_bytes = parse_wad(input_path, path.basename(input_path),True)
        print("Writing .wad file")
        with open(input_path, 'wb') as f:
            f.write(wad_bytes)
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(input_path) and (input_path.endswith('.fantome') or input_path.endswith('.zip')): # input is a zip file
    try:
        parse_fantome(input_path)
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isdir(input_path): # input is a directory
    from os import walk
    bin_files = []
    wad_files = []
    fantome_files = []
    is_wad_folder = False
    
    #if input_path is a folder named "installed"
    if path.basename(input_path) == "installed":
        cslol_path = wait_ps("cslol-manager.exe", True)

    for root, dirs, files in walk(input_path):
        for file in files:
            temp = file.lower()
            if temp.endswith('.bin'):
                bin_files.append(path.join(root, temp))
            elif temp.endswith('.wad.client'):
                wad_files.append(path.join(root, temp))
            elif temp.endswith('.zip') or temp.endswith('.fantome'):
                fantome_files.append(path.join(root, temp))
            elif temp.endswith('.dds') or temp.endswith('.tex'):
                full_path = path.join(root, temp)
                reduced = full_path[len(input_path)+1:]
                files_in_wad.add(xxh64(reduced).hexdigest())
    
    if len(wad_files) == 0 and len(fantome_files) == 0 and len(bin_files) != 0:
        for file_path in bin_files:
            try:
                bin_file = BIN()
                bin_file.read(file_path)
                bin_file = parse_bin(file_path, bin_file, False)
                bin_file.write(file_path)
            except Exception as e:
                print(e, '\nSomething went wrong')
                input()
        pass
    else:
        count = len(wad_files) + len(fantome_files)
        print(f"Processing {len(wad_files)} wad files and {len(fantome_files)} fantome files")
        
        # Create a Rich progress bar
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            TimeRemainingColumn(),
        ) as progress:
            task = progress.add_task("[cyan]Processing files...", total=count)
            
            for file_path in wad_files:
                metadata = path.join(path.dirname(file_path), "../META/info.json")
                if path.exists(metadata):
                    with open(metadata, 'r') as f:
                        data = json.load(f)
                        print(f"Processing {data['Name']} by {data['Author']}")
                
                wad_bytes = parse_wad(file_path, path.basename(file_path))
                with open(file_path, 'wb') as f:
                    f.write(wad_bytes)
                progress.update(task, advance=1)
            
            for file_path in fantome_files:
                parse_fantome(file_path)
                progress.update(task, advance=1)
    
    if cslol_path != "":
        import subprocess
        subprocess.Popen(cslol_path)
    
else:
    print("Couldn't find any files to fix")
    input()
