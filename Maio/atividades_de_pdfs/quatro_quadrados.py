#Desenhando 4 quadrados com funções
import turtle
t = turtle.Turtle()
sce = turtle.Screen()
sce.bgcolor('MidnightBlue')
t.shape("turtle")
t.color("whiteSmoke")

def drawStar():
    t.pendown()
    t.begin_fill()
    for side in range(4):
        t.left(90)
        t.forward(50)
    t.end_fill()
    t.penup()


drawStar()
t.forward(100)
drawStar()
t.left(90)
t.forward(150)
drawStar()
t.left(90)
t.forward(150)
drawStar()
t.forward(100)

t.done()
