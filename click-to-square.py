# CHALLENGE: create a program that draws a randomly colored square in the spot the user clicks on the screen
# Add Python libraries and set up
import turtle  
from turtle import *
import random

screen = turtle.Screen()
jimmy = Turtle()
jimmy.speed(0)

def myFunction(x, y):
    jimmy.penup()
    jimmy.setheading(jimmy.towards(x, y))
    jimmy.goto(x, y)
    length = random.randint(10, 100)
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    jimmy.fillcolor(r,g,b)
    jimmy.begin_fill()
    for x in range(4):
      jimmy.color(r,g,b)
      jimmy.pendown()
      jimmy.forward(length)
      jimmy.left(90)
    jimmy.end_fill()

screen.onscreenclick(myFunction)

