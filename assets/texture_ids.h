#pragma once

#include <string_view>

namespace absl::assets::textures {

enum class TextureId {
    kARROW,
    kONLINE,
    kSTART,
    kTITLE,
};

auto GetTexturePath(TextureId asset_id) -> std::string_view;

inline auto GetTexturePath(TextureId asset_id) -> std::string_view {
  switch (asset_id) {
    case TextureId::kARROW:
      return "assets/textures/arrow.png";
    case TextureId::kONLINE:
      return "assets/textures/online.png";
    case TextureId::kSTART:
      return "assets/textures/start.png";
    case TextureId::kTITLE:
      return "assets/textures/title.png";
  }
  return "";
}

}  // namespace absl::assets::textures
