import turtle
a = turtle.Turtle()
x = turtle.Screen()
x.bgcolor("aqua")

#kotak
a = turtle.Turtle()
a.penup()
a.goto(-150, -100)
a.pendown()
a.pensize(2)
a.color("black", "orange")
a.begin_fill()
a.forward(300)
a.left(90)
a.forward(125)
a.left(90)
a.forward(300)
a.left(90)
a.forward(125)
a.end_fill()
a.left(90)
a.forward(300)
a.left(90)
a.forward(125)
a.left(90)
a.forward(300)
a.left(90)

#hiasan
Circle = 3
a.color("black", "yellow")
a.begin_fill()
a.circle(50, 180)
while Circle >=2:
    a.left(180)
    a.circle(50, 180)
    Circle = Circle - 1
a.end_fill()

#lilin
a.penup()
a.goto(-25, 50)
a.pendown()
a.pencolor("red")
a.pensize(10)
a.forward(70)
a.penup()
a.goto(0, 50)
a.pendown()
a.forward(70)
a.penup()
a.goto(25, 50)
a.pendown()
a.forward(70)

turtle.done()