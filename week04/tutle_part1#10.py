import turtle

turtle.penup()
turtle.goto(0, 45)
turtle.pendown()
turtle.circle(45)
turtle.penup()
turtle.goto(0, -45)
turtle.pendown()
turtle.circle(45)
turtle.penup()
turtle.goto(45*0.866,45/2)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(45*0.866,-45/2)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(-45*0.866,45/2)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(-45*0.866,-45/2)
turtle.pendown()
turtle.circle(45)