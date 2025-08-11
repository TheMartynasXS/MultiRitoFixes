curl -o hashes.game.txt https://raw.communitydragon.org/data/hashes/lol/hashes.game.txt 
@echo off
@REM read version from version.txt
set /p VERSION=<src/version.txt
echo Building MultiRitoFixes v%VERSION%
pyinstaller --noconfirm src/MultiRitoFixes.spec
echo Build completed. Output in dist/MultiRitoFixes-v%VERSION%/