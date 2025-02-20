# Source Generated with Decompyle++
# File: script.pyc (Python 3.11)

# Unsupported opcode: CHECK_EXC_MATCH (106)
from io import BytesIO
import sys
from sys import argv
from os import path
import re
# import fnv1a
from xxhash import xxh64
from zipfile import ZIP_DEFLATED, ZipFile
# from LtMAO.binfile import BIN, BINField, BINType
# from LtMAO.wadfile import WAD, WADChunk
from pyritofile import BIN,WAD,WADChunk, BINField, BINType, BINEntry
from pyritofile.structs import Vector, Matrix4

if len(argv) < 2:
    input('Plz drag and drop a folder ')
    exit()

def compute_hash(s: str):
    if s.startswith("0x"):
        return s.removeprefix("0x")
    
    h = 0x811c9dc5 
    for b in s.encode('ascii').lower(): 
        h = ((h ^ b) * 0x01000193) % 0x100000000 
    return f"{h:08x}"

filesInWad = set()


class CACHED_BIN_HASHES(dict):
    """
    Simple class that stores our hashed strings without needing to manually make the hash to get it
    """
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
inpt = argv[1]
def parse_bin(bin_path, bin_file):
    print(f"Reading: {bin_path}")
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

        if entry.type != cached_bin['ResourceResolver']:
            for item in entry.data:
                item.data = searchForStringTypeValues(item.data)             
    return bin_file

bin_assets = set()
#recursively search for string type values
def searchForStringTypeValues(obj):
    if type(obj) == list:
        for item in obj:
            item = searchForStringTypeValues(item)
        pass
    elif type(obj) == str:
        pass
        # if obj.lower().endswith(".dds"):
        #     pattern = re.compile(r"assets/(characters/[a-d])", re.IGNORECASE)
        #     check = re.match(pattern, obj) != None
        #     if check and not(xxh64(obj.lower()).hexdigest() in filesInWad):
        #         ext = re.compile(r"\.dds$", re.IGNORECASE)
        #         print(f"Couldn't find {obj} in the wad renaming to .tex")
        #         # obj = re.sub(ext, ".tex", obj)
        #     else:
        #         print(f"{check} {xxh64(obj.lower()).hexdigest()}")
        # elif obj.lower().endswith(".tex"):
        #     ext = re.compile(r"\.tex$", re.IGNORECASE)
        #     if xxh64(re.sub(ext, ".dds", obj.lower())).hexdigest() in filesInWad:
        #         pass
        #         print(f"Found {obj} in the wad renaming to .dds")
        #         # obj = re.sub(ext, ".dds", obj)
    elif type(obj) == BINField and obj.type == BINType.String:
        if obj.data.lower().endswith(".dds"):
            pattern = re.compile(r"assets/(characters/[a-d])", re.IGNORECASE)
            check = (re.match(pattern, obj.data) != None)
            if check and (not (xxh64(obj.data.lower()).hexdigest()  in filesInWad)):
                ext = re.compile(r"\.dds$", re.IGNORECASE)
                print(f"Couldn't find {obj.data} in the wad renaming to .tex {xxh64(obj.data.lower()).hexdigest()}")

                obj.data = re.sub(ext, ".tex", obj.data)
        elif obj.data.lower().endswith(".tex"):
            ext = re.compile(r"\.tex$", re.IGNORECASE)
            if (xxh64(obj.data.lower()).hexdigest() in filesInWad):
                # pass
                new = xxh64(re.sub(ext, ".dds", obj.data.lower())).hexdigest()
                print(f"Found {obj.data} in the wad renaming to .dds {new} ")
                # obj.data = re.sub(ext, ".dds", obj.data)
    elif type(obj) == BINField and obj.type == BINType.List:
        for listitem in obj.data:
            if hasattr(listitem, 'data'):
                listitem.data = searchForStringTypeValues(listitem.data)
            else:
                listitem = searchForStringTypeValues(listitem)
    elif type(obj) == BINField and obj.type == BINType.List2:
        obj.data = searchForStringTypeValues(obj.data)
        pass
    elif type(obj) == BINField and obj.type == BINType.Embed:
        obj.data = searchForStringTypeValues(obj.data)
        pass
    elif type(obj) == BINField and obj.type == BINType.Pointer:
        obj.data = searchForStringTypeValues(obj.data)
        pass
    else:
        pass
        # if(hasattr(obj, 'type')):
        #     print(obj.type)
    return obj




def parse_wad(wad_path: str) -> bytes:
    wad_file = WAD()
    wad_file.read(wad_path)
    chunk_datas = []
    chunk_hashes = []
    with wad_file.stream(wad_path, 'rb+') as bs:
        for chunk in wad_file.chunks:
            chunk.read_data(bs)
            if chunk.extension == 'bin':
                try:
                    bin_file = BIN()
                    bin_file.read(path='', raw=chunk.data)
                    bin_file = parse_bin(chunk.hash, bin_file)
                    chunk.data = bin_file.write(path='', raw=True)
                except Exception:
                    print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION')
            
            chunk_datas.append(chunk.data)
            chunk_hashes.append(chunk.hash)

    wad = WAD()
    wad.chunks = [WADChunk.default() for _ in range(len(chunk_hashes))]
    
    with wad.stream('', 'rb+', raw=wad.write('', raw=True)) as bs:
        for id, chunk in enumerate(wad.chunks):
            chunk.write_data(bs, id, chunk_hashes[id], chunk_datas[id], previous_chunks=(
                                wad.chunks[i] for i in range(id)))
            chunk.free_data()
        final_bytes = bs.raw()

    return final_bytes

def parse_fantome(fantome_path: str) -> None:
    with open(fantome_path, 'rb') as file:
        
        zip_file = ZipFile(file, 'r')
        zip_name_list = zip_file.namelist()

        has_bin_files_flag = False
        bins_dict, final_bins_dict = {}, {}
        for info in zip_file.infolist():
            if not info.is_dir():
                if info.filename.lower().endswith('.bin'):
                    bins_dict[info.filename] = zip_file.read(info)
                    has_bin_files_flag = True

        if not has_bin_files_flag:
            # checking for .wad.client files if doesnt havae bin files inside
            if not any(x.lower().endswith('info.json') for x in zip_name_list) or \
            not any(x.lower().endswith('.wad.client') for x in zip_name_list):
                print("The Zip File does not contains info.json or .wad.client files (it isn't a fantome)")
                return
        
        wads_dict, final_wads_dict, extra_infos = {}, {}, {}  # "Path/To/Wad.wad" = WadBytes
        
        for name in zip_name_list:
            if name.lower().endswith('.wad.client'):
                with zip_file.open(name, 'r') as f:
                    wads_dict[name] = f.read()
            else:
                if name.lower().endswith('.bin'):
                    continue
                with zip_file.open(name, 'r') as f:
                    extra_infos[name] = f.read()
    
    for bin_path, bin_byte in bins_dict.items():
        try:
            bin_file = BIN()
            bin_file.read(path='', raw=bin_byte)
            bin_file = parse_bin(bin_path, bin_file)
            final_bins_dict[bin_path] = bin_file.write(path='', raw=True)
        except Exception:
            print(f"Bin File: {bin_path} THROWN AN EXCEPTION")

    for wad_name, wad_byte in wads_dict.items():
        filesInWad.clear()
        wad = WAD()
        wad.read(path='blank-path', raw=wad_byte)
        chunk_datas = []
        chunk_hashes = []
        with wad.stream(path='', mode='', raw=wad_byte) as bs:
            for chunk in wad.chunks:
                chunk.read_data(bs)
                # print(f"chunk ext: {chunk.hash}")
                if chunk.extension == 'dds' or chunk.extension == 'tex':
                    filesInWad.add(chunk.hash)
            for chunk in wad.chunks:
                chunk.read_data(bs)
                # print(f"chunk ext: {chunk.hash}")
                if chunk.extension == 'bin':
                    try:
                        bin_file = BIN()
                        bin_file.read(path='', raw=chunk.data)
                        bin_file = parse_bin(chunk.hash, bin_file)
                        chunk.data = bin_file.write(path='', raw=True)
                    except Exception:
                        print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION')
                chunk_datas.append(chunk.data)
                chunk_hashes.append(chunk.hash)

        print(f"files: {len(filesInWad)}")
        wad = WAD()
        wad.chunks = [WADChunk.default() for _ in range(len(chunk_hashes))]
        
        with wad.stream('', 'rb+', raw=wad.write('', raw=True)) as bs:
            for id, chunk in enumerate(wad.chunks):
                chunk.write_data(bs, id, chunk_hashes[id], chunk_datas[id], previous_chunks=(
                                    wad.chunks[i] for i in range(id)))
                chunk.free_data()
                    
            final_wads_dict[wad_name] = bs.raw()

    final_zip_buffer = BytesIO()
    final_zip_file = ZipFile(final_zip_buffer, 'w', ZIP_DEFLATED, False)

    for final_wad_name, final_wad_bytes in final_wads_dict.items():
        final_zip_file.writestr(final_wad_name, final_wad_bytes)
    for extra_name, extra_byte in extra_infos.items():
        final_zip_file.writestr(extra_name, extra_byte)
    for final_bin_name, final_bin_byte in final_bins_dict.items():
        final_zip_file.writestr(final_bin_name, final_bin_byte)

    zip_file.close()
    final_zip_file.close()

    with open(fantome_path, 'wb') as file:
        print(f"Writing Fantome: {fantome_path}")
        file.write(final_zip_buffer.getvalue())
        
if path.isfile(inpt) and inpt.endswith('.bin'):
    # User are using a .bin file
    try:
        bin_file = BIN()
        bin_file.read(inpt)
        bin_file = parse_bin(inpt, bin_file)
        print("Writing .bin file :D")
        bin_file.write(inpt)
        print("End of Script.")
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(inpt) and inpt.endswith('.wad.client'):
    # User are using a .wad file
    try:
        print(f"Parsing Wad: {inpt}...")
        wad_bytes = parse_wad(inpt)
        print("Writing .wad file :D")
        with open(inpt, 'wb') as f:
            f.write(wad_bytes)
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isfile(inpt) and (inpt.endswith('.zip') or inpt.endswith('.fantome')):
    # User are using a fantome
    try:
        print(f"Parsing Fantome: {inpt}")
        parse_fantome(inpt)
        print("End of Script.")
    except Exception as e:
        print(e, '\nSomething went wrong')
        input()

elif path.isdir(inpt):
    # User are using a dir
    from os import walk
    found_bins = []
    found_wads = []
    found_fantomes = []
    print("Searching for Wads and Bins and Fantomes/Zips inside the desired folder.")
    
    for root, dirs, files in walk(inpt):
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
    