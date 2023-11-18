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

# SCREEN LAYOUT ================================================================================================================

# SCREEN SETUP Screenuifunctions
# First thing to be called when main.py is run. This function will help setup the overall application
def Screen_Setup():
    #setup(900,500)
    # Title of the application. This will be displayed at the top left of the interface
    title("Keyboard Warriors: Adventure in SPACE(bar)")
    speed(0)

# Design for Home Screen ========================================================================================================

def Home_Screen():
    # Import the background image, to be displayed
    image = "Images/homescreenbackground.gif"
    screen = turtle.Screen()
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
    GamePlayButton = tk.Button(parent, text="Let's Play", fg='black', bg='light gray', command=ChangeTo_GamePlay)
    id1 = canvas.create_window((0,40), window=GamePlayButton)
    canvas.itemconfig(id1, width=200, height=40)
    GamePlayButton.update()

    ScoreboardButton = tk.Button(parent, text='Scoreboard', fg='black', bg='light gray', command=ChangeTo_Scoreboard)
    id2 = canvas.create_window((0,100), window=ScoreboardButton)
    canvas.itemconfig(id2, width=200, height=40)
    ScoreboardButton.update()

    QuitButton = tk.Button(parent, text='Leave', fg='black', bg='light gray', command=ChangeTo_Quit)
    id3 = canvas.create_window((0,160), window=QuitButton)
    canvas.itemconfig(id3, width=200, height=40)
    QuitButton.update()

# Design for Scoreboard Screen ======================================================================================================
def Scoreboard_Screen():
    # Import background image to be displayed
    image = "Images/scoreboard.gif"
    screen = turtle.Screen()
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
    BacktoHomeScreenButton = tk.Button(parent, text="Go back", fg='Black', bg='light grey', command=GoBack)
    id1 = canvas.create_window((0,190), window=BacktoHomeScreenButton)
    canvas.itemconfig(id1, width=200, height=40)
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