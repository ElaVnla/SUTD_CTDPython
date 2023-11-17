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

# Design for Home Screen ====================================
def Home_Screen():
    image = "Images/homescreenbackground.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)
    #Create_Button()

    # This should be the last line! Write your codes above this line!!!
    turtle.mainloop() # This will run the above results

def Create_Button():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pencolor('#111111')
    pen.fillcolor('white')

    ButtonXAxis = -30
    ButtonYAxis = -30
    ButtonLength = 100
    ButtonWidth = 50

    mode = 'dark'


    def draw_rect_button(pen, message = 'Play'):
        pen.penup()
        pen.begin_fill()
        pen.goto(ButtonXAxis, ButtonYAxis)
        pen.goto(ButtonXAxis + ButtonLength, ButtonYAxis)
        pen.goto(ButtonXAxis + ButtonLength, ButtonYAxis + ButtonWidth)
        pen.goto(ButtonXAxis, ButtonYAxis + ButtonWidth)
        pen.goto(ButtonXAxis, ButtonYAxis)
        pen.end_fill()
        pen.goto(ButtonXAxis + 15, ButtonYAxis + 15)
        pen.write(message, font = ('Arial', 15, 'normal'))


    draw_rect_button(pen)

# Design for Scoreboard Screen ===========================================
def Scoreboard_Screen():
    pass

# Design for Game Over Screen ============================================
def Gameover_Screen():
    pass

#  Design for Game Screen ===============================================
def Gameplay_Screen():
    pass