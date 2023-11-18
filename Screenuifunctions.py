# IMPORT Libraries
import functools
from functools import partial
from turtle import *
from random import *
import turtle
import tkinter as tk
from tkinter import messagebox
import time
import Class 

# TEXT Designs
CURSOR_SIZE = 20
FONT_SIZE = 32
FONT = ('Arial', FONT_SIZE, 'bold')
screen = turtle.Screen()
WIDTH, HEIGHT = 900, 500
USER_INPUT=[]
userInput=""

def justATestLMAO():
    print(userInput)
# SCREEN LAYOUT ======================================

# SCREEN SETUPScreenuifunctions
def Screen_Setup():
    screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
    # screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    title("Keyboard Warriors: Adventure in SPACE(bar)")
    speed(0)
    


# FUNCTIONS FOR BACKGROUND DESIGNS HERE ===============

# Design for Home Screen ====================================
def Home_Screen():
    image = "Images/homescreenbackground.gif"
    
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
    #screen = turtle.Screen()
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
    
    image = "Images/gamescreen.gif"
    
    #screen.addshape(image)
    screen.bgpic(image)
    screen.tracer(0)

    words= ["apple", "badge", "cloud", "drink", 
            "eleven", "fuzzy", "grape", "happy", "igloo", 
            "jolly", "kitty", "lemon", "magic", "ninja", 
            "ocean", "piano", "queen", "robot", "sunny", "tiger"]
    
    sprites=[]
    asteroids=[]
    player=Class.Player()
    ship=Class.Ship()
    missile=Class.Missile()
    difficulty=5
    sprites.append(player)
    sprites.append(ship)
    sprites.append(missile)

    
    
            
    
    sp_pen=turtle.Turtle()
    # delay=input(type(turtle.screensize()))
    turtle.penup()
    turtle.goto(WIDTH/2-300,-HEIGHT/2+50)
    turtle.hideturtle()
    screen.listen()
    
    screen._onkeypress = partial(_onkeypress, screen)
    screen.onkeypress(letter)
    screen.onkeypress(missile.fire, "space")
    screen.onkeypress(return_user_input, "space")
    screen.onkeypress(justATestLMAO, "w")
    
    
    

    while True:
    # Update the screen
        update()  
        bruh=randint(0,1000)
        sp_pen.clear()
        sp_pen.hideturtle()
        sp_pen.penup()
        if(len(asteroids)<difficulty):
            spawnSomeMotherFuckers(2,words,asteroids)
        
        # if

        # Render and update
        for sprite in sprites:
            sprite.update()
            sprite.render(sp_pen)
            # if isinstance(sprite, Class.Asteroid):
                

        for sprite in asteroids:
            sp_pen.goto(sprite.x, sprite.y)
            sp_pen.color("purple")
            sp_pen.write(f"{sprite.word}", False, font=("Courier New", 18, "normal"))
            sprite.update()
            sprite.render(sp_pen)
        # for sprite in sprites:
            
        # delay=input("blah blah")
        # pass


def spawnSomeMotherFuckers(difficultyTweak,words,sprites):
    for _ in range(difficultyTweak):
            asteroid = Class.Asteroid()
            # wordSpr=Class.Words()
            word=words[randint(0,len(words)-1)]
            x = randint(-WIDTH/2, WIDTH/2)
            y = HEIGHT/2
            asteroid.goto(x, y)
            
            dx = 0
            
            dy = randint(-10, -1) / 30.0 

            
            asteroid.dx = dx
            asteroid.dy = dy

            
            size = 2.0
            asteroid.size = size
            asteroid.word=word
            
            sprites.append(asteroid)
    

def _onkeypress(self, fun, key=None):
    if fun is None:
        if key is None:
            self.cv.unbind("<KeyPress>", None)
        else:
            self.cv.unbind("<KeyPress-%s>" % key, None)
    elif key is None:
        def eventfun(event):
            fun(event.char)
        self.cv.bind("<KeyPress>", eventfun)
    else:
        def eventfun(event):
            fun()
        self.cv.bind("<KeyPress-%s>" % key, eventfun)

def letter(character):
    if (character.isalpha()):
        turtle.write(character, move=True, font=FONT)
        USER_INPUT.append(character)
        # print(USER_INPUT)



def return_user_input():
    res=''
    userInput=res.join(USER_INPUT)
    USER_INPUT.clear()
    turtle.clear()
    turtle.goto(WIDTH/2-300,-HEIGHT/2+50)

