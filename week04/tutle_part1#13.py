import turtle
a=0
turtle.pensize(3)
turtle.circle(75)
turtle.penup()
turtle.goto(-30,90)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(30,90)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(-40,60)
turtle.pendown()
a=0
turtle.right(90)
while a<130:
  turtle.forward(1)
  turtle.left(1.5)
  a=a+1
