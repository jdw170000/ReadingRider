
import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import Window
from pyglet import clock
from pyglet import app
import math
import json
import os

#Car vars
turning = 0
acceleration = 0
velocity_Y = 0
velocity_X = 0
posX = 0
posY = 0
batch2 = pyglet.graphics.Batch()
playerTriangle = pyglet.shapes.Triangle(385, 10, 415, 10, 400, 40, color=(100, 150, 0), batch=batch2, group=pyglet.graphics.OrderedGroup(2))

#path vars
pathIndex = 0
path = []
nextWords = []
distanceScrolledY = 0
labelledRects = []

#key handler
keys = key.KeyStateHandler()

def MoveCheckCollisions(arg):
    #TODO - collision checking
    global velocity_Y, velocity_X
    global posX
    global posY
    global playerTriangle
    posY += velocity_Y
    posX += velocity_X

def LoadPath():
    global nextWords
    global pathIndex
    global path
    file = open(os.getcwd()+"/paths/TEST.path")
    pathJson = json.load(file)
    path = pathJson['text']
    nextWords = path

def DrawPath2D(batch, background, midground):
    global nextWords
    global labelledRects
    global posY, poX
    global distanceScrolledY
    sizeMultiplier = 40
    bottomLeftX = 400 - nextWords[0][2] * sizeMultiplier / 2 - posX
    bottomLeftY = -posY
    for word in nextWords:    
        width = word[2] * sizeMultiplier
        height = word[2] * sizeMultiplier
        rect = pyglet.shapes.Rectangle(bottomLeftX, bottomLeftY, width, height, batch=batch, group=background)
        label = pyglet.text.Label(word[0],font_name="Consolas", font_size=50, x=bottomLeftX, y=bottomLeftY + height / 2 - 30, color=(0, 0, 0, 255), batch=batch, group=midground)
        labelledRects.append((rect, label))
        bottomLeftX += width * word[1]
        bottomLeftY += height

def DefineWindowEvents(window, background, midground):
    @window.event
    def on_draw():
        #this is the main loop
        global acceleration
        global velocity_Y
        global posX
        global posY
        global batch2
        #Car movement
        velocity_Y += acceleration * 1 # constant to be adjusted later

        #update graphics
        #DrawPath()
        window.clear()
        #DrawPath()
        batch = pyglet.graphics.Batch()
        DrawPath2D(batch, background, midground)
        batch.draw()
        batch2.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        global turning
        global acceleration
        global velocity_X
        global keys
        print(f'keypress: {velocity_X}')
        print(f'{symbol}')
        if symbol == key.A:
            print(f'keypress: A')
            velocity_X -= velocity_Y
        elif symbol == key.D:
            print(f'keypress: D')
            velocity_X += velocity_Y
        elif symbol == key.W:
            if acceleration < 1:
                acceleration += 1
        elif symbol == key.S:
            if acceleration > -1:
                acceleration += -1
    @window.event
    def on_key_release(symbol, modifiers):
        global turning
        global acceleration
        global keys
        global velocity_X
        print(f'keyrelease: {velocity_X}')
        if symbol == key.A:
            velocity_X = 0
        elif symbol == key.D:
            velocity_X = 0
        elif symbol == key.W:
            if acceleration > 0:
                acceleration += -1
        elif symbol == key.S:
            if acceleration < 0:
                acceleration += 1


def main():
    global keys

    window = Window(width=800, height=800)
    
    background = pyglet.graphics.OrderedGroup(0)
    midground = pyglet.graphics.OrderedGroup(1)
    foreground = pyglet.graphics.OrderedGroup(2)
    
    window.push_handlers(keys)

    LoadPath()
    
    
    DefineWindowEvents(window, background, midground)
    clock.schedule(MoveCheckCollisions)
    app.run()

if __name__ == "__main__":
    main()
