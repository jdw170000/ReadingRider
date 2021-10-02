from typing import Callable
import pyglet

class Button:
    def __init__(self, batch, order, text, x, y, width, height, font_name='Times New Roman', font_size=36, color=(90, 0, 90, 255)):
        self.batch = batch

        button_layer = pyglet.graphics.OrderedGroup(order)
        text_layer = pyglet.graphics.OrderedGroup(order + 1)

        self.button_rectangle = pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch, group=button_layer)
        self.button_text = pyglet.text.Label(text,font_name=font_name, font_size=font_size, x=x, y=y, color=color, batch=batch, group=text_layer)

        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_name = font_name
        self.font_size = font_size
        self.color = color
    
    def set_click_event(self, func: Callable):
        self.on_click = func

    def is_clicked(self, click_x, click_y):
        return (self.x <= click_x <= self.x + self.width) and (self.y <= click_y <= self.y + self.height)
    
    def click(self, *args):
        self.on_click(*args)
