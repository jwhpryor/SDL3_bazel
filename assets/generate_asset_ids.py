#!/usr/bin/env python3
"""Generate asset IDs header with enum for all asset files."""

import os
import sys
from pathlib import Path

def generate_enum_name(filename, include_extension=False):
    """Convert filename to enum constant name."""
    if include_extension:
        # Use full filename including extension for unique names
        name = Path(filename).name.replace('.', '_')
    else:
        # Use only stem (no extension)
        name = Path(filename).stem
    # Convert to SCREAMING_SNAKE_CASE
    return name.upper().replace('-', '_').replace(' ', '_')

def generate_asset_header(asset_dir, output_file, namespace, asset_type, file_extensions):
    """Generate the asset header file."""
    
    # Find all files with specified extensions in asset directory
    asset_files = []
    for file in os.listdir(asset_dir):
        if any(file.endswith(ext) for ext in file_extensions):
            asset_files.append(file)
    
    asset_files.sort()  # Ensure consistent ordering
    
    # Generate header content
    header_content = f"""#pragma once

#include <string_view>

namespace assets::{namespace} {{

enum class {asset_type}Id {{
"""
    
    # Determine if we need to include extensions (for uniqueness)
    include_ext = len(file_extensions) > 1
    
    # Add enum values
    for asset_file in asset_files:
        enum_name = generate_enum_name(asset_file, include_ext)
        header_content += f"    k{enum_name},\n"
    
    header_content += "};\n\n"
    header_content += f"std::string_view Get{asset_type}Path({asset_type}Id asset_id);\n\n"
    header_content += f"inline std::string_view Get{asset_type}Path({asset_type}Id asset_id) {{\n"
    header_content += "    switch (asset_id) {\n"
    
    for asset_file in asset_files:
        enum_name = generate_enum_name(asset_file, include_ext)
        header_content += f'        case {asset_type}Id::k{enum_name}: return "{asset_dir}/{asset_file}";\n'
    
    header_content += "    }\n"
    header_content += "    return \"\";\n"
    header_content += "}\n\n"
    header_content += f"}} // namespace assets::{namespace}\n"
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write(header_content)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: generate_asset_ids.py <asset_dir> <output_file> <namespace> <asset_type> <extensions>")
        print("Example: generate_asset_ids.py assets texture_ids.h textures Texture .png")
        print("Example: generate_asset_ids.py assets/shaders shader_ids.h shaders Shader .vert,.frag")
        sys.exit(1)
    
    asset_dir = sys.argv[1]
    output_file = sys.argv[2]
    namespace = sys.argv[3]
    asset_type = sys.argv[4]
    extensions = sys.argv[5].split(',')
    
    generate_asset_header(asset_dir, output_file, namespace, asset_type, extensions)