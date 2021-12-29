import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("cyan")
t.hideturtle()

# base
t.fillcolor("orange")
t.begin_fill()
t.seth(180)
t.forward(45)
t.right(90)
t.forward(45)
t.right(90)
t.forward(90)
t.right(90)
t.forward(45)
t.right(90)
t.forward(45)
t.end_fill()
t.up()

# 3 bunderan
t.goto(-45, 45)
t.seth(270)
t.down()

t.fillcolor("yellow")
x = -45
for i in range(3):
    t.goto(x, 45)
    t.seth(270)
    t.begin_fill()
    t.circle(15, 180)
    t.end_fill()
    x += 30
t.up()

# lilin
t.goto(0, 55)
t.width(4)
t.pencolor("red")

t.seth(90)
t.down()
t.forward(25)
t.up()

t.goto(-10, 55)
t.down()
t.forward(25)
t.up()

t.goto(10, 55)
t.down()
t.forward(25)


s.exitonclick()
