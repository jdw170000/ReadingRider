import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

import InputHandler

def GenericDraw(window, batch):
    window.clear()
    batch.draw();

def GenericMousePress(InputStack, x, y, button):
    InputStack.addMouseInput(x, y, button)

def GenericKeyPress(InputStack, key):
    InputStack.addKeyInput(key)
