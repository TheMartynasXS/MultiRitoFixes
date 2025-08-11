@echo off
set /p VERSION=<src/version.txt
echo Building MultiRitoFixes v%VERSION%
pyinstaller --noconfirm src/MultiRitoFixes.spec
echo Build completed. Output in dist/MultiRitoFixes-v%VERSION%/