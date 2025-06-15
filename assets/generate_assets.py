#!/usr/bin/env python3
"""Generate assets header with enum for all asset files."""

import os
import sys
from pathlib import Path

def generate_enum_name(filename):
    """Convert filename to enum constant name."""
    name = Path(filename).stem  # Remove extension
    # Convert to SCREAMING_SNAKE_CASE
    return name.upper().replace('-', '_').replace(' ', '_')

def generate_assets_header(assets_dir, output_file):
    """Generate the assets header file."""
    
    # Find all PNG files in assets directory
    png_files = []
    for file in os.listdir(assets_dir):
        if file.endswith('.png'):
            png_files.append(file)
    
    png_files.sort()  # Ensure consistent ordering
    
    # Generate header content
    header_content = f"""#pragma once

#include <string_view>

namespace assets {{

enum class AssetId {{
"""
    
    # Add enum values
    for png_file in png_files:
        enum_name = generate_enum_name(png_file)
        header_content += f"    k{enum_name},\n"
    
    header_content += """};

std::string_view GetAssetPath(AssetId asset_id);

inline std::string_view GetAssetPath(AssetId asset_id) {
    switch (asset_id) {
"""
    
    for png_file in png_files:
        enum_name = generate_enum_name(png_file)
        header_content += f'        case AssetId::k{enum_name}: return "assets/{png_file}";\n'
    
    header_content += """    }
    return "";
}

} // namespace assets
"""
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write(header_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: generate_assets.py <assets_dir> <output_file>")
        sys.exit(1)
    
    assets_dir = sys.argv[1]
    output_file = sys.argv[2]
    
    generate_assets_header(assets_dir, output_file)