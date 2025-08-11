# -*- mode: python ; coding: utf-8 -*-
import os

# Get version from environment variable if set, otherwise use a default
version = os.environ.get('VERSION', '0.0.0')
name = f'MultiRitoFixes-v{version}'

a = Analysis(
    ['MultiRitoFixes.py'],
    pathex=[],
    binaries=[],
    datas=[('../LICENSE','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
