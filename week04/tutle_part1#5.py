import turtle
a=1
l=20
while a<=10:
  turtle.down()
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  turtle.left(90)
  turtle.forward(l)
  a=a+1
  turtle.up()
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(10)
  turtle.right(180)
  l=l+20
