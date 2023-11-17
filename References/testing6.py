import turtle

# Global variable to track turtle visibility
turtle_visible = True

def show_turtle():
    global turtle_visible
    turtle.showturtle()
    turtle_visible = True

def hide_turtle():
    global turtle_visible
    turtle.hideturtle()
    turtle_visible = False

def toggle_turtle():
    if turtle_visible:
        hide_turtle()
    else:
        show_turtle()

def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

# Example usage
draw_square()  # Turtle is visible by default

# Hide turtle from outside the function
hide_turtle()

# Show turtle from outside the function
show_turtle()

# Toggle turtle visibility from outside the function
toggle_turtle()

# Draw another square with the turtle hidden
draw_square()

# Close the turtle graphics window
turtle.done()