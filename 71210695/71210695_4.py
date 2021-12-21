# Program 4
import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("cyan")

t.penup()
t.goto(-150, -100)
t.pendown()
t.pensize(2)
t.color("black", "orange")
t.begin_fill()

# Kotak Kue
for i in range(3):
    t.fd(300)
    t.left(90)
    t.fd(140)
    t.left(90)


t.end_fill()
t.fd(300)
t.left(90)

# Hiasan Melengkung
t.color("black", "yellow")
t.begin_fill()
t.circle(50, 180)
for i in range(2):
    t.left(180)
    t.circle(50, 180)
t.end_fill()

# Lilin
def lilin(x, y):
    t.color("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(49)
        t.left(90)
        t.forward(4)
        t.left(90)
    t.end_fill()


lilin(30, 45)
lilin(2, 45)
lilin(-26, 45)

t.end_fill()
turtle.done()


s.exitonclick()
