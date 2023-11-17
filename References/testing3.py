import turtle
import colorsys

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.speed(0)
turtle.delay(0)

t.hideturtle()
t.pensize(10)
t.goto(0,100)

while True:
    for i in range(120):
        t.color(colorsys.hls_to_rgb(i/130,i/130,1))
        t.forward(20)
        t.right(6)

        if i%2==0:
            t.penup()
        else:
            t.pendown()


# MUST ALWAYS BE AT THE LAST OF THE CODE !! CODE MUST NOT GO BEYOND THIS LINE!!
# To allow screen to stay and not close
turtle.done() #Program will end when user clicks on the exit button on top right