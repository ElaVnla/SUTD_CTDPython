from turtle import Screen, Turtle
from random import randint

FONT_STYLE = ('Courier', 30, 'italic')

screen = Screen()
screen.title("My game by python code")
screen.bgcolor('black')
screen.setup(width=600, height=600)

# Making the user 'bubble'
bubble = Turtle()
bubble.color('red')
bubble.shape('circle')
bubble.penup()

# Making the collection balls
collection_ball = Turtle()
collection_ball.color('yellow')
collection_ball.shape('circle')
collection_ball.shapesize(0.5)
collection_ball.penup()
ball_cor1 = randint(30, 280)
ball_cor2 = randint(30, 280)
collection_ball.setposition(ball_cor1, ball_cor2)

# Scoring
score = 0
speed = 3

points = Turtle()
points.hideturtle()
points.color('yellow')
points.penup()
points.goto(-200, 250)
points.write("Points: 0", font=FONT_STYLE)

# Turning
def turn_left():
    bubble.left(90)

def turn_right():
    bubble.right(90)

# Collection of the balls
def was_collected(bubble):
    return bubble.distance(collection_ball) < 15

def collection_ball_reset():
    collection_ball.hideturtle()
    collection_ball.goto(randint(30, 280), randint(30, 280))
    collection_ball.showturtle()

def play_game():
    global score

    if was_collected(bubble):
        score += 2
        points.clear()
        points.write("Points: " + str(score), font=FONT_STYLE)
        collection_ball_reset()

    bubble.forward(speed)
    screen.ontimer(play_game, 10)

screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_right, 'Right')
screen.listen()

play_game()

screen.mainloop()