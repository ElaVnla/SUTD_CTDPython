# IMPORT Libraries
from turtle import *
from random import *
import turtle
import tkinter as tk
import time
import Class 

# TEXT Designs
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

# SCREEN LAYOUT ======================================

# SCREEN SETUPScreenuifunctions
def Screen_Setup():
    #setup(900,500)
    title("Keyboard Warriors: Adventure in SPACE(bar)")
    speed(0)
    


# FUNCTIONS FOR BACKGROUND DESIGNS HERE ===============

# Design for Home Screen ====================================
def Home_Screen():
    image = "Images/homescreenbackground.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)
    return screen

def Play_Button(ChangeTo_GamePlay,ChangeTo_Scoreboard,ChangeTo_Quit):
    canvas = turtle.getcanvas()
    parent = canvas.master
    #parent.geometry('500x500')

    button1 = tk.Button(parent, text="Let's Play", fg='light grey', bg='navy', command=ChangeTo_GamePlay)
    id1 = canvas.create_window((0,0), window=button1)

    button2 = tk.Button(parent, text='Scoreboard', fg='light grey', bg='navy', command=ChangeTo_Scoreboard)
    id2 = canvas.create_window((100,0), window=button2)

    button3 = tk.Button(parent, text='Leave', fg='light grey', bg='navy', command=ChangeTo_Quit)
    id3 = canvas.create_window((200,0), window=button3)

# Design for Scoreboard Screen ===========================================
def Scoreboard_Screen():
    image = "Images/scoreboard.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)
    return screen

# Design for Game Over Screen ============================================
def Gameover_Screen():
    pass

#  Design for Game Screen ===============================================
def Gameplay_Screen():
    tracer(0)

    sprites=[]
    player=Class.Player()
    ship=Class.Ship()
    #sprites.append(player)
    #sprites.append(ship)
    for _ in range(5):
            asteroid = Class.Asteroid()
            x = randint(-450, 450)
            y = 250
            asteroid.goto(x, y)
            dx = 0
            #randint(-5, 5) / 20.0
            dy = randint(-2, -1) / 30.0 
            
            asteroid.dx = dx
            asteroid.dy = dy
            size = 2.0
            asteroid.size = size
            sprites.append(asteroid)
    
    sp_pen=turtle.Turtle()

    while True:
    # Update the screen
        update()  

        sp_pen.clear()
        sp_pen.hideturtle()
        sp_pen.penup()

        # Render and update
        for sprite in sprites:
            sprite.update()
            sprite.render(sp_pen)

        # delay=input("blah blah bitch")
        # pass