#version 330 core

layout (location = 0) in vec2 aPos;
layout (location = 1) in vec2 aTexCoord;

out vec2 texCoord;

uniform vec2 position;
uniform vec2 scale;

void main()
{
    vec2 transformedPos = aPos * scale + position;
    gl_Position = vec4(transformedPos, 0.0, 1.0);
    texCoord = aTexCoord;
}