
# Interactive 3D Colored Cube

## About the Project
This project renders a colorful 3D cube using Python, Pygame, and OpenGL. Each face has a different color, and keyboard controls allow the user to transform the cube interactively.

## Features
- Six colored cube faces
- 3D rendering using OpenGL triangles
- Keyboard-controlled movement
- Rotation around the X, Y, and Z axes
- Scaling controls to enlarge or shrink the cube
- Depth testing for correct 3D visibility

## Controls

| Key | Action |
|---|---|
| A / D | Move left / right |
| W / S | Move up / down |
| Q / E | Move closer / farther |
| Up / Down arrows | Rotate around X axis |
| Left / Right arrows | Rotate around Y axis |
| Z / X | Rotate around Z axis |
| + / - | Scale up / down |
| Close window | Exit |

## Technologies Used
- Python
- Pygame
- PyOpenGL
- OpenGL GLU

## Installation

Install the required packages:

```bash
python -m pip install pygame PyOpenGL PyOpenGL_accelerate
```

## How to Run
1. Install Python and the required packages.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run:

```bash
python main.py
```

## Learning Objectives
- Defining 3D vertices and faces
- Splitting quadrilateral faces into triangles
- Applying OpenGL transformations
- Processing keyboard input
- Rendering interactive 3D graphics
