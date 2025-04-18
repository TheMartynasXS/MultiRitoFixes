def stream2tex(chunk_data):
    import struct
    import math
    from pyritofile.tex import TEXFormat
    
    # Parse DDS header manually
    if len(chunk_data) < 128:  # Basic check for minimal DDS header size
        raise Exception('Ritoddstex: Failed: stream2tex: Input data too small for a DDS file')
    
    # Unpack header values
    signature = struct.unpack('<I', chunk_data[0:4])[0]
    if signature != 0x20534444:  # "DDS " in little endian
        raise Exception(f'Ritoddstex: Failed: stream2tex: Wrong signature DDS file: {signature}')
    
    # Extract individual header fields to avoid struct size mismatch
    dwSize = struct.unpack('<I', chunk_data[4:8])[0]
    dwFlags = struct.unpack('<I', chunk_data[8:12])[0]
    dwHeight = struct.unpack('<I', chunk_data[12:16])[0]
    dwWidth = struct.unpack('<I', chunk_data[16:20])[0]
    dwPitchOrLinearSize = struct.unpack('<I', chunk_data[20:24])[0]
    dwDepth = struct.unpack('<I', chunk_data[24:28])[0]
    dwMipMapCount = struct.unpack('<I', chunk_data[28:32])[0]
    
    # Skip dwReserved1 (11 DWORDs = 44 bytes)
    
    # Pixel format starts at offset 76
    pixelformat_dwSize = struct.unpack('<I', chunk_data[76:80])[0]
    pixelformat_dwFlags = struct.unpack('<I', chunk_data[80:84])[0]
    pixelformat_dwFourCC = struct.unpack('<I', chunk_data[84:88])[0]
    pixelformat_dwRGBBitCount = struct.unpack('<I', chunk_data[88:92])[0]
    pixelformat_dwRBitMask = struct.unpack('<I', chunk_data[92:96])[0]
    pixelformat_dwGBitMask = struct.unpack('<I', chunk_data[96:100])[0]
    pixelformat_dwBBitMask = struct.unpack('<I', chunk_data[100:104])[0]
    pixelformat_dwABitMask = struct.unpack('<I', chunk_data[104:108])[0]
    
    # Caps and reserved2
    dwCaps = struct.unpack('<I', chunk_data[108:112])[0]
    dwCaps2 = struct.unpack('<I', chunk_data[112:116])[0]
    
    # Build header structure
    dds_header = {
        'dwSize': dwSize,
        'dwFlags': dwFlags,
        'dwHeight': dwHeight,
        'dwWidth': dwWidth,
        'dwPitchOrLinearSize': dwPitchOrLinearSize,
        'dwDepth': dwDepth,
        'dwMipMapCount': dwMipMapCount,
        'dwReserved1': [0] * 11,  # Not used
        'ddspf': {
            'dwSize': pixelformat_dwSize,
            'dwFlags': pixelformat_dwFlags,
            'dwFourCC': pixelformat_dwFourCC,
            'dwRGBBitCount': pixelformat_dwRGBBitCount,
            'dwRBitMask': pixelformat_dwRBitMask,
            'dwGBitMask': pixelformat_dwGBitMask,
            'dwBBitMask': pixelformat_dwBBitMask,
            'dwABitMask': pixelformat_dwABitMask,
        },
        'dwCaps': dwCaps,
        'dwCaps2': dwCaps2,
    }
    
    # DDS pixel format
    dds_pixel_format = dds_header['ddspf']
    
    # DDS data starts after the header
    dds_data = chunk_data[128:]
    
    # Determine texture format
    width = dds_header['dwWidth']
    height = dds_header['dwHeight']
    tex_format = None
    
    # Check format based on FourCC or flags
    dxt1_code = int('DXT1'.encode('ascii')[::-1].hex(), 16)
    dxt5_code = int('DXT5'.encode('ascii')[::-1].hex(), 16)
    
    if dds_pixel_format['dwFourCC'] == dxt1_code:
        tex_format = TEXFormat.DXT1
    elif dds_pixel_format['dwFourCC'] == dxt5_code:
        tex_format = TEXFormat.DXT5
    elif (dds_pixel_format['dwFlags'] & 0x00000041) == 0x00000041:
        if (dds_pixel_format['dwRGBBitCount'] != 32 or 
            dds_pixel_format['dwRBitMask'] != 0x000000ff or 
            dds_pixel_format['dwGBitMask'] != 0x0000ff00 or 
            dds_pixel_format['dwBBitMask'] != 0x00ff0000 or 
            dds_pixel_format['dwABitMask'] != 0xff000000):
            raise Exception('Ritoddstex: Failed: stream2tex: DDS file is not in exact RGBA8 format.')
        tex_format = TEXFormat.RGBA8
    else:
        raise Exception(f'Ritoddstex: Failed: stream2tex: Unsupported DDS format: {dds_pixel_format["dwFourCC"]}')
    
    # Check for mipmaps
    has_mipmaps = False
        
    
    
    # Prepare texture data
    tex_data = []
    
    if has_mipmaps:
        # Set block size and bytes per block based on format
        if tex_format in (TEXFormat.DXT1, TEXFormat.DXT1_):
            block_size = 4
            bytes_per_block = 8
        elif tex_format == TEXFormat.DXT5:
            block_size = 4
            bytes_per_block = 16
        else:  # RGBA8
            block_size = 1
            bytes_per_block = 4
        
        # Calculate and extract mipmap data
        mipmap_count = dds_header['dwMipMapCount']
        current_offset = 0
        
        for i in range(mipmap_count):
            current_width = max(width // (1 << i), 1)
            current_height = max(height // (1 << i), 1)
            block_width = (current_width + block_size - 1) // block_size
            block_height = (current_height + block_size - 1) // block_size
            current_size = bytes_per_block * block_width * block_height
            
            # Extract data for this mipmap level
            if current_offset + current_size <= len(dds_data):
                data = dds_data[current_offset:current_offset+current_size]
                tex_data.append(data)
                current_offset += current_size
            else:
                raise Exception(f'Ritoddstex: Failed: stream2tex: DDS data too small for mipmap {i}')
        
        # Mipmap order is reversed in TEX compared to DDS
        tex_data.reverse()
    else:
        # No mipmaps, just use the entire data
        tex_data = [dds_data]
    
    # Build TEX file in memory
    # TEX header: signature(4) + width(2) + height(2) + unknown1(1) + format(1) + unknown2(1) + mipmaps(1)
    tex_bytes = bytearray()
    
    # Signature: 'TEX\0' in little endian
    tex_bytes.extend(struct.pack('<I', 0x00584554))
    
    # Width and height (16-bit unsigned short)
    tex_bytes.extend(struct.pack('<HH', width, height))
    
    # unknown1, format, unknown2
    tex_bytes.extend(struct.pack('<BBB', 1, tex_format.value, 0))
    
    # Mipmaps flag (1 byte boolean)
    tex_bytes.extend(struct.pack('<B', 1 if has_mipmaps else 0))
    
    # Write texture data
    for block_data in tex_data:
        tex_bytes.extend(block_data)
    
    return bytes(tex_bytes)