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

if len(argv) < 2:
    input('Do not run this program directly,\ndrag and drop file/folder on to the fixer')
    exit()
else :
    print(f"Running on: {argv[1]}")


def compute_hash(s: str):
    if s.startswith("0x"):
        return s[2:]
    
    h = 0x811c9dc5
    for b in s.encode('ascii').lower():
        h = (h ^ b) * 0x01000193
    return f"{h & 0xffffffff:08x}"

filesInWad = set()
class CACHED_BIN_HASHES(dict):
    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        else:
            super().__setitem__(key, compute_hash(key))
            return super().__getitem__(key)

# read from included txt file in pyinstaller with --add-data 'BannedPaths.txt;.'
allowed_chars = []
if getattr(sys, 'frozen', False):
    allowed_chars = path.join(sys._MEIPASS, 'AllowedChars.txt')
else:
    allowed_chars = 'AllowedChars.txt'

if path.exists(allowed_chars):
    with open(allowed_chars, 'r') as file:
        allowed_chars = [line.strip() for line in file.readlines()]
cached_bin = CACHED_BIN_HASHES()
input_path = argv[1]
def parse_bin(bin_path, bin_file, is_standalone=False):
    for entry in bin_file.entries:
        if entry.type == cached_bin['SkinCharacterDataProperties']:
            is_champion = False
            for field in entry.data:
                if field.hash == cached_bin['IconSquare']:
                    for char in allowed_chars:
                        if len(field.data.lower().split(char)) > 1:
                            is_champion = True
                            break
                if is_champion:
                    break
                    
            if is_champion:
                for HealthBarData in entry.data:
                    if(HealthBarData.hash == cached_bin['HealthBarData']):
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
    for entry in bin_file.entries:
        if entry.type != cached_bin['ResourceResolver'] and (not(is_standalone)):
            for item in entry.data:
                item.data = traverse_bin(item.data)             
    return bin_file

bin_assets = set()
def dds_to_tex(obj):
    if obj.lower().endswith(".dds"):
        pattern = re.compile(r"assets/(characters/[a-j])", re.IGNORECASE)
        check = (re.match(pattern, obj) != None)
        if check and (not (xxh64(obj.lower()).hexdigest()  in filesInWad)):
            ext = re.compile(r"\.dds$", re.IGNORECASE)
            print(f"Couldn't find {obj} in the wad renaming to .tex {xxh64(obj.lower()).hexdigest()}")
            obj = re.sub(ext, ".tex", obj)
    return obj

#recursively search for string type values
def traverse_bin(obj):
    if isinstance(obj, str):
        return dds_to_tex(obj)

    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = traverse_bin(obj[i])
        return obj
    
    if isinstance(obj, BINField):
        if obj.type == BINType.String:
            obj.data = dds_to_tex(obj.data)
        elif obj.type == BINType.List:
            for i in range(len(obj.data)):
                if hasattr(obj.data[i], 'data'):
                    obj.data[i].data = traverse_bin(obj.data[i].data)
                else:
                    obj.data[i] = traverse_bin(obj.data[i])
        elif obj.type in (BINType.List2, BINType.Embed, BINType.Pointer):
            obj.data = traverse_bin(obj.data)

    return obj




def parse_wad(wad_path: str) -> bytes:
    wad_file = WAD()
    wad_file.read(wad_path)
    chunks_dict = {}

    with wad_file.stream(wad_path, "rb+") as bs:
        filesInWad.clear()
        for chunk in wad_file.chunks:
            chunk.read_data(bs)
            if chunk.extension in ["dds", "tex"]:
                filesInWad.add(chunk.hash)

        for chunk in wad_file.chunks:
            chunk.read_data(bs)
            if chunk.extension == "bin":
                try:
                    bin_file = BIN()
                    bin_file.read(path="", raw=chunk.data)
                    bin_file = parse_bin(chunk.hash, bin_file)
                    chunk.data = bin_file.write(path="", raw=True)
                except Exception:
                    print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION')

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
            final_wads_dict[wad_name] = parse_wad(tmp_file.name)

    final_zip_buffer = BytesIO()
    final_zip_file = ZipFile(final_zip_buffer, 'w', ZIP_DEFLATED, False)

    for final_wad_name, final_wad_bytes in final_wads_dict.items():
        final_zip_file.writestr(final_wad_name, final_wad_bytes)
    for extra_name, extra_byte in extra_files.items():
        final_zip_file.writestr(extra_name, extra_byte)
        \

    
    zip_file.close()
    final_zip_file.close()

    with open(fantome_path, 'wb') as file:
        print(f"Writing Fantome: {fantome_path}")
        file.write(final_zip_buffer.getvalue())
 
if path.isfile(input_path) and input_path.endswith('.bin'):
    # User are using a .bin file
    try:
        bin_file = BIN()
        bin_file.read(input_path)
        bin_file = parse_bin(input_path, bin_file)
        print("Writing .bin file :D")
        bin_file.write(input_path)
        print("End of Script.")
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(input_path) and input_path.endswith('.wad.client'):
    # User are using a .wad file
    try:
        print(f"Parsing Wad: {input_path}...")
        wad_bytes = parse_wad(input_path)
        print("Writing .wad file :D")
        with open(input_path, 'wb') as f:
            f.write(wad_bytes)
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(input_path) and (input_path.endswith('.zip') or input_path.endswith('.fantome')):
    # User are using a fantome
    try:
        print(f"Parsing Fantome: {input_path}")
        parse_fantome(input_path)
        print("End of Script.")
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isdir(input_path):
    # User are using a dir
    from os import walk
    found_bins = []
    found_wads = []
    found_fantomes = []
    print("Searching for Wads and Bins and Fantomes/Zips inside the desired folder.")
    
    for root, dirs, files in walk(input_path):
        for file in files:
            if file.lower().endswith('.bin'):
                found_bins.append(path.join(root, file))
            elif file.lower().endswith('.wad.client'):
                found_wads.append(path.join(root, file))
            elif file.lower().endswith('.fantome') or file.lower().endswith('.zip'):
                found_fantomes.append(path.join(root, file))
    print(f'"Bins": {found_bins}\n"Wads": {found_wads}\n"Fantomes": {found_fantomes}\n')
    
    for bin_path in found_bins:
        try:
            print(f"Parsing Bin: {bin_path}...")
            bin_file = BIN()
            bin_file.read(bin_path)
            parse_bin(bin_file)
            print("Writing .bin file :D")
            bin_file.write(bin_path)
        except Exception:
            print(f"{bin_path} THROWN AN EXCEPTION")
    
    for wad_path in found_wads:
        try:
            print(f"Parsing Wad: {wad_path}...")
            wad_bytes = parse_wad(wad_path)
            print("Writing .wad file :D")
            with open(wad_path, 'wb') as f:
                f.write(wad_bytes)
        except Exception:
            print(f"{wad_path} THROWN AN EXCEPTION")

    for fantome_path in found_fantomes:
        try:
            print(f"Parsing Fantome: {fantome_path}")
            parse_fantome(fantome_path)
        except Exception:
            print(f"{fantome_path} THROWN AN EXCEPTION")

    print("End of Script.")

else:
    print("Couldn't guess the desired object to fix")
    input()
