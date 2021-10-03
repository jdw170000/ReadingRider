
import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import Window
from pyglet import clock
from pyglet import app
import math
import json
import os
import random
from PygletButton import *

#Car vars
turning = 0
acceleration = 0
velocity_Y = 0
velocity_X = 0
posX = 400
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

answerButtons = []
score = 0
questionIndex = 0
maxScore = 0

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
    global posY, posX
    global velocity_Y
    global distanceScrolledY
    sizeMultiplier = 40

    if posY < 0:
        posY = 0
    
    collision = True
    win = True
    while collision:
        bottomLeftX = 400 - nextWords[0][2] * sizeMultiplier / 2 - (posX-400)
        bottomLeftY = -posY
        currentXOffset = 0
        collision = False
        labelledRects.clear()
        for word in nextWords:    
            width = word[2] * sizeMultiplier
            height = word[2] * sizeMultiplier
            if bottomLeftY-5 < 40 < bottomLeftY+height+5:
                win = False
                if bottomLeftX > 400:
                    posX = 400
                    posY = 0
                    velocity_Y = 0
                    collision = True
                    break
                if bottomLeftX + width < 400:
                    posX = 400
                    posY = 0
                    collision = True
                    break

            rect = pyglet.shapes.Rectangle(bottomLeftX, bottomLeftY, width, height, batch=batch, group=background)
            label = pyglet.text.Label(word[0],font_name="Consolas", font_size=50, x=bottomLeftX, y=bottomLeftY + height / 2 - 30, color=(0, 0, 0, 255), batch=batch, group=midground)
            labelledRects.append((rect, label))
            
            bottomLeftX += width * word[1]
            currentXOffset += width * word[1]
            bottomLeftY += height

    return win

def QuizMode(batch3):
    global answerButtons
    global questionIndex
    file = open(os.getcwd()+"/paths/TEST.path")
    pathJson = json.load(file)
    questions = pathJson['questions']
    if questionIndex >= len(questions):
        return True
    question = questions[questionIndex]
    pyglet.text.Label(question[0],font_name="Times New Roman", font_size=50, x=200, y=600, color=(255, 255, 255, 255), batch=batch3)
    
    answers = list()
    x = 100
    y = 100
    width = 45
    height = 75
    correct_answer = question[1][0]
#    correct_answer_button = PygletButton(batch3, 0, correct_answer, x, y, width, height)
#    correct_answer_button.set_click_event(lambda: True)
#    correct_index = random.randint(len(question[1]))
    random.seed(sum([ord(c) for c in question[0]]))
    random.shuffle(question[1])
    answerButtons.clear()
    for answer in question[1]:
        correct = answer == correct_answer
        answer_button = Button(batch3, 0, answer, x, y, width*len(answer), height, correct)
        answerButtons.append(answer_button)
        x += 10 + width*len(answer)
    return False


def DefineWindowEvents(window, background, midground):
    @window.event
    def on_draw():
        #this is the main loop
        global acceleration
        global velocity_Y
        global posX
        global posY
        global batch2
        global score
        global questionIndex
        #Car movement
        velocity_Y += acceleration * 1 # constant to be adjusted later

        #update graphics
        #DrawPath()
        window.clear()
        #DrawPath()
        batch = pyglet.graphics.Batch()
        if DrawPath2D(batch, background, midground):
            batch3 = pyglet.graphics.Batch()
            if QuizMode(batch3):
                pyglet.text.Label(f"{score}/{questionIndex}",font_name="Times New Roman", font_size=50, x=200, y=600, color=(255, 255, 255, 255), batch=batch3)
            batch3.draw()
        else:
            batch.draw()
            batch2.draw()

    @window.event
    def on_key_press(symbol, modifiers):
        global turning
        global acceleration
        global velocity_X
        global keys
        if symbol == key.A:
            velocity_X -= velocity_Y + 1
        elif symbol == key.D:
            velocity_X += velocity_Y + 1
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

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global answerButtons
        global score
        global questionIndex

        clicked = True
        for button in answerButtons:
            if button.is_clicked(x, y):
                if clicked:
                    questionIndex += 1
                clicked = False
                correct = button.click()
                if correct:
                    score += 1
                    
        

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
