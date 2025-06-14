package(default_visibility = ["//visibility:public"])

# Header-only library for now, just to verify bgfx headers are accessible
cc_library(
    name = "bgfx",
    hdrs = glob([
        "include/**/*.h",
    ]),
    includes = ["include"],
    deps = [
        "@com_github_bx//:bx",
        "@com_github_bimg//:bimg",
    ],
    visibility = ["//visibility:public"],
)