package(default_visibility = ["//visibility:public"])

# Header-only library for now
cc_library(
    name = "bx",
    hdrs = glob([
        "include/**/*.h",
        "include/**/*.inl",
    ]),
    includes = ["include"],
    copts = [
        "-std=c++17",
        "-DBX_CONFIG_DEBUG=0",
    ] + select({
        "@bazel_tools//src/conditions:darwin": [
            "-DBX_PLATFORM_OSX=1",
        ],
        "@bazel_tools//src/conditions:linux": [
            "-DBX_PLATFORM_LINUX=1",
        ],
        "@bazel_tools//src/conditions:windows": [
            "-DBX_PLATFORM_WINDOWS=1",
        ],
        "//conditions:default": [],
    }),
    visibility = ["//visibility:public"],
)