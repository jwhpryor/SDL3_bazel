package(default_visibility = ["//visibility:public"])

# Header-only library for now
cc_library(
    name = "bimg",
    hdrs = glob([
        "include/**/*.h",
    ]),
    includes = ["include"],
    deps = ["@com_github_bx//:bx"],
    visibility = ["//visibility:public"],
)