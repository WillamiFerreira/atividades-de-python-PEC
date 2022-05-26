import turtle
t = turtle.Turtle()
t.shape("turtle")
scr = turtle.Screen()
scr.bgcolor("MidnightBlue")
t.penup()

def planetdraw(size, color):
    t.color(color)
    t.pendown()
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()

planetdraw(50, "red")
t.forward(120)
planetdraw(60, "blue")
t.left(100)
t.forward(170)
planetdraw(40, "green")



t.done()
