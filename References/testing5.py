from turtle import Screen, Turtle

def click(x, y):
    button.hideturtle()
    button.write("Thank you!", align='center', font=('Arial', 18, 'bold'))

screen = Screen()

button = Turtle()
button.shape('square')
button.shapesize(2, 4)
button.fillcolor('gray')
button.onclick(click)

screen.mainloop()