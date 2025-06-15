load("@emsdk//emscripten_toolchain:wasm_rules.bzl", "wasm_cc_binary")

cc_library(
  name = "game_headers",
  hdrs = [
    "game.h"
  ],
  deps = [
    "@com_github_sdl//:sdl3_shared",
  ],
  visibility = ["//:__pkg__"],
)

cc_binary(
  name = "game",
  srcs = glob(["game.*"]),
  deps = [
    ":game_headers",
  ],
  linkshared = True,
  visibility = ["//:__pkg__"],
)

cc_binary(
  name = "engine",
  data = [":game"],
  srcs = glob(["engine.*", "main.cpp"]),
  deps = [
    "@com_github_sdl//:sdl3_shared",
    "@com_github_bgfx//:bgfx",
    ":game_headers",
  ],
  visibility = ["//:__pkg__"],
)

cc_binary(
  name = "release",
  srcs = glob(["*.cpp", "*.h"], exclude=["main.cpp"]),
  deps = [
    "@com_github_sdl//:sdl3_shared"
  ],
  visibility = ["//:__pkg__"],
)

cc_binary(
    name = "release-static-linked",
    srcs = glob(["*.cpp", "*.h"], exclude=["main.cpp"]),
    deps = [
        "@com_github_sdl//:sdl3_static",
    ],
    visibility = ["//:__pkg__"],
)

wasm_cc_binary(
  name = "sdl3-wasm",
  cc_target = ":release-static-linked",
  # emcc main.cpp -o sdl3-wasm.html
  outputs = [
    "sdl3-wasm.html",
    "sdl3-wasm.wasm",
    "sdl3-wasm.js"
  ],
  visibility = ["//:__pkg__"],
)

