# IMPORT Libraries
from turtle import *
from random import *
import turtle
import time
import Screenuifunctions as Screenuifunctions # Import functions from the other .py file to be used them in this file

# Set up Screen ===================================================================================================
screen = turtle.Screen()
screen.setup(width=1.0, 
             height=1.0)

# Run screen setup
Screenuifunctions.Screen_Setup()

# First screen to pop up
Homescreen = Screenuifunctions.Home_Screen()
global NewHomescreen

# Set up home screen buttons =====================================================================================

# If player clicks Gameplay, will navigate to this function
def ChangeTo_GamePlay():
    # Clear everything on the screen to display a new screen
    Homescreen.clear()
    print("play button")
    Screenuifunctions.Gameplay_Screen()
    

# If player clicks scoreboard, will navigate to this function
def ChangeTo_Scoreboard():
    Homescreen.clear()
    print("Scoreboard button")
    NewHomescreen = Screenuifunctions.Scoreboard_Screen()

    # Pass in the Score list and display the results in order
    # Display the top 6 results
    Players_Score_Dict = [{'PlayerName': 'Erika', 'Score':20}, 
                          {'PlayerName':'Joey','Score': 30}, 
                          {'PlayerName':'Ryan','Score': 100}, 
                          {'PlayerName':'Erika','Score': 0}, 
                          {'PlayerName': 'Angie', 'Score': 50}, 
                          {'PlayerName': "Jered", 'Score': 60}, 
                          {'PlayerName': "Drea", 'Score': 80}]
    Sorted_Dict = sorted(Players_Score_Dict, 
                         key=lambda d: d['Score'], 
                         reverse=True) 
    # Print results in terminal to check if sorted_dict was sorted right
    print(Sorted_Dict)

    # Pass to display score function to display scores
    Screenuifunctions.Display_Score(Sorted_Dict)

    # If player clicks back, will navigate back to homepage
    def GoBack():
        NewHomescreen.clear()
        print("Go back")
        Screenuifunctions.Home_Screen()

        # Must add this code again or the homescreen won't display the buttons
        # Display the 3 buttons
        Screenuifunctions.Play_Button(ChangeTo_GamePlay,
                                      ChangeTo_Scoreboard,
                                      ChangeTo_Quit)

    # Display the back button
    Screenuifunctions.Back_Button(GoBack)

# If player clicks on leave, will navigate to this function
def ChangeTo_Quit():
    Homescreen.clear()
    print("Quit")
    turtle.bye()

# Display the 3 buttons
Screenuifunctions.Play_Button(ChangeTo_GamePlay,
                              ChangeTo_Scoreboard,
                              ChangeTo_Quit)

# MUST ALWAYS BE AT THE LAST OF THE CODE !! CODE MUST NOT GO BEYOND THIS LINE!! ============================================
# To allow screen to stay and not close
turtle.mainloop() # This will run the above results
turtle.done() #Program will end when user clicks on the exit button on top right

