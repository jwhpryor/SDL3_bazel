#pragma once

#include <string_view>

namespace assets::shaders {

enum class ShaderId {
  kBasicFrag,
  kBasicVert,
  kPositionedFrag,
  kPositionedVert,
  kTexturedFrag,
  kTexturedVert,
};

auto GetShaderPath(ShaderId asset_id) -> std::string_view;

inline auto GetShaderPath(ShaderId asset_id) -> std::string_view {
  switch (asset_id) {
    case ShaderId::kBasicFrag:
      return "assets/shaders/basic.frag";
    case ShaderId::kBasicVert:
      return "assets/shaders/basic.vert";
    case ShaderId::kPositionedFrag:
      return "assets/shaders/positioned.frag";
    case ShaderId::kPositionedVert:
      return "assets/shaders/positioned.vert";
    case ShaderId::kTexturedFrag:
      return "assets/shaders/textured.frag";
    case ShaderId::kTexturedVert:
      return "assets/shaders/textured.vert";
  }
  return "";
}

} // namespace assets::shaders
