import turtle

s = turtle.Screen()
b = 4
t = turtle.Turtle()
turtle.bgcolor("cyan")

# kotak
t.penup()
t.goto(-30 * b, -20 * b)
t.pendown()

t.fillcolor("orange")
t.begin_fill()
t.forward(60 * b)
t.right(90)
t.forward(40 * b)
t.right(90)
t.forward(60 * b)
t.right(90)
t.forward(40 * b)
t.end_fill()

# stenghlingkaran

for i in range(3):
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(180)
    t.circle(10 * b, 180)
    t.end_fill()
# lilin
t.penup()
t.width(10)
t.color("red")
t.goto(0, b)
t.pendown()
t.right(180)
t.forward(17 * b)
t.penup()
t.goto(b * 5, b)
t.pendown()
t.forward(17 * b)
t.penup()
t.goto(-5 * b, b)
t.pendown()
t.forward(17 * b)


s.exitonclick()
