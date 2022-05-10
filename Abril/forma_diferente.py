import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)
list = ['red', 'blue', 'green', 'orange'] 
t.pensize(4)

for n in range(36):
  t.forward(140)
  t.right(100)
  t.color(random.choice(list))
  
t.done()
#fiz uma modificaçao para mudar a a cor da caneta sempre que ela mudar de ângulo.