#Always compile from this file

import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

from MainMenu import *
from GenericGraphics import *
import InputHandler

def main():
    InputStack = InputHandler.RecentInputs()
    (window, batch) = PrepareWindow(InputStack)
    MainMenu(window, batch, InputStack)

def PrepareWindow(InputStack):
    window = Window(width=800, height=800)
    batch = pyglet.graphics.Batch()
    
    @window.event
    def on_draw():
        GenericDraw(window, batch)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        GenericMousePress(InputStack, x, y, button)

    @window.event
    def on_key_press(symbol, modifiers):
        GenericKeyPress(InputStack, symbol)

    return (window, batch)

if __name__ == "__main__":
    main()

