import turtle
n=int(input())
a=0
while a<=n:
  turtle.forward(90)
  turtle.backward(90)
  turtle.left(360/n)
  a=a+1
