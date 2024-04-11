import turtle

t = turtle.Turtle()

t.penup()
t.goto(-50, 50) 

t.pendown()
t.write("D", align="center", font=("Arial", 24, "normal"))

t.penup()
t.goto(-50, 0)  
t.pendown()
t.write("N", align="center", font=("Arial", 24, "normal"))

t.penup()
t.goto(-50, -50)  
t.pendown()
t.write("T", align="center", font=("Arial", 24, "normal"))

t.hideturtle()
turtle.done()
