from io import BytesIO

import sys
from sys import argv
from os import path, listdir

import re
from xxhash import xxh64
from zipfile import ZIP_DEFLATED, ZipFile
from pyritofile import BIN,WAD,WADChunk, BINField, BINType, BINEntry
import tempfile
import json
from functions import stream2tex 
import subprocess

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

league_path = wait_ps("LeagueClient.exe", False)

if league_path == "":
    print("Run League of Legends before running this fixer.")
    input("Press Enter to exit...")
    exit()
else:
    league_path = path.join(path.dirname(league_path), "game", "data", "final", "champions")
    
champions = dict()

default_health_bar_style = 12
for champion in listdir(league_path):
    pattern = re.compile(r"^[a-z]+\.wad\.client$", re.IGNORECASE)
    if pattern.match(champion):
        champions[champion.lower().split('.')[0]] = default_health_bar_style

# Manually extend champions with special cases
champions.update({
    "aniviaegg": default_health_bar_style,
    "annietibbers": 5,
    "azirsundisc": 3,
    "elisespider": default_health_bar_style,
    "gnarbig": default_health_bar_style,
    "ireliablades": 5,
    "ivernminion": 5,
    "kogmawdead": default_health_bar_style,
    "luxair": default_health_bar_style,
    "luxstorm": default_health_bar_style,
    "luxmagma": default_health_bar_style,
    "luxnature": default_health_bar_style,
    "luxice": default_health_bar_style,
    "luxmystic": default_health_bar_style,
    "luxwater": default_health_bar_style,
    "luxfire": default_health_bar_style,
    "luxdark": default_health_bar_style,
    "monkeykingflying": default_health_bar_style,
    "monkeykingclone": default_health_bar_style,
    "naafiripackmate": 9,
    "nidaleecougar": default_health_bar_style,
    "rammuspb": default_health_bar_style,
    "rammusdbc": default_health_bar_style,
    "shyvanadragon": default_health_bar_style,
    "swaindemonform": default_health_bar_style,
    "sonadjgenre03": default_health_bar_style,
    "sonadjgenre02": default_health_bar_style,
    "sonadjgenre01": default_health_bar_style,
    "trundlewall": 1,
    "yorickbigghoul": 5,
    "zacrebirthbloblet": 1
})


if len(argv) < 2:
    print('Do not run this program directly,\ndrag and drop file/folder on to the fixer')
    print("https://github.com/Microsoft/DirectXTex/releases/latest/download/texconv.exe")
    input("Press Enter to exit...")
    exit()
print(f"Running on: {argv[1]}")
    
print(path.join(path.basename(argv[0]), "texconv.exe"))
if not path.exists(path.join(path.dirname(argv[0]), "texconv.exe")):
    print("texconv.exe not found in the current directory. Download and place it in the same folder as this program.")
    input("Press Enter to exit...")
    exit()


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

hashes_path = None
hashes = dict()

if getattr(sys, 'frozen', False):
    hashes_path = path.join(sys._MEIPASS, 'hashes.game.txt')
else:
    hashes_path = 'hashes.game.txt'

        
if path.exists(hashes_path) and hashes_path != None:
    with open(hashes_path, "r", encoding="utf-8") as file:
        for line in file:
            hash = line.split(" ")[0]
            hashes[hash] = line.split(" ")[1].strip()

def parse_bin(bin_path, bin_file, is_standalone=False):
    champion = None
    for entry in bin_file.entries:
        if entry.type == cached_bin['SkinCharacterDataProperties']:
            is_champion = False
            for field in entry.data:
                if field.hash == cached_bin['IconSquare']:
                    for char in champions.keys():
                        if len(field.data.lower().split(f"/{char}/")) > 1:
                            is_champion = True
                            champion = char
                            break
                if is_champion:
                    break
                    
            if is_champion:
                has_hp_bar = False
                has_hp_style = False
                UnitHealthBarStyle = BINField()
                UnitHealthBarStyle.hash = cached_bin['UnitHealthBarStyle']
                UnitHealthBarStyle.type = BINType.U8
                UnitHealthBarStyle.data = champions.get(champion, default_health_bar_style)
                
                for HealthBarData in entry.data:
                    if HealthBarData.hash == cached_bin['HealthBarData']:
                        has_hp_bar = True
                        new_data = []
                        
                        for field in HealthBarData.data:
                            if field.hash == cached_bin['UnitHealthBarStyle']:
                                has_hp_style = True
                                field.data = champions.get(champion, default_health_bar_style)
                            if any(field.hash == data.hash for data in new_data):
                                continue
                            else:
                                new_data.append(field)
                        if has_hp_style:
                            HealthBarData.data = new_data
                        else:
                            HealthBarData.data.append(UnitHealthBarStyle)
                            
                if has_hp_bar == False:
                    HealthBarData = BINField()
                    HealthBarData.hash = cached_bin['HealthBarData']
                    HealthBarData.type = BINType.Embed
                    HealthBarData.hash_type = cached_bin['CharacterHealthBarDataRecord']
                    HealthBarData.data = [UnitHealthBarStyle]
                    entry.data.append(HealthBarData)
                            
                            
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
    pattern = re.compile(r"assets/(characters/)", re.IGNORECASE)
    is_affected_asset = (re.match(pattern, obj) is not None)
    if obj.endswith(".dds"):
        if is_affected_asset and (xxh64(obj).hexdigest() not in files_in_wad):
            ext = re.compile(r"\.dds$", re.IGNORECASE)
            obj = re.sub(ext, ".tex", obj)
        elif is_affected_asset and (xxh64(obj.replace(r".dds$", ".tex")).hexdigest() in files_in_wad):
            pass
    elif obj.endswith(".tex") and (xxh64(obj).hexdigest() not in files_in_wad):
        ext = re.compile(r"\.tex$", re.IGNORECASE)
        newobj = re.sub(ext, ".dds", obj)
        if is_affected_asset and (xxh64(newobj).hexdigest() in files_in_wad):
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

def parse_wad(wad_path: str, wad_name: str, standalone=False) -> bytes:
    wad_file = WAD()
    wad_file.read(wad_path)
    chunks_dict = {}


    with wad_file.stream(wad_path, "rb+") as bs:
        files_in_wad.clear()
        has_bin = False
        
        # Initialize inside the stream context
        asset_pattern = re.compile(r"assets/(characters/)", re.IGNORECASE)
        failed_conversion = False
        
        # Inner function to find hash data
        def find_hash_data():
            # Collect hash data from bin files
            for chunk in wad_file.chunks:
                this_string = hashes.get(chunk.hash, None)
                if this_string is not None:
                    if this_string.endswith(".bin"):
                        continue
                chunk.read_data(bs)
                if chunk.extension == "bin":
                    hash_count = len(hashes.keys())
                    bin_file = BIN()
                    bin_file.read(path="", raw=chunk.data)
                    for entry in bin_file.entries:
                        for item in entry.data:
                            traverse_bin(item.data, find_missing_hashes)
                    print(f'Found {len(hashes.keys()) - hash_count} new hashes in {chunk.hash}')
                    
        
        # Inner function to convert DDS to TEX
        def convert_dds_to_tex():
            nonlocal failed_conversion, has_bin
            
            for chunk in wad_file.chunks:
                chunk.read_data(bs)
                if chunk.extension == "dds":
                    try:
                        this_string = hashes.get(chunk.hash, None)
                        if this_string is None:
                            print(f'(this is not bad) File Hash: "{chunk.hash}" not found in hashes, skipping conversion')
                            failed_conversion = True
                            continue
                        if this_string.split("/")[-1].startswith("2x") or this_string.split("/")[-1].startswith("4x"):
                            continue
                        if "hud/icons2d" in this_string:
                            files_in_wad.add(chunk.hash)
                            continue
                        if re.match(asset_pattern, this_string) is None and "/hud/" not in this_string:
                            files_in_wad.add(chunk.hash)
                            continue
                        print(f'Converting {this_string} to TEX format')
                        # write temp file
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".dds")
                        temp_file.write(chunk.data)
                        temp_file.close()

                        command = [f"texconv.exe", "-o", path.dirname(temp_file.name), "-f", "BC3_UNORM", "-y", temp_file.name]
                        subprocess.run(command, capture_output=True, text=True)

                        # Find the output file (texconv outputs to same dir with _BC3_UNORM.dds suffix)
                        with open(temp_file.name, "rb") as out_f:
                            out_buffer = out_f.read()

                        newdata = stream2tex(out_buffer)
                        newpath = this_string.replace(".dds",".tex")
                        # print(f"{this_string} -> {newpath}")
                        newhash = xxh64(newpath).hexdigest()
                        hashes[newhash] = newpath
                        chunk.hash = newhash
                        chunk.extension = "tex"
                        chunk.data = newdata
                        files_in_wad.add(chunk.hash)
                            
                    except Exception as e:
                        print(f'File Hash: "{chunk.hash}" Unknown error: {e}')
                        files_in_wad.add(chunk.hash)
                        failed_conversion = True
                elif chunk.extension == "bin":
                    # determine if the wad has a bin file
                    has_bin = True
                elif chunk.extension == "tex":
                    files_in_wad.add(chunk.hash)
        
        # Inner function to process bin files
        def process_bin_files():
            for chunk in wad_file.chunks:

                if chunk.extension == "bnk":
                    this_string = hashes.get(chunk.hash, "no")
                    if this_string == "no":
                        continue
                    if this_string.endswith("sfx_events.bnk"):
                        new_string = this_string.replace("sfx_events.bnk", "sfx_events.old.bnk")
                        hashes[chunk.hash] = new_string
                        chunk.hash = new_string
                        print(f'Renaming {this_string} to {new_string}')
                        
                elif chunk.extension == "bin":
                    try:
                        
                        for champ_name in champions.keys():
                            if chunk.hash == xxh64(f"data/characters/{champ_name}/skins/root.bin").hexdigest() \
                                or chunk.hash == xxh64(f"data/characters/{champ_name}/{champ_name}.bin").hexdigest():
                                continue
                        this_string = hashes.get(chunk.hash, None)
                        if this_string:
                            print(f'Processing BIN file: {this_string}')
                        bin_file = BIN()
                        bin_file.read(path="", raw=chunk.data)
                        bin_file = parse_bin(chunk.hash, bin_file)
                        chunk.data = bin_file.write(path="", raw=True)
                    except Exception as e:
                        print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION {e}')
                chunks_dict[chunk.hash] = chunk.data
        
        # Execute core functions
        find_hash_data()
        
        # Now wrap conversion process in progress bar if in standalone mode
        if standalone:
            chunks_to_process = [c for c in wad_file.chunks if c.extension in ["dds", "bin", "tex"]]
            total_chunks = len(chunks_to_process)
            
            with Progress(
                TextColumn("[bold blue]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
            ) as progress:
                task = progress.add_task(f"[cyan]Processing {path.basename(wad_name)}...", total=total_chunks + 1)
                
                convert_dds_to_tex()
                progress.update(task, advance=total_chunks+1)
                
                bin_task = progress.add_task("[cyan]Processing BIN files...", total=1)
                process_bin_files()
                progress.update(bin_task, advance=1)
        else:
            convert_dds_to_tex()
            process_bin_files()
            
    # Create the final WAD
    wad = WAD()

    # Remove specific bin/subchunktoc chunks if present
    for champ_name in champions.keys():
        for key in (
            xxh64(f"data/characters/{champ_name}/skins/root.bin").hexdigest(),
            xxh64(f"data/characters/{champ_name}/{champ_name}.bin").hexdigest(),
            xxh64(f"data/final/champions/{champ_name}.wad.subchunktoc").hexdigest(),
            
        ):
            chunks_dict.pop(key, None)


    wad.chunks = [WADChunk.default() for _ in range(len(chunks_dict))]
    
    

    # Write the final WAD, with progress bar if standalone
    if standalone:
        with Progress(
            TextColumn("[bold blue]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            write_task = progress.add_task("[purple]Writing WAD file...", total=len(chunks_dict))
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
                    progress.update(write_task, advance=1)
                
                final_bytes = bs.raw()
    else:
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
            final_wads_dict[wad_name] = parse_wad(tmp_file.name, wad_name,True)

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
        wad_bytes = parse_wad(input_path, path.basename(input_path), standalone=True)
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