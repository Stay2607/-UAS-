import turtle

s = turtle.Screen()
turtle.Screen().bgcolor("cyan")

square = turtle.Turtle()
square.penup()
square.goto(-150, -100)
square.pendown()
square.pensize(2)
square.speed("normal")
square.color("black", "orange")
square.begin_fill()
for i in range(3):
    square.forward(300)
    square.left(90)
    square.forward(125)
    square.left(90)

square.end_fill()
square.forward(300)
square.left(90)

square.color("black", "yellow")
square.begin_fill()
square.circle(50, 180)
for i in range(2):
    square.left(180)
    square.circle(50, 180)
square.end_fill()

# lilin
square.penup()
square.goto(-20, 100)
square.pencolor("red")
square.pensize(5)
square.pendown()
square.right(180)
square.forward(50)
square.penup()
square.goto(0, 100)
square.pencolor("red")
square.pensize(5)
square.pendown()
square.forward(50)
square.penup()
square.goto(20, 100)
square.pencolor("red")
square.pensize(5)
square.pendown()
square.forward(50)

s.exitonclick()
