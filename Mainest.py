
import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import Window
from pyglet import app
import math
import json
import os

#Car vars
turning = 0
acceleration = 0
velocity = 0
rotation = math.pi # [0, 2pi)
posX = 0
posY = 0

def MoveCheckCollisions():
    #TODO - collision checking
    global velocity
    global rotation
    global posX
    global posY
    posX += velocity * math.cos(rotation + math.pi / 2)
    posY += velocity * math.sin(rotation + math.pi / 2)

def DrawPath():
    file = open(os.getcwd()+"/paths/UTD_ALERT.path")
    pathJson = json.load(file)

def DefineWindowEvents(window):
    @window.event
    def on_draw():
        #this is the main loop
        global turning
        global acceleration
        global velocity
        global rotation
        global posX
        global posY
        #Car movement
        rotation += turning * 1 # Constant to be adjusted later
        while (rotation >= 2 * math.pi):
            rotation += -2 * math.pi
        velocity += acceleration * 1 # constant to be adjusted later
        MoveCheckCollisions()

        #update graphics
        DrawPath()
        window.clear()
        batch.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        global turning
        global acceleration
        if keys[key.A]:
            if turning > -1:
                turning += -1
        elif keys[key.D]:
            if turning < 1:
                turning += 1
        elif keys[key.W]:
            if acceleration < 1:
                acceleration += 1
        elif keys[key.S]:
            if acceleration > -1:
                acceleration += -1
    @window.event
    def on_key_release(symbol, modifiers):
        global turning
        global acceleration
        if keys[key.A]:
            if turning < 0:
                turning += 1
        elif keys[key.D]:
            if turning > 0:
                turning += -1
        elif keys[key.W]:
            if acceleration > 0:
                acceleration += -1
        elif keys[key.S]:
            if acceleration < 0:
                acceleration += 1


def main():
    window = Window(width=800, height=800)
    batch = pyglet.graphics.Batch()
    background = pyglet.graphics.OrderedGroup(0)
    midground = pyglet.graphics.OrderedGroup(1)
    foreground = pyglet.graphics.OrderedGroup(2)
    keys = key.KeyStateHandler()
    window.push_handlers(keys)

    DefineWindowEvents(window)

    app.run()


if __name__ == "__main__":
    main()
