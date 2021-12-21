import turtle

s = turtle.Screen()
s.bgcolor("skyblue")
t = turtle.Turtle()
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

# lilin
def lilin(x, y):
    t.color("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(6)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.end_fill()

        t.color("red")
        t.begin_fill()
        for i in range(2):
            t.forward(6)
            t.right(90)
            t.forward(10)
            t.right(90)
            t.end_fill()
