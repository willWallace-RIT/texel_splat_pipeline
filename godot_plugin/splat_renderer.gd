extends Node3D

@export var splat_resource: SplatResource
var material: ShaderMaterial

func _ready():
    material = ShaderMaterial.new()
    material.shader = load("res://shaders/splat_shader.glsl")

func _process(delta):
    if splat_resource:
        # pass data to GPU (simplified placeholder)
        material.set_shader_parameter("time", Time.get_ticks_msec())
