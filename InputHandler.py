import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

class MouseInput:
    x = y =  button = None
    def __init__(this, x, y, button):
        this.x = x
        this.y = y
        this.button = button
    def getX(this):
        return this.x
    def getY(this):
        return this.y
    def getButton(this):
        return this.button

class KeyInput:
    key = None
    def __init__(this, key):
        this.key = key
    def getKey(this):
        return this.key

class RecentInputs:
    mouseInputs = []
    keyInputs = []

    def __init__(this):
        this.mouseInputs = []
        this.keyInputs = []

    def addMouseInput(this, x, y, button):
        this.mouseInputs.append(MouseInput(x, y, button))

    def addKeyInput(this, key):
        this.keyInputs.append(KeyInput(key))

    def clearInputs(this):
        this.mouseInputs.clear()
        this.keyInputs.clear()

    def popMouseInputs(this):
        temp = this.mouseInputs.copy()
        this.mouseInputs.clear()
        return temp

    def popKeyInputs(this):
        temp = this.keyInputs.copy()
        this.keyInputs.clear()
        return temp