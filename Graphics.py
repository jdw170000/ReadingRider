import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

def GenericDraw(window, batch):
    window.clear()
    batch.draw();