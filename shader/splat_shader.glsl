shader_type spatial;
render_mode unshaded, blend_add;

uniform float time;

void fragment() {
    ALBEDO = vec3(1.0);
    ALPHA = 0.2;
}
