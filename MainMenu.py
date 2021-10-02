import pyglet
from pyglet.window import Window
from pyglet import app
from pyglet.gl import *

from GenericGraphics import *

from InputHandler import *

def MainMenu(window, batch, InputStack):
    currentGraphicItems = MainMenuGraphics(batch)

    
    app.run()

def MainMenuGraphics(batch):
    background = pyglet.graphics.OrderedGroup(0)
    foreground = pyglet.graphics.OrderedGroup(1)
    playButton = pyglet.shapes.Rectangle(300, 550, 200, 50, color=(200, 200, 200), batch=batch, group=background)
    playLabel = pyglet.text.Label('Play',font_name='Times New Roman', font_size=36, x=350, y=562, color=(90, 0, 90, 255), batch=batch, group=foreground)
    currentGraphicItems = []
    currentGraphicItems.append(playButton)
    currentGraphicItems.append(playLabel)
    return currentGraphicItems

def ClickHandler(InputStack):
    mouseInputs = InputStack.popMouseInputs()
    for input in mouseInputs:
        if(input.getButton() == 1):
            if(input.getX() > playButton.x and input.getX() < playButton.x * playButton.width):
                if(input.getY() > playButton.y and input.getY() < playButton.y * playButton.height):
                    #button was clicked
                    return 'Play'