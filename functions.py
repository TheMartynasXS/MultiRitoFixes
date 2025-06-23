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
    pixelformat_dwBBitMask = struct.unpack('<I', chunk_data[92:96])[0]
    pixelformat_dwGBitMask = struct.unpack('<I', chunk_data[96:100])[0]
    pixelformat_dwRBitMask = struct.unpack('<I', chunk_data[100:104])[0]
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
    dxt3_code = int('DXT3'.encode('ascii')[::-1].hex(), 16)
    if dds_pixel_format['dwFourCC'] == dxt3_code:
        dds_data = convert_dxt3_to_dxt5_bytes(dds_data, width, height)
        dds_pixel_format['dwFourCC'] = dxt5_code

    if dds_pixel_format['dwFourCC'] == dxt1_code:
        tex_format = TEXFormat.DXT1
    elif dds_pixel_format['dwFourCC'] == dxt5_code:
        tex_format = TEXFormat.DXT5
    elif (dds_pixel_format['dwFlags'] & 0x00000041) == 0x00000041:
        # BGRA8 in DDS: B=0x000000ff, G=0x0000ff00, R=0x00ff0000, A=0xff000000
        if (dds_pixel_format['dwRGBBitCount'] != 32 or 
            dds_pixel_format['dwRBitMask'] != 0x000000ff or 
            dds_pixel_format['dwGBitMask'] != 0x0000ff00 or 
            dds_pixel_format['dwBBitMask'] != 0x00ff0000 or 
            dds_pixel_format['dwABitMask'] != 0xff000000):
            print(dds_pixel_format)
            # print actual pixel bit mask as hex
            print(f"R: {dds_pixel_format['dwRBitMask']:08x}, G: {dds_pixel_format['dwGBitMask']:08x}, B: {dds_pixel_format['dwBBitMask']:08x}, A: {dds_pixel_format['dwABitMask']:08x}")
            raise Exception('Ritoddstex: Failed: stream2tex: DDS file is not in exact BGRA8 format.')
        tex_format = TEXFormat.RGBA8  # This is actually BGRA8 in DDS
    else:
        print(f"other: {TEXFormat.DXT1} {TEXFormat.DXT5}")
        print(f"pixel format: {dds_pixel_format['dwFourCC']}")
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

def convert_dxt3_to_dxt5_bytes(dxt3_bytes, width, height):
    """
    Converts a DXT3 DDS image (as bytes) to DXT5 DDS image (as bytes).
    Only the pixel data is converted; header must be handled externally if needed.
    """
    import io

    # DXT3 and DXT5 both use 16 bytes per 4x4 block
    block_w = (width + 3) // 4
    block_h = (height + 3) // 4
    block_count = block_w * block_h

    dxt3_stream = io.BytesIO(dxt3_bytes)
    dxt5_data = bytearray()

    def convert_dxt3_alpha_to_dxt5(block8):
        # block8: 8 bytes DXT3 alpha block
        # Returns: 8 bytes DXT5 alpha block
        # 1. Extract 16 4-bit alpha values
        alphas = []
        for i in range(0, 8, 2):
            byte = block8[i] | (block8[i+1] << 8)
            alphas.append(byte & 0xF)
            alphas.append((byte >> 4) & 0xF)
        # Scale 4-bit alpha to 8-bit
        alphas = [int(a * 17) for a in alphas]
        # Find min/max
        alpha0 = max(alphas)
        alpha1 = min(alphas)
        # Build alpha lookup table (DXT5 spec)
        alpha_table = [alpha0, alpha1]
        if alpha0 > alpha1:
            for i in range(1, 7):
                alpha_table.append(((7-i)*alpha0 + i*alpha1)//7)
        else:
            for i in range(1, 5):
                alpha_table.append(((5-i)*alpha0 + i*alpha1)//5)
            alpha_table.extend([0, 255])
        # For each alpha, find closest index in table
        indices = []
        for a in alphas:
            best = min(range(8), key=lambda i: abs(alpha_table[i] - a))
            indices.append(best)
        # Pack indices into 6 bytes (3 bits per alpha, 16 alphas)
        bits = 0
        bitlen = 0
        packed = bytearray()
        for idx in indices:
            bits |= (idx & 0x7) << bitlen
            bitlen += 3
            if bitlen >= 8:
                packed.append(bits & 0xFF)
                bits >>= 8
                bitlen -= 8
        while len(packed) < 6:
            packed.append(bits & 0xFF)
            bits >>= 8
        # Compose DXT5 alpha block
        return bytes([alpha0, alpha1]) + packed

    for _ in range(block_count):
        alpha_block = dxt3_stream.read(8)
        color_block = dxt3_stream.read(8)
        dxt5_alpha = convert_dxt3_alpha_to_dxt5(alpha_block)
        dxt5_data.extend(dxt5_alpha)
        dxt5_data.extend(color_block)

    return bytes(dxt5_data)