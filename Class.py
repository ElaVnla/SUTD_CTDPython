import turtle
import math
import random
import Screenuifunctions as Screenuifunctions # Import functions from the other .py file to be used them in this file
WIDTH, HEIGHT = 900, 500
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()


class Sprite:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "white"
        self.size = 1.0
        self.active = True
        
    def update(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy

        
    def render(self, pen):
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.stamp()
            
    # def is_collision(self, other):
    #     x = self.x-other.x
    #     y = self.y-other.y
    #     distance = ((x**2) + (y**2)) ** 0.5
    #     if distance < ((10 * self.size) + (10 * other.size)):
    #         return True
    #     else:
    #         return False
            
    def goto(self, x, y):
        self.x = x
        self.y = y


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.lives = 3
        self.score = 0
        self.x = 0
        self.y = -HEIGHT/2
        self.heading = 90
        self.size=2.5
        self.shape = "triangle"
        self.color = "yellow"
    #def rotate_left(self):
    #    self.heading += 30
        
    #def rotate_right(self):
    #    self.heading -= 30
        
    def accelerate(self):
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.1
        self.dy += ay * 0.1
        
    def render(self, pen):
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size/2.0, self.size, 0)
            pen.color(self.color)
            pen.stamp()


class Ship(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x = 0
        self.y = -300
        self.size = 1.5
        self.shape = "square"
        self.color = "gray"

class Asteroid(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "circle"
        self.color= "gray"
        self.word=""

# class Words(Sprite):
#     def __init__(self):
#         Sprite.__init__(self)
#         #self.shape = "circle"
#         #self.color= "gray"   
#         # 
#     def render(self, pen):
#         if self.active:
#             pen.goto(self.x, self.y)
#             pen.write(f"test", False, font=("Courier New", 18, "normal"))
#             #pen.setheading(self.heading)
#             #pen.shape(self.shape)
#             #pen.shapesize(self.size/2.0, self.size, 0)
#             #pen.color(self.color)
#             #pen.stamp()     

class Missile(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.shape = "square"
        self.color="orange"
        self.size = 0.5
        self.active = False
        

    def update(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy
            
            # if self.x > WIDTH/2:
            #     self.active = False
            # elif self.x < -(WIDTH/2):
            #     self.active = False
                
            if self.y > HEIGHT/2:
                self.active = False
            elif self.y < -(HEIGHT/2):
                self.active = False
        
    def fire(self):
        if not self.active:
            self.active = True
            self.x = 0
            self.y = -HEIGHT/2
            self.heading = 90
            self.dx = math.cos(math.radians(self.heading)) * 1
            self.dy = math.sin(math.radians(self.heading)) * 1

