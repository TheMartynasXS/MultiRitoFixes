from io import BytesIO
import sys
from sys import argv
from os import path, listdir, makedirs
import re
from xxhash import xxh64
from zipfile import ZIP_DEFLATED, ZipFile
from pyritofile import BIN,WAD,WADChunk, BINField, BINType, BINEntry
import tempfile
import json
from functions import stream2tex 
import subprocess
from colorama import Fore
import shutil
import psutil
import msvcrt
import subprocess
import urllib.request
import time

def get_process_exe(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return proc.exe()
    return None

def kill_process(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            proc.kill()
            log(f"Closed: {process_name}","ok")
    
def log(message = "",type = "text", indent = False):
    
    type = type.lower()
    if indent:
        message = "    " + message + Fore.RESET
    if type == "ok" or type == "success":
        print(f"{Fore.GREEN}[OK_] {message}{Fore.RESET}")
    elif type == "text":
        print(f"[INF] {message}")
    elif type == "info":
        print(f"{Fore.BLUE}[INF] {message}{Fore.RESET}")
    elif type == "error" or type == "err":
        print(f"{Fore.RED}[ERR] {message}{Fore.RESET}")
    elif type == "warning" or type == "warn":
        print(f"{Fore.YELLOW}[WRN] {message}{Fore.RESET}")

league_path = None
cslol_path = None

champions = set()
health_bars = dict()

default_hp_style = 12

def compute_hash(s: str):
    if s.startswith("0x"):
        return s[2:]
    
    h = 0x811c9dc5
    for b in s.encode('ascii').lower():
        h = (h ^ b) * 0x01000193
    return f"{h & 0xffffffff:08x}"
class CACHED_BIN_HASHES(dict):
    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        else:
            super().__setitem__(key, compute_hash(key))
            return super().__getitem__(key)
cached_bin = CACHED_BIN_HASHES()

hashes_path=None
hashes = dict()
hashes_in_bin = dict()
files_in_wad = set()

texconv_path = None

def exit_with_input(message="Done!", type="text"):
    log(message, type=type)
    print("Press any key to continue...")
    msvcrt.getch()
    sys.exit(0)
    
if len(argv) < 2:
    exit_with_input("Do not run this program directly, drag and drop file/folder on to the fixer", type="error")
    exit()
def sync_hashes(url,cache_path):
    name = path.basename(url)
    sha_cache = path.join(cache_path, name + ".sha")
    
    if path.exists(sha_cache):
        # Check if last modified is older than 1 hour ago
        last_modified = path.getmtime(sha_cache)
        if last_modified > time.time() - 3600:
            log(f"{name} was synced recently skipping","info", indent=True)
            return

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    

    sha = data.get('sha')
    url = data.get('download_url')
    
    if path.exists(sha_cache):
        with open(sha_cache, "r") as f:
            cached_sha = f.read().strip()
            if cached_sha == sha:
                log(f"{name} is up to date","ok", indent=True)
                return
            else:
                log(f"{name} is outdated","warning", indent=True)
    else:
        with open(sha_cache, "w") as f:
            f.write(sha)
    subprocess.run(["curl", "-L", "-o", path.join(cache_path, name), url])
    log(f"Downloaded {name} to {path.join(cache_path, name)}","ok", indent=True)
def setup():
    global league_path, cslol_path, champions, health_bars
    global default_hp_style, hashes_path, hashes, texconv_path
    log("Setting up MultiRitoFixes...","info")
    temp_dir = tempfile.gettempdir()
    
    fixer_cache_path = path.join(temp_dir, "multiritofixes")
    
    config_path = path.join(fixer_cache_path, "config.ini")

    if not path.exists(config_path):
        log("Fixer cache not found, creating new one...")
        
        makedirs(fixer_cache_path, exist_ok=True)
        log(f"New cache location: {fixer_cache_path}","info")
        cslol_path = get_process_exe('cslol-manager.exe')
        if cslol_path is None:
            exit_with_input("cslol-manager.exe is not running. Please start it and try again.")
        cslol_config = path.join(path.dirname(cslol_path), 'config.ini')
        if path.exists(cslol_config):
            with open(cslol_config, 'r') as f:
                for line in f:
                    if line.startswith('leaguePath='):
                        league_path = line.split('=')[1].strip()
                        break
        with open(config_path, 'w') as f:
            f.write(f"[fixer]\nleaguePath={league_path}\n")
            f.write(f"cslolPath={cslol_path}\n")
        log(f"Created fixer cache at {fixer_cache_path}",  indent=True)
    else:
        log(f"Using existing fixer cache at {fixer_cache_path}", indent=True)
        with open(config_path, 'r') as f:
            config_data = f.read()
            league_path_match = re.search(r'leaguePath\s*=\s*(.*)', config_data)
            cslol_path_match = re.search(r'cslolPath\s*=\s*(.*)', config_data)
            if league_path_match:
                league_path = league_path_match.group(1).strip()
            if cslol_path_match:
                cslol_path = cslol_path_match.group(1).strip()
    if not shutil.which("texconv.exe"):
        # curl -L -o texconv.exe https://github.com/Microsoft/DirectXTex/releases/latest/download/texconv.exe into fixer_cache_path
        if not path.exists(path.join(fixer_cache_path, "texconv.exe")):
            subprocess.run(["curl", "-L", "-o", path.join(fixer_cache_path, "texconv.exe"), "https://github.com/Microsoft/DirectXTex/releases/latest/download/texconv.exe"])
            texconv_path = path.join(fixer_cache_path, "texconv.exe")
        else:
            texconv_path = path.join(fixer_cache_path, "texconv.exe")
    else:
        texconv_path = shutil.which("texconv.exe")
        
    
    
    
    champion_wad_path = path.join(path.dirname(league_path), "game", "data", "final", "champions")
    if path.exists(champion_wad_path):
        for champion in listdir(champion_wad_path):
            pattern = re.compile(r"^[a-z]+\.wad\.client$", re.IGNORECASE)
            if pattern.match(champion):
                champions.add(champion.lower().replace('.wad.client', ''))
        log(f"Found {len(champions)} champions in {champion_wad_path}", indent=True)
    health_bars.update({
        "aniviaegg": default_hp_style,
        "annietibbers": 5,
        "azirsundisc": 3,
        "elisespider": default_hp_style,
        "gnarbig": default_hp_style,
        "ireliablades": 5,
        "ivernminion": 5,
        "kogmawdead": default_hp_style,
        "luxair": default_hp_style,
        "luxstorm": default_hp_style,
        "luxmagma": default_hp_style,
        "luxnature": default_hp_style,
        "luxice": default_hp_style,
        "luxmystic": default_hp_style,
        "luxwater": default_hp_style,
        "luxfire": default_hp_style,
        "luxdark": default_hp_style,
        "monkeykingflying": default_hp_style,
        "monkeykingclone": default_hp_style,
        "naafiripackmate": 9,
        "nidaleecougar": default_hp_style,
        "rammuspb": default_hp_style,
        "rammusdbc": default_hp_style,
        "shyvanadragon": default_hp_style,
        "swaindemonform": default_hp_style,
        "sonadjgenre03": default_hp_style,
        "sonadjgenre02": default_hp_style,
        "sonadjgenre01": default_hp_style,
        "trundlewall": 1,
        "yorickbigghoul": 5,
        "zacrebirthbloblet": 1
    })

    try:
        part1= "https://api.github.com/repos/CommunityDragon/Data/contents/hashes/lol/hashes.game.txt.0"
        part2= "https://api.github.com/repos/CommunityDragon/Data/contents/hashes/lol/hashes.game.txt.1"
        sync_hashes(part1, fixer_cache_path)
        sync_hashes(part2, fixer_cache_path)
        
        with open(path.join(fixer_cache_path, "hashes.game.txt.0"), "r", encoding="utf-8") as file:
            for line in file:
                hash = line.split(" ")[0]
                hashes[hash] = line.split(" ")[1].strip()
        with open(path.join(fixer_cache_path, "hashes.game.txt.1"), "r", encoding="utf-8") as file:
            for line in file:
                hash = line.split(" ")[0]
                hashes[hash] = line.split(" ")[1].strip()
        log(f"Loaded {len(hashes)} hashes from {fixer_cache_path}", indent=True)
    except Exception as e:
        exit_with_input(f"Error syncing/loading hashes: {e}","error")

    log("Setup complete! ", "ok", indent=False)
    
setup()

def rename(obj, champion=None):
    pattern = re.compile(r"^assets\/(characters|shared|perks|particles|maps|spells).*\.dds$", re.IGNORECASE)
    is_affected_asset = (re.match(pattern, obj) is not None)
    if is_affected_asset:
        if (xxh64(obj.lower()).hexdigest() not in files_in_wad):
            if obj.endswith(".dds") and hashes.get(xxh64(obj.replace(".dds", ".tex").lower()).hexdigest(), None) != None:
                text_line = obj.replace(".dds", "")
                log(f"Renaming: {text_line}{Fore.RED}.dds{Fore.RESET}{Fore.GREEN}.tex{Fore.RESET}", indent=True)
                obj = obj.replace(".dds", ".tex")
            else:
                log(f"Skipping: {Fore.RESET}{obj}{Fore.RED} no .tex variant", "warn", indent=True)
                pass
                
    obj = obj.replace("assets/", "ASSETS/", 1)
    return obj

def extract_hashes(obj, champion=None):
    if obj.find(" ") == -1 and obj.find(".") != -1:
        hash = xxh64(obj.lower()).hexdigest()
        if hash not in hashes_in_bin.keys():
            hashes_in_bin[hash] = obj.lower()
    return obj

def traverse_bin(obj, function=extract_hashes, champion=None):
    if isinstance(obj, str):
        return function(obj, champion)
    elif isinstance(obj, list):
        return [traverse_bin(item, function, champion) for item in obj]
    elif isinstance(obj, BINField):
        obj.data = traverse_bin(obj.data, function, champion)
        return obj
    elif isinstance(obj, tuple) and len(obj) == 2 and isinstance(obj[1], BINField):
        return (obj[0], traverse_bin(obj[1], function, champion))
    return obj



def parse_bin(bin_path, bin_file, is_standalone=False, champion=None):
    if is_standalone:
        log(f"Parsing BIN file: {bin_path}","info")
    for entry in bin_file.entries:
        if entry.type == cached_bin['SkinCharacterDataProperties']:
            for field in entry.data:
                if field.hash == cached_bin['IconSquare']:
                    char_regex = re.compile(rf"^assets\/characters\/([a-z0-9_]+)", re.IGNORECASE)
                    match = char_regex.match(field.data)
                    if match:
                        champion = match.group(1)
                        break
                        
            has_hp_bar = False
            has_hp_style = False
            UnitHealthBarStyle = BINField()
            UnitHealthBarStyle.hash = cached_bin['UnitHealthBarStyle']
            UnitHealthBarStyle.type = BINType.U8
            UnitHealthBarStyle.data = health_bars.get(champion, default_hp_style)
            
            for HealthBarData in entry.data:
                if HealthBarData.hash == cached_bin['HealthBarData']:
                    has_hp_bar = True
                    new_data = []
                    
                    for field in HealthBarData.data:
                        if field.hash == cached_bin['UnitHealthBarStyle']:
                            has_hp_style = True
                            field.data = health_bars.get(champion, default_hp_style)
                        if any(field.hash == data.hash for data in new_data):
                            continue
                        else:
                            new_data.append(field)
                    if has_hp_style:
                        HealthBarData.data = new_data
                        log(f"Set health bar for {Fore.LIGHTGREEN_EX}{champion}{Fore.RESET} with style {UnitHealthBarStyle.data}", indent=True)
                    else:
                        HealthBarData.data.append(UnitHealthBarStyle)
                        
            if has_hp_bar == False:
                HealthBarData = BINField()
                HealthBarData.hash = cached_bin['HealthBarData']
                HealthBarData.type = BINType.Embed
                HealthBarData.hash_type = cached_bin['CharacterHealthBarDataRecord']
                HealthBarData.data = [UnitHealthBarStyle]
                entry.data.append(HealthBarData)
                log(f"Set health bar to {str(champion).upper()} with style {UnitHealthBarStyle.data}", indent=True)
                

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
            for item in entry.data:
                item.data = traverse_bin(item.data, rename)             
    return bin_file

def parse_wad(wad_path: str, wad_name: str, standalone=False):
    wad_file = WAD()
    wad_file.read(wad_path)
    chunks_dict = {}

    # Extract champion name from wad_name, e.g. "WAD/TahmKench.wad.client"
    this_champion = None
    wad_basename = path.basename(wad_name).lower()
    for champ in champions:
        if champ in wad_basename and wad_basename.count(".") == 2:
            this_champion = champ
            break


    with wad_file.stream(wad_path, "rb+") as bs:
        files_in_wad.clear()
        has_bin = False
        
        # Initialize inside the stream context
        # Match any champion except this_champion
        shared_regex = re.compile(
            # rf"^ASSETS/(?!characters/{re.escape(this_champion)})(shared|perks|particles|maps|spells)?.+\.", re.IGNORECASE
            rf"^ASSETS/(characters|shared|perks|particles|maps|spells)?.+\.", re.IGNORECASE
        ) if this_champion else None
        
        # Inner function to find hash data
        def find_hash_data():
            nonlocal has_bin
            # Collect hash data from bin files
            for chunk in wad_file.chunks:
                this_string = hashes.get(chunk.hash, chunk.hash)
                if this_string is not None:
                    if not this_string.endswith(".bin"):
                        continue
                chunk.read_data(bs)
                if chunk.extension == "bin":
                    has_bin = True
                    hash_count = len(hashes_in_bin)
                    bin_file = BIN()
                    bin_file.read(path="", raw=chunk.data)
                    for entry in bin_file.entries:
                        for item in entry.data:
                            traverse_bin(item.data, extract_hashes)
                    log(f'Found {len(hashes_in_bin) - hash_count} hashes in {this_string}',indent=True)
            log(f"Files in WAD: {len(wad_file.chunks)}", "warn", indent=True)
            log(f"Files mentioned in Bin: {len(hashes_in_bin)}", "warn", indent=True)

        # Inner function to convert DDS to TEX
        def transform_files():
            count = 0
            for chunk in wad_file.chunks:
                chunk.read_data(bs)
                
                is_in_bin = (chunk.hash in hashes_in_bin.keys())
                
                this_string = hashes_in_bin.get(chunk.hash, hashes.get(chunk.hash, chunk.hash))
                # check if file is dds and if it is in bin or is not known hash
                if this_string == chunk.hash:
                    # log(f"{this_string}", indent=True)
                    files_in_wad.add(chunk.hash)
                elif chunk.extension == "dds" and is_in_bin:
                    files_in_wad.add(chunk.hash)
                    # log(f"{this_string}" ,"error", indent=True)
                    pass
                elif chunk.extension == "dds" and not is_in_bin:
                    if path.basename(this_string).startswith("2x") or path.basename(this_string).startswith("4x"):
                        files_in_wad.add(chunk.hash)
                        # Highlight both 2x and 4x prefixes in the log
                        prefix = ""
                        if path.basename(this_string).startswith("2x_"):
                            prefix = f"{Fore.RED}2x_{Fore.RESET}"
                        elif path.basename(this_string).startswith("4x_"):
                            prefix = f"{Fore.RED}4x_{Fore.RESET}"
                        log(f"Skipping: {Fore.RESET}{this_string.replace('2x_', prefix).replace('4x_', prefix)}", "warning", indent=True)
                        continue
                    if xxh64(this_string.replace(".dds",".tex").lower()).hexdigest() not in hashes.keys():
                        log(f"Skipping (doesn't have .tex variant): {this_string}", indent=True)
                        files_in_wad.add(chunk.hash)
                        continue
                    try:
                        
                        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".dds")
                        temp_file.write(chunk.data)
                        temp_file.close()
                        
                        with open(temp_file.name, "rb") as f:
                            dds_header = f.read(128)
                        
                        width = int.from_bytes(dds_header[12:16], 'little')
                        height = int.from_bytes(dds_header[16:20], 'little')
                        
                        if width % 4 != 0 or height % 4 != 0:
                            #round texture dimentions to the nearest multiple of 4
                            width = (width + 3) // 4 * 4
                            height = (height + 3) // 4 * 4
                            command = [texconv_path, "-o", path.dirname(temp_file.name), "-f", "BC3_UNORM", "-y", temp_file.name, "-w", str(width), "-h", str(height)]
                        command = [texconv_path, "-o", path.dirname(temp_file.name), "-f", "BC3_UNORM", "-y", temp_file.name]
                        subprocess.run(command, capture_output=True, text=True)
                        
                        
                        
                        if width % 4 != 0 or height % 4 != 0:
                            log(f"Skipping: {Fore.RESET}{this_string} has non-power-of-4 dimensions ({width}x{height})","warning", indent=True)
                            files_in_wad.add(chunk.hash)
                            continue
                        
                        with open(temp_file.name, "rb") as out_f:
                            out_buffer = out_f.read()
                        

                        newdata = stream2tex(out_buffer)
                        
                        newpath = this_string.replace(".dds",".tex")
                        log(f"Converting: {newpath.replace('.tex',f'{Fore.RED}.dds{Fore.RESET}{Fore.GREEN}.tex{Fore.RESET}')}", indent=True)
                        newhash = xxh64(newpath).hexdigest()
                        
                        hashes[newhash] = newpath
                        chunk.hash = newhash
                        chunk.extension = "tex"
                        chunk.data = newdata
                        files_in_wad.add(chunk.hash)
                        count += 1
                    except Exception as e:
                        log(f'Failed conversion: "{hashes.get(chunk.hash,chunk.hash)}" Unknown error: {e}',"error", indent=True)
                    
                elif chunk.extension == "tex":
                    log(f"Skipping: {Fore.RESET}{this_string}", indent=True)
                    files_in_wad.add(chunk.hash)
                else:
                    log(f"Skipping: {Fore.RESET}{this_string}{Fore.RED} is not a DDS or TEX file", indent=True)
                    files_in_wad.add(chunk.hash)
            log(f"Converted {count} DDS files to TEX", indent=True, type="info")

        # Inner function to process bin files
        def process_bin_files():
            for chunk in wad_file.chunks:
                if chunk.extension == "bnk":
                    this_string = hashes.get(chunk.hash, "no")
                    if this_string == "no":
                        log(f"Skipping: {Fore.RESET}{chunk.hash}{Fore.RED} cannot find path from hash for this bnk", "warning", indent=True)
                    elif this_string.endswith("sfx_events.bnk"):
                        new_string = this_string.replace("sfx_events.bnk", "sfx_events.old.bnk")
                        hashes[chunk.hash] = new_string
                        chunk.hash = xxh64(new_string).hexdigest()
                        log(f'Renaming:   {new_string.replace(".old.", f"{Fore.BLUE}.old.{Fore.RESET}")}', "info")
                    elif this_string.endswith("vo_events.bnk"):
                        pattern = re.compile(r"^([a-z]+)\.[a-z]{2}_[A-Z]{2}\.wad\.client$", re.IGNORECASE)
                        # in list directory of league_path find matching
                        org_wad_path = ""
                        for vo_wad in listdir(league_path):
                            if pattern.match(vo_wad):
                                if vo_wad.lower().split(".")[0] == wad_name.removeprefix("WAD/").lower().split(".")[0]:
                                    
                                    org_wad_path = path.join(league_path, vo_wad)
                        
                        if org_wad_path != "":
                            org_wad = WAD()
                            org_wad.read(org_wad_path)
                            with open(org_wad_path, "rb") as f:
                                for org_chunk in org_wad.chunks:
                                    if org_chunk.hash == chunk.hash:
                                        org_chunk.read_data(f)
                                        chunk.data = org_chunk.data
                                        log(f'Copying VO events from latest league: {this_string}', indent=True, type="ok")
                                        
                elif chunk.extension == "bin":
                    try:
                        this_string = hashes.get(chunk.hash, None)
                        if this_string:
                            log(f'Processing BIN file: {Fore.RESET}{this_string}', indent=True, type="info")
                        bin_file = BIN()
                        bin_file.read(path="", raw=chunk.data)
                        bin_file = parse_bin(chunk.hash, bin_file, is_standalone=False, champion=this_champion)
                        chunk.data = bin_file.write(path="", raw=True)
                    except Exception as e:
                        print(f'File Hash: "{chunk.hash}" THROWN AN EXCEPTION {e}')
                
                chunks_dict[chunk.hash] = chunk.data
                
        
        # Execute core functions
        find_hash_data()
        transform_files()
        process_bin_files()
        
            
    # Create the final WAD
    wad = WAD()

    #Remove specific bin/subchunktoc chunks if present
    for champ_name in champions:
        for key in (
            xxh64(f"data/characters/{champ_name}/skins/root.bin").hexdigest(),
            xxh64(f"data/characters/{champ_name}/{champ_name}.bin").hexdigest(),
            xxh64(f"data/final/champions/{champ_name}.wad.subchunktoc").hexdigest(),
        ):
            if key in chunks_dict:
                log(f"Deleting: {key} from WAD", indent=True)
            chunks_dict.pop(key, None)
            
    # for hash in files_in_wad:
    #     this_string = hashes.get(hash, "").lower()
    #     if this_string.endswith(".dds"):
    #         continue
    #     if path.basename(this_string).startswith("2x") or path.basename(this_string).startswith("4x"):
    #         chunks_dict.pop(hash, None)
            

    wad.chunks = [WADChunk.default() for _ in range(len(chunks_dict))]
    
    # Write the final WAD, with progress bar if standalone
    
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

    
def parse_fantome(fantome_path):
    log(f"Parsing Fantome file: {fantome_path}","info")
    try:
        with open(fantome_path, 'rb') as file:
            zip_file = ZipFile(file, 'r')
            zip_name_list = zip_file.namelist()

            # Check if there's at least a wad file to parse
            if (not any(x.lower().endswith('.wad.client') for x in zip_name_list)):
                # if doesnt include "META/info.json"
                log("No WADs found in this fantome.", "warning", indent=True)
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
                            log(f'Fixing "{Name}" by "{author}"', indent=True)
    except Exception as e:
        exit_with_input(f"Failed to read Fantome: {fantome_path} {str(e)}", type="error")
        

    # Reuse parse_wad by writing the WAD bytes to a temp file

    try:
        
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
    except Exception as e:
        exit_with_input(f"Failed to process WADs in Fantome: {fantome_path} {str(e)}", type="error")

    try:
        with open(fantome_path, 'wb') as file:
            log(f"Writing Fantome: {fantome_path}", type="success")
            file.write(final_zip_buffer.getvalue())
    except Exception as e:
        exit_with_input(f"Failed to write Fantome: {fantome_path} {str(e)}", type="error")

input_path = argv[1]
if path.isfile(input_path) and input_path.endswith('.bin'): # input is a bin file
    try:
        bin_file = BIN()
        bin_file.read(input_path)
        bin_file = parse_bin(input_path, bin_file, True)
        bin_file.write(input_path)
    except Exception as e:
        exit_with_input(f"Failed to parse BIN file: {input_path} {str(e)}", type="error")

elif path.isfile(input_path) and input_path.endswith('.wad.client'): # input is a wad file
    try:
        log(f"Parsing Wad: {input_path}...")
        log(path.join("WAD",path.basename(input_path)))
        wad_bytes = parse_wad(input_path, path.basename(input_path), standalone=True)
        log("Writing .wad file")
        with open(input_path, 'wb') as f:
            f.write(wad_bytes)
    except Exception as e:
        exit_with_input(f"Failed to parse WAD file: {input_path} {str(e)}", type="error")

elif path.isfile(input_path) and (input_path.endswith('.fantome') or input_path.endswith('.zip')): # input is a zip file
    try:
        parse_fantome(input_path)
    except Exception as e:
        exit_with_input(f"Failed to parse Fantome file: {input_path} {str(e)}", type="error")

elif path.isdir(input_path): # input is a directory
    from os import walk

    bin_files = []
    wad_files = []
    fantome_files = []
    is_wad_folder = False

    if path.basename(input_path) == "cslol-manager":
        exit_with_input('Don\'t run this on cslol-manager, drag and drop "installed" folder instead or a file', type="error")
    elif path.basename(input_path) == "installed":
        kill_process('cslol-manager.exe')
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
                log(str(e), type="error")
                input()
        pass
    else:
        for file_path in wad_files:
            wad_bytes = parse_wad(file_path, path.basename(file_path))
            with open(file_path, 'wb') as f:
                f.write(wad_bytes)

        for file_path in fantome_files:
            parse_fantome(file_path)
    
else:
    exit_with_input("Couldn't find any files to fix", type="warning")

if get_process_exe("cslol-manager.exe") == None:
    subprocess.Popen(cslol_path)
exit_with_input("Done!", type="success")
