exports_files([
    "textures/arrow.png",
    "textures/online.png",
    "textures/start.png", 
    "textures/title.png",
    "generate_asset_ids.py",
    "shaders/basic.vert",
    "shaders/basic.frag",
    "shaders/textured.vert",
    "shaders/textured.frag", 
    "shaders/positioned.vert",
    "shaders/positioned.frag",
    "id.h",
])

# Generate texture IDs
genrule(
    name = "generate_texture_ids",
    srcs = [
        "textures/arrow.png",
        "textures/online.png", 
        "textures/start.png",
        "textures/title.png",
        "generate_asset_ids.py",
    ],
    outs = ["texture_ids.h"],
    cmd = "python3 $(location generate_asset_ids.py) assets/textures $(OUTS) textures Texture .png",
    visibility = ["//visibility:public"],
)

cc_library(
    name = "texture_ids",
    hdrs = ["texture_ids.h"],
    visibility = ["//visibility:public"],
)

# Generate shader IDs  
genrule(
    name = "generate_shader_ids",
    srcs = [
        "shaders/basic.vert",
        "shaders/basic.frag",
        "shaders/textured.vert", 
        "shaders/textured.frag",
        "shaders/positioned.vert",
        "shaders/positioned.frag",
        "generate_asset_ids.py",
    ],
    outs = ["shader_ids.h"],
    cmd = "python3 $(location generate_asset_ids.py) assets/shaders $(OUTS) shaders Shader .vert,.frag",
    visibility = ["//visibility:public"],
)

cc_library(
    name = "shader_ids",
    hdrs = ["shader_ids.h"],
    visibility = ["//visibility:public"],
)

# Top-level asset IDs for easy reference
cc_library(
    name = "id",
    hdrs = ["id.h"],
    deps = [
        ":texture_ids",
        ":shader_ids",
    ],
    visibility = ["//visibility:public"],
)

