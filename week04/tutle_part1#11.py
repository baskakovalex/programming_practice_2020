import turtle
a=0
b=0
l=1
u=1
while a<10:
  while b<=360:
    turtle.forward(l)
    turtle.left(u)
    b=b+1
  b=0
  while b<=360:
    turtle.forward(l)
    turtle.right(u)
    b=b+1
  b=0
  u=u+1
  l=+1
  a=a+1
