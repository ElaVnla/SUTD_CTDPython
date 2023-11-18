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
from tkinter import font

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

# SCREEN LAYOUT ================================================================================================================

# SCREEN SETUP Screenuifunctions
# First thing to be called when main.py is run. This function will help setup the overall application
def Screen_Setup():
    screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
    # screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    #setup(900,500)
    # Title of the application. This will be displayed at the top left of the interface
    title("Keyboard Warriors: Adventure in SPACE(bar)")
    speed(0)

# Design for Home Screen ========================================================================================================

def Home_Screen():
    # Import the background image, to be displayed
    image = "Images/homescreenbackground.gif"
    
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)

    # Return the screen. Easier to clear when navigating to different pages
    return screen

# Function that creates the buttons in the homescreen
def Play_Button(ChangeTo_GamePlay,ChangeTo_Scoreboard,ChangeTo_Quit):
    canvas = turtle.getcanvas()
    parent = canvas.master
    #parent.geometry('500x500')

    # Creation of buttons and linking it to their respective functions (command=(function name) )
    myfont = font.Font(family='Arial', size=11, weight="normal")

    GamePlayButton = tk.Button(parent, text="Let's Play", fg='black', bg='light gray', command=ChangeTo_GamePlay, font=myfont)
    id1 = canvas.create_window((0,80), window=GamePlayButton)
    canvas.itemconfig(id1, width=180, height=40)
    GamePlayButton.update()

    ScoreboardButton = tk.Button(parent, text='Scoreboard', fg='black', bg='light gray', command=ChangeTo_Scoreboard, font=myfont)
    id2 = canvas.create_window((0,140), window=ScoreboardButton)
    canvas.itemconfig(id2, width=180, height=40)
    ScoreboardButton.update()

    QuitButton = tk.Button(parent, text='Leave', fg='black', bg='light gray', command=ChangeTo_Quit, font=myfont)
    id3 = canvas.create_window((0,200), window=QuitButton)
    canvas.itemconfig(id3, width=180, height=40)
    QuitButton.update()

# Design for Scoreboard Screen ======================================================================================================
def Scoreboard_Screen():
    # Import background image to be displayed
    image = "Images/scoreboard.gif"
    #screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)

    # Return the screen. Easier to clear when navigating to different pages
    return screen

# Function that helps display scores from the list given
def Display_Score(Sorted_Dict):
    # Variables
    stopat6 = 0
    position_yaxis = 60

    # Loop through the sorted list
    for users in Sorted_Dict:

        # Only display the top 6 players. Once 6 players have been displayed, break the loop
        if stopat6 == 6:
            break
        else:
            # Turtle Set up
            T = turtle.Pen()
            T.speed(0)
            T.hideturtle()
            T.up()
            T.color('White')

            # Write player name
            T.setposition(-150,position_yaxis)
            T.write(f'{users["PlayerName"]}',align='left', font=("Arial", 16, "bold", "italic"))

            # Write player's score
            T.setposition(80,position_yaxis)
            T.write(f'{users["Score"]}', align="left", font=("Arial", 16, "bold"))
            
            stopat6 += 1
            position_yaxis -= 40


# Function that creates the buttons in the homescreen
def Back_Button(GoBack):
    canvas = turtle.getcanvas()
    parent = canvas.master
    #parent.geometry('500x500')

    # Creation of buttons and linking it to their respective functions (command=(function name) )
    myfont = font.Font(family='Arial', size=11, weight="normal")
    BacktoHomeScreenButton = tk.Button(parent, text="Go back", fg='Black', bg='light grey', command=GoBack, font=myfont)
    id1 = canvas.create_window((0,190), window=BacktoHomeScreenButton)
    canvas.itemconfig(id1, width=180, height=40)
    BacktoHomeScreenButton.update()


# Design for Game Over Screen ====================================================================================================
def Gameover_Screen():
    # Import the background image, to be displayed
    image = "Images/gameover.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)

#  Design for Game Screen =======================================================================================================
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

