import turtle
import time
import random
import winsound
from playsound import playsound
from threading import Thread

firstUserScore = 0
secondUserScore = 0
shouldNotExit = True

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer()

leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.color("white")
leftPaddle.shape("square")
leftPaddle.shapesize(4, 1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)
leftPaddle.direction = "stop"

rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.color("white")
rightPaddle.penup()
rightPaddle.goto(350, 0)
rightPaddle.shape("square")
rightPaddle.shapesize(4, 1)
rightPaddle.direction = "stop"

ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shape("square")
ball.direction = "stop"
ball.dx = 5
ball.dy = 5

firstScoreArea = turtle.Turtle()
firstScoreArea.speed(0)
firstScoreArea.color("white")
firstScoreArea.penup()
firstScoreArea.hideturtle()
firstScoreArea.goto(-70, 260)
firstScoreArea.write("Player A: 0", align="right", font=("Courier", 24, "normal"))

secondScoreArea = turtle.Turtle()
secondScoreArea.speed(0)
secondScoreArea.color("white")
secondScoreArea.penup()
secondScoreArea.hideturtle()
secondScoreArea.goto(70, 260)
secondScoreArea.write("Player B: 0", align="left", font=("Courier", 24, "normal"))


# Functions
def move_right_paddle_up():
    yCoordinate = rightPaddle.ycor()
    rightPaddle.direction = "up"
    rightPaddle.sety(yCoordinate + 8)

    if rightPaddle.ycor() >= 250:
        rightPaddle.sety(250)


def move_right_paddle_down():
    yCoordinate = rightPaddle.ycor()
    rightPaddle.direction = "down"
    rightPaddle.sety(yCoordinate - 8)

    if rightPaddle.ycor() <= -250:
        rightPaddle.sety(-250)


def move_left_paddle_up():
    xCoordinate = leftPaddle.ycor()
    leftPaddle.direction = "up"
    leftPaddle.sety(xCoordinate + 8)

    if leftPaddle.ycor() >= 250:
        leftPaddle.sety(250)


def move_left_paddle_down():
    xCoordinate = leftPaddle.ycor()
    leftPaddle.direction = "down"
    leftPaddle.sety(xCoordinate - 8)

    if leftPaddle.ycor() <= -250:
        leftPaddle.sety(-250)


def exit_game():
    global shouldNotExit
    if shouldNotExit == True:
        shouldNotExit = False


def get_mouse_coordinates(mouseObject):
    rightPaddle.sety(mouseObject.y)
    if rightPaddle.xcor() > 350 or rightPaddle.xcor() < 350:
        rightPaddle.setx(350)

    if rightPaddle.ycor() > 290:
        rightPaddle.sety(290)

    if rightPaddle.ycor() < -290:
        rightPaddle.sety(-290)
    print(mouseObject.y)


window.listen()
window.onkeypress(move_right_paddle_up, "Up")
window.onkeypress(move_right_paddle_down, "Down")
window.onkeypress(move_left_paddle_up, "w")
window.onkeypress(move_left_paddle_down, "s")
window.onkey(exit_game, "P")
window.onclick(get_mouse_coordinates)


while shouldNotExit:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collisions checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        firstUserScore += 1
        ball.goto(0, 0)
        ball.dx *= -1
        firstScoreArea.clear()
        firstScoreArea.write(
            "Player A: {}".format(firstUserScore),
            align="right",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < -390:
        secondUserScore += 1
        ball.goto(0, 0)
        ball.dx *= -1
        secondScoreArea.clear()
        secondScoreArea.write(
            "Player B: {}".format(secondUserScore),
            align="left",
            font=("Courier", 24, "normal"),
        )

    # ball and paddle collisions checking

    if (
        ball.xcor() > 340
        and ball.ycor() < (rightPaddle.ycor() + 40)
        and (ball.ycor() > rightPaddle.ycor() - 40)
        and ball.xcor() < 350
    ):
        winsound.MessageBeep(winsound.MB_OK)
        ball.setx(340)
        ball.dx *= -1

    if (
        ball.xcor() < -340
        and ball.ycor() < (leftPaddle.ycor() + 40)
        and ball.xcor() > -350
        and ball.ycor() > leftPaddle.ycor() - 40
    ):
        winsound.MessageBeep(winsound.MB_OK)
        ball.setx(-340)
        ball.dx *= -1

    canvas = turtle.getcanvas()
    canvas.bind("<Motion>", get_mouse_coordinates)
