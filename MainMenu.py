import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

from GenericGraphics import *

def MainMenu(window, batch, InputStack):
    MainMenuGraphics(batch)

    PrepareEventLoop(InputStack)

    app.run()

def MainMenuGraphics(batch):
    background = pyglet.graphics.OrderedGroup(0)
    foreground = pyglet.graphics.OrderedGroup(1)
    playButton = pyglet.shapes.Rectangle(300, 550, 200, 50, color=(200, 200, 200), batch=batch, group=background)
    playButton.opacity = 255
    playLabel = pyglet.text.Label('Play',font_name='Times New Roman', font_size=36, x=350, y=562, color=(200, 0, 90, 255), batch=batch, group=foreground)

def PrepareEventLoop(InputStack):
    event_loop = pyglet.app.EventLoop()

    @event_loop.event
    def on_exit():
        l = InputStack.popKeyInputs()
        for key in l:
            print(key)