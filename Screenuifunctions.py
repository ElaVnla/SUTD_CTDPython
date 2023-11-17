# IMPORT Libraries
from turtle import *
from random import *
import turtle
import time

# TEXT Designs
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

# SCREEN LAYOUT ======================================

# SCREEN SETUP
def Screen_Setup():
    setup(900,500)
    title("Keyboard Warriors: Adventure in SPACE(bar)")
    Home_Screen()
    speed(0)


# FUNCTIONS FOR BACKGROUND DESIGNS HERE ===============

# Design for Home Screen
def Home_Screen():
    image = "Images/homescreenbackground.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)
    turtle.mainloop()
    while True:
        screen.update()
    

# Design for Scoreboard Screen
def Scoreboard_Screen():
    pass

# Design for Game Over Screen
def Gameover_Screen():
    pass

#  Design for Game Screen
def Gameplay_Screen():
    pass