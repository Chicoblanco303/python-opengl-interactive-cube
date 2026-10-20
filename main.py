import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

VERTICES = (
 (1, 1, 1), # 0
 (1, 1, -1), # 1
 (1, -1, -1), # 2
 (1, -1, 1), # 3
 (-1, 1, 1), # 4
 (-1, -1, -1), # 5
 (-1, -1, 1), # 6
 (-1, 1, -1), # 7
)

FACES = (
 ((0, 1, 2, 3), (1, 1, 0)), 
 ((4, 7, 5, 6), (0, 0, 1)), 
 ((0, 1, 7, 4), (0, 1, 1)), 
 ((3, 2, 5, 6), (1, 0, 1)), 
 ((0, 3, 6, 4), (0, 1, 0)), 
 ((1, 2, 5, 7), (1, 0, 0)), 
)
def draw_cube():
 glBegin(GL_TRIANGLES)
 for (a, b, c, d), color in FACES:
 glColor3f(*color) 
 for i in (a, b, c, a, c, d): 
 glVertex3f(*VERTICES[i])
 glEnd()

KEY_ACTIONS = {
 K_a: lambda: glTranslatef(-1, 0, 0), 
 K_d: lambda: glTranslatef(1, 0, 0), 
 K_w: lambda: glTranslatef(0, 1, 0), 
 K_s: lambda: glTranslatef(0, -1, 0), 
 K_q: lambda: glTranslatef(0, 0, 1), 
 K_e: lambda: glTranslatef(0, 0, -1), 
 K_UP: lambda: glRotatef(10, 1, 0, 0), 
 K_DOWN: lambda: glRotatef(-10, 1, 0, 0),
 K_LEFT: lambda: glRotatef(10, 0, 1, 0), 
 K_RIGHT: lambda: glRotatef(-10, 0, 1, 0),
 K_z: lambda: glRotatef(10, 0, 0, 1), 
 K_x: lambda: glRotatef(-10, 0, 0, 1),
 K_EQUALS: lambda: glScalef(1.1, 1.1, 1.1), 
 K_MINUS: lambda: glScalef(0.9, 0.9, 0.9), 
}
def main():
 pygame.init()
 display = (800, 600)
 pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
 pygame.display.set_caption("04 Lab 1")
 pygame.key.set_repeat(200, 50) 
 glEnable(GL_DEPTH_TEST) 
 gluPerspective(45, display[0] / display[1], 0.1, 50.0)
 glTranslatef(0, 0, -7) 
 glScalef(0.5, 0.5, 0.5) 
 running = True
 while running:
 for event in pygame.event.get():
 if event.type == pygame.QUIT:
 running = False
 elif event.type == pygame.KEYDOWN:
 action = KEY_ACTIONS.get(event.key)
 if action:
 action()
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 draw_cube()
 pygame.display.flip()
 pygame.time.wait(10)
 pygame.quit()
main()
