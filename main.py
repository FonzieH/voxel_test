from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=2, exposure=12)
scene.set_floor(-1.0, (1.0, 1.0, 1.0))
scene.set_background_color((1.0, 0.9, 1.0))
scene.set_directional_light((0.7, 1, -0.5), 0.1, (1.0, 1.0, 1.0))


@ti.func
def create_block(pos, size, color, color_noise, symmetry=False):
    rotate_matrix = ti.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]),
                       (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 1, color + color_noise * ti.random())
        if symmetry:
            scene.set_voxel(rotate_matrix@I, 1, color + color_noise * ti.random())


@ti.func
def create_virtual(pos, size, symmetry=False):
    rotate_matrix = ti.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
    for I in ti.grouped(
            ti.ndrange((pos[0], pos[0] + size[0]),
                       (pos[1], pos[1] + size[1]),
                       (pos[2], pos[2] + size[2]))):
        scene.set_voxel(I, 0, vec3(0.5))
        if symmetry:
            scene.set_voxel(rotate_matrix@I, 0, vec3(0.5))


@ti.func
def create_decor(pos, width, height, color, symmetry=True):

    create_block(pos, vec3(width, height, 1), color, vec3(0), symmetry)
    create_virtual(pos + vec3(1, 1, -20), vec3(width - 2, height-2, 31), symmetry)

    i, j = width, height
    new_pos = pos
    while i > 4 and j > 2:
        new_pos = new_pos + vec3(1, j - 1, 0)
        create_block(new_pos, vec3(i - 2, j - 1, 1), color, vec3(0), symmetry)
        create_virtual(new_pos + vec3(1, 0, -20), vec3(i - 4, j - 2, 31), symmetry)

        i -= 2
        j -= 1

@ti.kernel
def initialize_voxels():
    color = vec3(0.8, 0.94, 1.0)
    create_block(vec3(-50, -50, -50), vec3(100, 100, 100), color, vec3(0))

    pos = vec3(20, 20, 50)

    create_decor(pos, 9, 5, color)

    create_block(pos + vec3(2, 13, 0), vec3(1, 1, 1), color, vec3(0), symmetry=True)
    create_block(pos + vec3(4, 15, 0), vec3(1, 1, 1), color, vec3(0), symmetry=True)
    create_block(pos + vec3(6, 13, 0), vec3(1, 1, 1), color, vec3(0), symmetry=True)

    create_block(pos + vec3(0, -21, 0), vec3(9, 20, 1), color, vec3(0), symmetry=True)
    create_virtual(pos + vec3(1, -21, -20), vec3(7, 19, 31), symmetry=True)

    create_block(vec3(49, 27, 49), vec3(2, 2, 2), color, vec3(0)) # base height +7
    create_block(vec3(44, 27, 50), vec3(2, 2, 1), color, vec3(0), symmetry=True)

    create_block(pos + vec3(0, -21, 0), vec3(9, 1, 9), color, vec3(0), symmetry=True)

    for i in range(12):
        create_block(pos + vec3(9, -21, 0) + vec3(1, 1, 0) * i, ivec3(2, 1, 9), color, vec3(0))

    create_block(pos + vec3(20, -10, 0), ivec3(10, 1, 9), color, vec3(0))
    create_block(ti.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])@(pos + vec3(9, -10, 0)), ivec3(9, 1, 30), color, vec3(0))

    create_block(vec3(54, -1, 28), vec3(1, 15, 1), color, vec3(0))
    create_block(vec3(57, -1, 28), vec3(1, 15, 1), color, vec3(0))

    for i in range(15 // 2):
        create_block(vec3(54, 0, 28) + vec3(0, 1, 0) * i * 2, vec3(4, 1, 1), color, vec3(0))

initialize_voxels()

scene.finish()
