import turtle
import time
import random

delay = 0.05
snakeBody = []
score = 0
#Setting up the screen

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("grey")
window.setup(width=600,height=600)
window.tracer(0) #turns off the animation or the screen updates

#logic for game is betweenn tracer and mainloop 

#Snake head

snakeHead = turtle.Turtle()
snakeHead.speed(0) #animation speed if the turtle module
snakeHead.shape("square")
snakeHead.color("blue")
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
print([xCordForFood, yCordForFood ])
snakeFood = getSnakeFood(xCordForFood, yCordForFood)
#Functions 
def updateSnake():
    global xCordForFood, yCordForFood, snakeFood, snakeBody, score
    snakeXCord = snakeHead.xcor()
    snakeYCord = snakeHead.ycor()
    if snakeHead.distance(snakeFood) < 20:
        getXCordForFood()
        getYCordForFood()
        snakeFood.goto(xCordForFood, yCordForFood)
        body = turtle.Turtle()
        body.shape("square")
        body.color("blue")
        body.speed(0)
        body.penup()
        snakeBody.append(body)
        score = len(snakeBody)
        
    
    for index in range(len(snakeBody)-1, 0,-1):
            x = snakeBody[index - 1].xcor()
            y = snakeBody[index - 1].ycor()
            snakeBody[index].goto(x,y)
            
    if len(snakeBody) > 0:
            x = snakeHead.xcor()
            y = snakeHead.ycor()
            snakeBody[0].goto(x, y)
            
    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < 290:
        snakeHead.goto(0,0)
        snakeBody = []
    
def move():
#    print([snakeHead.xcor() , snakeHead.ycor()])
#    print("+++++", [snakeFood.xcor(), snakeFood.ycor()])
    if snakeHead.direction == "up":
        yCord = snakeHead.ycor()
        snakeHead.sety(yCord + 10)
#        if snakeHead.ycor() >= 300:
#            snakeHead.sety(-300)
        
    if snakeHead.direction == "down":
        yCord = snakeHead.ycor()
        snakeHead.sety(yCord - 10)
#        if snakeHead.ycor() <= -300:
#            snakeHead.sety(300)
        
    if snakeHead.direction == "left":
        xCord = snakeHead.xcor()
        snakeHead.setx(xCord - 10)
#        if snakeHead.xcor() <= -300:
#            snakeHead.setx(300)
        
    if snakeHead.direction == "right":
        xCord = snakeHead.xcor()
        snakeHead.setx(xCord + 10)
#        if snakeHead.xcor() >= 300:
#            snakeHead.setx(-300)
        
def go_up():
    snakeHead.direction = "up"
    
def go_down():
    snakeHead.direction = "down"
    
def go_left():
    snakeHead.direction = "left"
    
def go_right():
    snakeHead.direction = "right"

    
#Keyboard bindings

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down,"Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
# main game loop

while True:
    window.update()
    move()
    updateSnake()

    time.sleep(delay)

window.mainloop()