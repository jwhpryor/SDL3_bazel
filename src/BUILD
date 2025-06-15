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
  srcs = [
    "game.cpp",
    "game.h",
  ],
  deps = [
    ":game_headers",
  ],
  linkshared = True,
  visibility = ["//:__pkg__"],
)

cc_binary(
  name = "engine",
  data = [":game"],
  srcs = [
    "engine.cpp",
    "engine.h", 
    "main.cpp",
  ],
  deps = [
    "@com_github_sdl//:sdl3_shared",
    "@com_github_bgfx//:bgfx",
    ":game_headers",
  ],
  visibility = ["//:__pkg__"],
)

