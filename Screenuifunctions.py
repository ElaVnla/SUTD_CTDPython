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
import requests
from tkinter import font

# TEXT Designs
CURSOR_SIZE = 20
FONT_SIZE = 32
FONT = ('Arial', 
        FONT_SIZE, 
        'bold')
screen = turtle.Screen()
WIDTH, HEIGHT = 900, 500
USER_INPUT=[]
userInput=""

# SCREEN LAYOUT ================================================================================================================

# SCREEN SETUP Screenuifunctions
# First thing to be called when main.py is run. This function will help setup the overall application
def Screen_Setup():
    screen.setup(WIDTH + 4, 
                 HEIGHT + 8)  # fudge factors due to window borders & title bar
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

    # Button for Gameplay
    GamePlayButton = tk.Button(parent, text="Let's Play", fg='black', bg='light gray', command=ChangeTo_GamePlay, font=myfont)
    id1 = canvas.create_window((0,80), window=GamePlayButton)
    canvas.itemconfig(id1, width=180, height=40)
    GamePlayButton.update()

    # Button for Scoreboard
    ScoreboardButton = tk.Button(parent, text='Scoreboard', fg='black', bg='light gray', command=ChangeTo_Scoreboard, font=myfont)
    id2 = canvas.create_window((0,140), window=ScoreboardButton)
    canvas.itemconfig(id2, width=180, height=40)
    ScoreboardButton.update()

    # Button for Quit
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
def Gameover_Screen(score):
    # Import the background image, to be displayed
    image = "Images/gameover.gif"
    screen = turtle.Screen()
    #screen.addshape(image)
    screen.bgpic(image)
    screen.register_shape(image)
    turtle.shape(image)

    # Ask player to input their playername to be stored and display on the scoreboard
    player_name=screen.textinput("Enter your name", "SCORE: " + str(score))
    # print(player_name)
    PLAYER_SCORE_DICT={"PlayerName":player_name,"Score": score}

    # Return the player's dictionary and the current active screen
    return PLAYER_SCORE_DICT, screen

#  Design for Game Screen =======================================================================================================
def GetWords():
    # Instead of making a List full of words, to save time we use a wordlist that comprises of 10000 words for us to choose from
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    # print(WORDS)

    # We only want specific words that has specific number of characters. This is needed to not overwhelmed the screen with too long words
    # and for display purpose
    newlist = []
    for words in WORDS:
        if len(words) <= 6 and len(words) >= 4:
            # Words are given in utf-8 format, thus we need to decode it to get it to a string
            bruh = words.decode("utf-8")
            newlist.append(bruh)
    
    return newlist
def Gameplay_Screen():
    # Variables
    gameoveractivate = False
    
    #Background image to be displayed
    image = "Images/gamescreen.gif"
    
    #screen.addshape(image)
    screen.bgpic(image)
    screen.tracer(0)

    # words= ["apple", "badge", "cloud", "drink", 
    #         "eleven", "fuzzy", "grape", "happy", "igloo", 
    #         "jolly", "kitty", "lemon", "magic", "ninja", 
    #         "ocean", "piano", "queen", "robot", "sunny", "tiger", ]

    words = GetWords()
    
    # list of sprites to animate, asteroids will be separate list
    sprites=[]
    asteroids=[]

    # player, ship, and missile instances
    player=Class.Player()
    ship=Class.Ship()
    missile=Class.Missile()

    # experimental difficulty 
    difficulty = 3
    
    # add player, ship, and missile into list of sprites to animate
    sprites.append(player)
    sprites.append(ship)
    sprites.append(missile)

    # declare variable just for animation of sprites
    sp_pen=turtle.Turtle()
    
    turtle.penup()
    turtle.goto(WIDTH/2-300,-HEIGHT/2+50)
    turtle.hideturtle()

    score_pen = turtle.Turtle()
    score_pen.color("white")
    score_pen.goto(WIDTH/2-200,HEIGHT/2-50)
    # turtle screen listen for user input on keyboard
    # this specifically will print out the letters typed by the player live on the screen
    screen.listen()
    screen._onkeypress = partial(_onkeypress, screen)
    screen.onkeypress(letter)
    
    # main game while loop, enables animation update and render to run continuously
    while gameoveractivate==False:
    # Update the screen
        update()  

        # clear all, if any, previous drawings by the turtle pen
        sp_pen.clear()
        # hide the turtle pen
        sp_pen.hideturtle()
        # turtle won't draw continuous lines
        sp_pen.penup()

        for i in range(player.lives):
            sp_pen.goto(-WIDTH/2 +20 + 30 * i, HEIGHT/2-50)
            sp_pen.shape("triangle")
            sp_pen.color("red")
            sp_pen.shapesize(0.9, 0.9, 0)
            sp_pen.setheading(90)
            sp_pen.stamp()

        # if there are less than certain number of asteroids, continue spawning for player to play
        while(len(asteroids)<difficulty):
            asteroidSpawn(difficulty,words,asteroids)
        
        # render and update
        for sprite in sprites:
            sprite.update() 
            sprite.render(sp_pen)
                           
        # attach a word from the list of words to appear below the asteroid    
        for sprite in asteroids:
            
            sp_pen.goto(sprite.x-10*sprite.size, sprite.y-20*sprite.size-10)
            sp_pen.color("white")
            sp_pen.write(f"{sprite.word}", False, font=("Courier New", 18, "normal"))
            sprite.update()
            sprite.render(sp_pen)
            if sprite.y < -(HEIGHT/2):
                asteroids.remove(sprite)
                player.lives-=1
                print(f"Lives: {player.lives}")
                if player.lives <= 0:
                    print("PLAYER DIES")
                    player.active = False
                    gameoveractivate = True
                    break

        # get user input via series of functions, when player presses "space", if word exists, asteroid is destroyed
        screen.onkeypress(partial(return_user_input, missile, asteroids, player), "space")
        # screen.onkeypress(partial(return_user_input, missile, asteroids, player), "return")
        # delay=input("blah blah")
        # pass
        score_pen.clear()
        score_pen.write(player.score,False, font=FONT)
        
        # difficulty increases when the points increases
        for i in range (1,20):
            if  player.score == i*100:
                difficulty = i + 3
                # print(difficulty)
    
    return gameoveractivate, screen, player.score

# function for spawning asteroids to be put into while loop
def asteroidSpawn(difficultyTweak,words,sprites): # args influence number of asteroids to spawn, what words to use, and the list of asteroid objects
    for _ in range(difficultyTweak):
            # create asteroid instance
            k=_
            # print(k)
            if(k>2):
                k=0
            asteroid = Class.Asteroid()
            
            # choose a random word to be attached to asteroid instance
            word=words[randint(0,len(words)-1)]

            # randomly spawn asteroid slightly above the top of the screen 
            x = (k+1)*122.5*choice([-1,1])
            y = HEIGHT/2+(k+1)*70
            # print(x,y)

            
            # if there are already asteroids in the list
            # if(len(sprites)!=0):
            #     for k in sprites:
            #         # if asteroid spawns within collision of existing asteroid, do not spawn the asteroid
            #         if (asteroid.x-k.x>):
            #             break
            #         # if there is already an asteroid with randomly assigned word, generate a new word
            #         if (k.word==word):
            #             word=words[randint(0,len(words)-1)]
            #         # spawn the asteroid
            #         else:
            #             asteroid.goto(x, y)
            # # spawn the asteroid
            # else:
            asteroid.goto(x, y)
            if (len(sprites)>0):
                for a in sprites:
                    if asteroid.is_collision(a):
                        sprites.remove(a)
                        print("collide!")
            # asteroid movement variable, can be adjusted according to the difficulty level
            dx = 0
            dy = randint(-difficultyTweak, -difficultyTweak+2) / 25.0            
            asteroid.dx = dx
            asteroid.dy = dy
        
            size = randint(2,4)
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
        character=character.lower()
        turtle.color('white')
        turtle.write(character, move=True, font=FONT)
        USER_INPUT.append(character)
        # print(USER_INPUT)

def return_user_input(missile, asteroids, player):
    res=''
    userInput=res.join(USER_INPUT)
    USER_INPUT.clear()
    turtle.clear()
    turtle.goto(WIDTH/2-300,-HEIGHT/2+50)
    # print(userInput)

    for a in asteroids:
        # print(a.word, asteroids.index(a))
        if (a.word==userInput):
            missile.fire(a)
            asteroids.remove(asteroids[asteroids.index(a)])
            player.score += 10
        #    asteroids.remove(asteroids.index(userInput))
        
    # return userInput

