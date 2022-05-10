import turtle
lados = 4 # esse número pode ser mudado para qualquer outro, podendo ser feito qualquer polígono.
angulos = 360 / lados
t = turtle.Turtle()
for n in range(lados):
  t.forward(100)
  t.right(angulos)
t.done()