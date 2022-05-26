import turtle
import random

t = turtle.Turtle()
sky = turtle.Screen()
sky.bgcolor("MidnightBlue")
t.shape("turtle")

def lugaraleatorio():
    t.penup()
    t.setpos(randint(-400, 400), randint(-400, 400))
    t.pendown()

def drawstar(size, color):
    color(color)
    t.pendonw()
    t.begin_fill()
    for side in range(5):
        t.left(144)
        t.forward(size)
    t.end_fill()
    t.penup()

for star in range(30):
    lugaraleatorio()
    drawstar(randit(5, 25), "White")

t.done()



