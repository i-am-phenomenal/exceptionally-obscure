import turtle
import time
import random

delay = 0.03
snakeBody = []
score = 0
highScore = 0
is_game_paused = False
can_play_game = True

#Setting up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("grey")
window.setup(width=600,height=600)
window.tracer(0) #turns off the animation or the screen updates

#logic for game is betweenn tracer and mainloop

#Snake head
snakeHead = turtle.Turtle()
snakeHead.speed(0) #animation speed of the turtle module
snakeHead.shape("square")
snakeHead.color("black")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "stop"


# snake food
def getSnakeFood(xCordForFood, yCordForFood):
    snakeFood = turtle.Turtle()
    snakeFood.speed(0)
    snakeFood.shape("circle")
    snakeFood.color("red")
    snakeFood.penup()
    snakeFood.goto(xCordForFood, yCordForFood)
    return snakeFood

def getScore(score):
    global highScore
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: {}   High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))
    pen.clear()
    return pen

def getXCordForFood():
    global xCordForFood
    xCordForFood = random.randint(-290, 290)
    if xCordForFood % 10 == 0:
        return xCordForFood
    else:
        getXCordForFood()

def getYCordForFood():
    global yCordForFood
    yCordForFood = random.randint(-290, 290)
    if yCordForFood % 10 == 0:
        return yCordForFood
    else:
        getYCordForFood()


xCordForFood = 0
getXCordForFood()
yCordForFood = 0
getYCordForFood()

snakeFood = getSnakeFood(xCordForFood, yCordForFood)
#Functions
def remove_pause_message():
    screen_remover = turtle.Turtle()
    screen_remover.up()
    screen_remover.goto(0, -260)
    screen_remover.color("grey")
    screen_remover.begin_fill()
    screen_remover.setheading(0)
    for iter in range(2):
        screen_remover.fd(260)


def check_if_game_is_paused():
    global is_game_paused
    pause_message = turtle.Turtle()
    pause_message.speed(0)
    pause_message.shape("square")
    pause_message.color("black")
    pause_message.penup()
    pause_message.hideturtle()
    pause_message.goto(0, -260)
    if is_game_paused:
        pause_message.write("Press escape to pause and any arrow key to resume", align="center", font = ("Courier", 12, "normal"))


def move():
    global xCordForFood, yCordForFood
    getXCordForFood()
    getYCordForFood()

    if snakeHead.direction == "up":
        snakeFood.showturtle()
        yCord = snakeHead.ycor()
        snakeHead.sety(yCord + 10)
        if snakeHead.ycor() >= 300:
           snakeHead.sety(-300)

    if snakeHead.direction == "down":
        snakeFood.showturtle()
        yCord = snakeHead.ycor()
        snakeHead.sety(yCord - 10)
        if snakeHead.ycor() <= -300:
           snakeHead.sety(300)

    if snakeHead.direction == "left":
        snakeFood.showturtle()
        xCord = snakeHead.xcor()
        snakeHead.setx(xCord - 10)
        if snakeHead.xcor() <= -300:
           snakeHead.setx(300)

    if snakeHead.direction == "right":
        snakeFood.showturtle()
        xCord = snakeHead.xcor()
        snakeHead.setx(xCord + 10)
        if snakeHead.xcor() >= 300:
           snakeHead.setx(-300)

def go_up():
    global is_game_paused
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
        is_game_paused = False

def go_down():
    global is_game_paused
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
        is_game_paused = False

def go_left():
    global is_game_paused
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
        is_game_paused = False

def go_right():
    global is_game_paused
    if snakeHead.direction != "left":
        snakeHead.direction = "right"
        is_game_paused = False

def pause_game():
    global is_game_paused
    window.freeze()
    snakeHead.direction = "stop"
    is_game_paused = True

def exit_game():
    global can_play_game
    can_play_game = False


#Keyboard bindings

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down,"Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(pause_game, "Escape")
window.onkey(exit_game, "e")

# main game loop
while True:
    window.update()

    snakeXCord = snakeHead.xcor()
    snakeYCord = snakeHead.ycor()
    if snakeHead.distance(snakeFood) < 20:
        getXCordForFood()
        getYCordForFood()
        snakeFood.goto(xCordForFood, yCordForFood)
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("blue")
        body.penup()
        snakeBody.append(body)


    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < -290:
        snakeHead.reset()
        snakeHead.penup()
        snakeHead.direction = "stop"
        snakeFood.reset()
        snakeFood.penup()
        snakeFood.hideturtle()
        for ele in snakeBody:
            ele.hideturtle()

    if snakeHead.direction == "stop":
        snakeBody.clear()

    for index in range((len(snakeBody)-1), 0, -1):
            x = snakeBody[index - 1].xcor()
            y = snakeBody[index - 1].ycor()
            snakeBody[index].goto(x,y)

    if len(snakeBody) > 0: #and snakeHead.direction is not "stop":
            x = snakeHead.xcor()
            y = snakeHead.ycor()
            snakeBody[0].goto(x, y)


        # snakeHead.goto(0,0)
        # snakeHead.direction = "stop"
        # snakeBody = []
        # window.clear()
        # window.bgcolor("grey")
        # snakeHead.hideturtle()
        # window.title("Snake Game")
        # pen.clear()
        # window.tracer(0)

    move()

    score = len(snakeBody)
    if score >= highScore:
        highScore = score

    check_if_game_is_paused()
    pen = getScore(score)


    # for element in snakeBody:
    #     if element.distance(snakeHead) < 20:
    #         time.sleep(1)
    #         snakeHead.goto(0, 0)
    #         snakeHead.direction = "stop"
    #
    #         for body in snakeBody:
    #             print(" I am here")
    #             body.goto(1000, 1000)
    #
    #         snakeBody.clear()


    time.sleep(delay)

window.mainloop()
