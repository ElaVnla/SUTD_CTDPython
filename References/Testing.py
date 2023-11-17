from turtle import *
from random import *
import turtle
import time

#SCREEN SETUP
setup(800, 500) # Size of screen
title("Turtle Race") # Title of Game , will be shown on the top left bar of the screen
bgcolor("forestgreen")
speed(0)


# HEADING
penup() # will lift the turtle off the "Digital canvas" and if you move the turtle in penup state it won't draw
goto(-100, 205)
color("white")
write("TURTLE RACE", font=("Arial", 20, "bold"))

# DIRT
goto(-350, 200)
pendown() # Default state of turtle. It will ensure the turtle draws when it's moving with your commands
color("Chocolate")
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
gap_size = 20
shape("square")
penup()

# WHITE SQAURES ROW 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQAURES ROW 2
color("white")
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# BLACK SQAURES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK SQAURES ROW 2
color("black")
for i in range(10):
    goto(250 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()

# TURTLE 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()

# TURTLE 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()

# TURTLE 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("magenta")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()

# TURTLE 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()

time.sleep(1) # pause the game for 1 second before starting the race

# MOVE THE TURTLES
for i in range(145):
    turtle1.forward(randint(1,8)) # number 8, the higher number, the longer they travel. 
    #if you put 5 it will only start 3/4 of the path, it won't cross the finishing line
    turtle2.forward(randint(1,8))
    turtle3.forward(randint(1,8))
    turtle4.forward(randint(1,8))

# MUST ALWAYS BE AT THE LAST OF THE CODE !! CODE MUST NOT GO BEYOND THIS LINE!!
# To allow screen to stay and not close
turtle.done() #Program will end when user clicks on the exit button on top right