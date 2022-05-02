from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=2, exposure=10)
scene.set_floor(-0.05, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 0.9, 1.0))
scene.set_directional_light((0.7, 1, -1), 0.1, (0.95, 0.95, 0.8))


@ti.func
def create_block(pos, size, color, color_noise):
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]),
                       (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color + color_noise * ti.random())


@ti.func
def create_virtual(pos, size):
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]),
                       (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 0, vec3(0.5))

@ti.kernel
def initialize_voxels():
    color = vec3(0.99, 0.98, 0.9)

    create_block(vec3(0, 0, 0), vec3(50, 50, 50), color, vec3(0))

    create_virtual(vec3(38, 20, 20), vec3(5, 10, 30))
    create_virtual(vec3(20, 20, 38), vec3(30, 10, 5))

    create_block(vec3(38, 31, 50), vec3(5, 4, 1), color, vec3(0))
    create_block(vec3(39, 35, 50), vec3(3, 2, 1), color, vec3(0))

    create_virtual(vec3(39, 32, 20), vec3(3, 2, 31))
    create_virtual(vec3(40, 34, 20), vec3(1, 2, 31))

    create_block(vec3(50, 31, 38), vec3(1, 4, 5), color, vec3(0))
    create_block(vec3(50, 35, 39), vec3(1, 2, 3), color, vec3(0))

    create_virtual(vec3(20, 32, 39), vec3(31, 2, 3))
    create_virtual(vec3(20, 34, 40), vec3(31, 2, 1))

    scene.set_voxel(vec3(38, 38, 50), 1, color)
    scene.set_voxel(vec3(40, 40, 50), 1, color)
    scene.set_voxel(vec3(42, 38, 50), 1, color)

    scene.set_voxel(vec3(50, 38, 38), 1, color)
    scene.set_voxel(vec3(50, 40, 40), 1, color)
    scene.set_voxel(vec3(50, 38, 42), 1, color)

    scene.set_voxel(vec3(48, 35, 50), 1, color)
    scene.set_voxel(vec3(50, 35, 48), 1, color)

    for i, j in ti.ndrange((38, 43), (20, 30)):
        if i == 38 or i == 42 or j == 20 or j == 29:
            scene.set_voxel(vec3(i, j, 50), 1, color)
            scene.set_voxel(vec3(50, j, i), 1, color)

    create_block(vec3(38, 20, 50), vec3(5, 1, 5), color, vec3(0))
    create_block(vec3(50, 20, 38), vec3(5, 1, 5), color, vec3(0))

    create_block(vec3(50, 25, 43), vec3(5, 1, 7), color, vec3(0))
    create_block(vec3(49, 25, 50), vec3(6, 1, 5), color, vec3(0))

    for i in range(6):
        create_block(vec3(43, 20, 50) + vec3(1, 1, 0) * i, ivec3(2, 1, 5), color, vec3(0))

    create_block(vec3(52, 20, 42), vec3(1, 7, 1), color, vec3(0))
    create_block(vec3(54, 20, 42), vec3(1, 7, 1), color, vec3(0))

    for i in range(7 // 2):
        create_block(vec3(53, 21, 42) + vec3(0, 1, 0) * i * 2, vec3(1, 1, 1), color, vec3(0))




initialize_voxels()

scene.finish()
