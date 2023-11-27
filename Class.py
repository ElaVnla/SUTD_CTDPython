# Import Libraries
import turtle
import math
import random
import Screenuifunctions as Screenuifunctions # Import functions from the other .py file to be used them in this file
WIDTH, HEIGHT = 900, 500
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()


# Sprite superclass
class Sprite:
    def __init__(self):
        #Sprite superclass attributes
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
        #Sprite superclass animation update  
        if self.active:
            self.x += self.dx
            self.y += self.dy

    def render(self, pen):
        #Sprite superclass render sprite
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size, self.size, 0)
            pen.color(self.color)
            pen.stamp()
            
    def is_collision(self, other):
        #Sprite superclass collision check
        x = self.x-other.x
        y = self.y-other.y
        distance = ((x**2) + (y**2)) ** 0.5
        if distance < ((10 * self.size) + (10 * other.size)):
            return True
        else:
            return False
            
    def goto(self, x, y):
        #Sprite location set
        self.x = x
        self.y = y

#Player subclass of Sprite
class Player(Sprite):
    def __init__(self):
        #Player attributes
        Sprite.__init__(self)
        self.lives = 3
        self.score = 0
        self.x = 0
        self.y = -HEIGHT/2+50
        self.heading = 90
        self.size=2
        self.shape = "triangle"
        self.color = "yellow"
      
    def render(self, pen):
        #Player render 
        if self.active:
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.shapesize(self.size/2.0, self.size, 0)
            pen.color(self.color)
            pen.stamp()

#Ship subclass of Sprite
class Ship(Sprite):
    def __init__(self):
        #Ship attributes
        Sprite.__init__(self)
        self.x = 0
        self.y = -300
        self.size = 1.5
        self.shape = "square"
        self.color = "gray"

#Asteroid subclass of Sprite
class Asteroid(Sprite):
    def __init__(self):
        #Asteroid attributes
        Sprite.__init__(self)
        self.shape = "circle"
        self.color= "gray"
        self.word=""

#Missile subclass of Sprite
class Missile(Sprite):
    def __init__(self):
        #Missile attributes
        Sprite.__init__(self)
        self.shape = "square"
        self.color="orange"
        self.size = 0.5
        self.active = False
        
    def update(self):
        #Missile animation update
        if self.active:
            self.x += self.dx
            self.y += self.dy
            
            #if out of bounds, missile will despawn
            if self.x > WIDTH/2:
                self.active = False
            elif self.x < -(WIDTH/2):
                self.active = False
                
            if self.y > HEIGHT/2:
                self.active = False
            elif self.y < -(HEIGHT/2):
                self.active = False
        
    def fire(self, asteroid):
        #Missile firing function
        print("FIRE")
        if not self.active:
            tta=0 #angle
            self.active = True
            self.x = 0
            self.y = -HEIGHT/2+50
            self.heading = 90
            deltay = asteroid.y - self.y
            deltax = asteroid.x - self.x

            if deltax == 0:
                tta= math.pi()
            else:
                tta= math.atan2(deltay, deltax) #get angle of asteroid wrt missile start pos 

            self.dx = math.cos(tta) *15
            self.dy = math.sin(tta) *15

        #Missile despawn if collide with asteroid
        if (self.is_collision(asteroid)):
            self.active=False



