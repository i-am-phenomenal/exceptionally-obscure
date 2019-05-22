import turtle

shouldNotExit = True

window = turtle.Screen()
window.title("Cricket")
window.bgcolor("green")
window.setup(800, 600)
window.tracer()

pitch = turtle.Turtle()
pitch.speed(0)
pitch.color("white")
pitch.shape("square")
pitch.penup()
pitch.shapesize(13, 3)
pitch.goto(0, 0)


ball = turtle.Turtle()
ball.penup()
ball.speed(0)
ball.color("red")
ball.shape("circle")
ball.shapesize(0.8, 0.8)
ball.goto(0, -130)
ball.dx = 3
ball.dy = 3

leftStump = turtle.Turtle()
leftStump.speed(0)
leftStump.color("black")
leftStump.penup()
leftStump.goto(-5, 150)
leftStump.shape("square")
leftStump.shapesize(1.5, 0.1)

middleStump = turtle.Turtle()
middleStump.speed(0)
middleStump.color("black")
middleStump.penup()
middleStump.goto(0, 150)
middleStump.shape("square")
middleStump.shapesize(1.5, 0.1)


rightStump = turtle.Turtle()
rightStump.speed(0)
rightStump.color("black")
rightStump.penup()
rightStump.goto(5, 150)
rightStump.shape("square")
rightStump.shapesize(1.5, 0.1)


#Functions
def throw_ball():
    while ball.ycor() <= 150: 
        ball.sety(ball.ycor() + 2)
    ball.goto(0, -130)
    
window.listen()
window.onkey(throw_ball, "Up")

while shouldNotExit:
    window.update()