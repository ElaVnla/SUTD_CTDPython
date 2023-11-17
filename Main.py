# IMPORT Libraries
from turtle import *
from random import *
import turtle
import time
import Screenuifunctions as Screenuifunctions # Import functions from the other .py file to be used them in this file

# Run screen setup
Screenuifunctions.Screen_Setup()

# First screen to pop up
Homescreen = Screenuifunctions.Home_Screen()

# Set up home screen buttons
def ChangeTo_GamePlay():
    Homescreen.clear()
    print("play button")
    Screenuifunctions.Gameplay_Screen()

def ChangeTo_Scoreboard():
    Homescreen.clear()
    print("Scoreboard button")
    Screenuifunctions.Scoreboard_Screen()

def ChangeTo_Quit():
    Homescreen.clear()
    print("Quit")
    turtle.bye()

Screenuifunctions.Play_Button(ChangeTo_GamePlay,ChangeTo_Scoreboard,ChangeTo_Quit)



# MUST ALWAYS BE AT THE LAST OF THE CODE !! CODE MUST NOT GO BEYOND THIS LINE!! ============================================
# To allow screen to stay and not close
turtle.mainloop() # This will run the above results
turtle.done() #Program will end when user clicks on the exit button on top right
