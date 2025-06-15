#version 330 core

in vec2 texCoord;
out vec4 FragColor;

uniform sampler2D titleTexture;

void main()
{
    FragColor = texture(titleTexture, texCoord);
}
