#membuat bolu
import turtle
turtle.Screen()
turtle.bgcolor("#00FFFF")
pen=turtle.Turtle()
pen.pensize(2)

#kotak
pen.penup()
pen.goto(-150,75)
pen.pendown()
pen.fillcolor("orange")
pen.begin_fill()
pen.forward(300)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.end_fill()
pen.penup()

def cream():
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(50,180)
    pen.end_fill()

def lilin():
    pen.pensize(5)
    pen.pencolor("red")
    pen.pendown()
    pen.forward(75)
    pen.penup()

#cream
pen.pendown()
pen.right(90)
cream()
pen.right(180)
cream()
pen.right(180)
cream()
pen.penup()

#lilin
pen.goto(-30,90)
lilin()
pen.goto(0,90)
lilin()
pen.goto(30,90)
lilin()

pen.hideturtle()
turtle.exitonclick()