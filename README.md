# <a name="title">Taichi Voxel Challenge</a>

<p align="center">
<img src=".\screenshots\res.jpg" width="50%"></img>
</p>

> Figure: result of `python3 main.py`. 

* Inspired by Sir Carma. This was an imitation of his work. you can find original one in ref.jpg 

----

We invite you to create your voxel artwork, by putting your [Taichi](https://github.com/taichi-dev/taichi) code in `main.py`!

Rules:

+ You can only import two modules: `taichi` (`pip` installation guide below) and `scene.py` (in the repo).
+ The code in `main.py` cannot exceed 99 lines. Each line cannot exceed 120 characters.

The available APIs are:

+ `scene = Scene(voxel_edges, exposure)`
+ `scene.set_voxel(voxel_id, material, color)`
+ `material, color = scene.get_voxel(voxel_id)`
+ `scene.set_floor(height, color)`
+ `scene.set_directional_light(dir, noise, color)`
+ `scene.set_background_color(color)`

Remember to call `scene.finish()` at last.

**Taichi Lang documentation:** https://docs.taichi-lang.org/

**Modifying files other than `main.py` is not allowed.**


## Installation

Make sure your `pip` is up-to-date:

```bash
pip3 install pip --upgrade
```

Assume you have a Python 3 environment, simply run:

```bash
pip3 install -r requirements.txt
```

to install the dependencies of the voxel renderer.

## Quickstart

```sh
python3 example1.py  # example2/3/.../7/8.py
```

Mouse and keyboard interface:

+ Drag with your left mouse button to rotate the camera.
+ Press `W/A/S/D/Q/E` to move the camera.
+ Press `P` to save a screenshot.


## Show your artwork 

Please put your artwork at the beginning of this README file. Replacing the `demo.jpg` file with your creation will do the job.
