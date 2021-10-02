#Always compile from this file

import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

from MainMenu import *

def main():
    (window, batch) = PrepareWindow()
    MainMenu(window, batch)

    app.run() # main event loop, returns when all windows are closed

def PrepareWindow():
    window = Window(width=800, height=800)
    batch = pyglet.graphics.Batch()
    @window.event
    def on_draw():
        GenericDraw(window, batch)
    return (window, batch)

if __name__ == "__main__":
    main()

