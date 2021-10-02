import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

from Graphics import *

def MainMenu(window, batch):
    button = pyglet.shapes.Rectangle(150, 240, 200, 20, color=(255, 55, 55), batch=batch)
    button2 = pyglet.shapes.Rectangle(100, 280, 200, 50, color=(255, 255, 55), batch=batch)

    app.run()