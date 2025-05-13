@echo off
set /p VERSION=<version.txt
echo Building MultiRitoFixes v%VERSION%
pyinstaller --noconfirm MultiRitoFixes.spec
echo Build completed. Output in dist/MultiRitoFixes-v%VERSION%/