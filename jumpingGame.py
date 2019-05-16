import turtle
import time
import threading
import random
from multiprocessing  import Pool

delay = 0.04
obstacle_delay = 0.02
obstacle2_delay = 0.03
obstacle3_delay = 0.04
random_x_coordinate = 0

window = turtle.Screen()
window.title("Jumping Game")
window.bgcolor("grey")
window.setup(width=600, height=600)
window.tracer(0)

car = turtle.Turtle()
car.speed(0)
car.color("green")
car.shape("square")
car.shapesize(2,1)  # 1st parameter increases height and second parameter increases width
car.penup()
car.goto(-130, -260)

#
#road_left_line = turtle.Turtle()
#road_left_line.color("black")
#road_left_line.shape("square")
#road_left_line.penup()
#road_left_line.goto(-250, 150)
#road_left_line.shapesize(9, 0.1)
#road_left_line.direction = "down"
#
#
#road_left_line2 = turtle.Turtle()
#road_left_line2.color("black")
#road_left_line2.shape("square")
#road_left_line2.penup()
#road_left_line2.goto(-250, -120)
#road_left_line2.shapesize(9, 0.1)
#road_left_line2.direction = "down"
#
#
#road_right_line = turtle.Turtle()
#road_right_line.color("black")
#road_right_line.shape("square")
#road_right_line.penup()
#road_right_line.goto(250, 150)
#road_right_line.shapesize(9, 0.1)
#road_right_line.direction = "down"
#
#
#road_right_line2 = turtle.Turtle()
#road_right_line2.color("black")
#road_right_line2.shape("square")
#road_right_line2.penup()
#road_right_line2.goto(250, -120)
#road_right_line2.shapesize(9, 0.1)
#road_right_line2.direction = "down"
#
#road_middle_line = turtle.Turtle()
#road_middle_line.color("black")
#road_middle_line.shape("square")
#road_middle_line.penup()
#road_middle_line.goto(0, 150)
#road_middle_line.shapesize(9, 0.1)
#road_middle_line.direction = "down"
#
#road_middle_line2 = turtle.Turtle()
#road_middle_line2.color("black")
#road_middle_line2.shape("square")
#road_middle_line2.penup()
#road_middle_line2.goto(0, -120)
#road_middle_line2.shapesize(9, 0.1)
#road_middle_line2.direction = "down"

obstacle = turtle.Turtle()
obstacle.color("red")
obstacle.shape("square")
obstacle.penup()
obstacle.goto(-130, 290)
obstacle.direction = "down"

obstacle2 = turtle.Turtle()
obstacle2.color("red")
obstacle2.shape("square")
obstacle2.penup()
obstacle2.goto(0,0)
obstacle2.direction = "down"

obstacle3 = turtle.Turtle()
obstacle3.color("red")
obstacle3.shape("square")
obstacle3.penup()
obstacle3.goto(130, 290)
obstacle3.direction = "down"

obstacle4 = turtle.Turtle()
obstacle4.color("red")
obstacle4.shape("square")
obstacle4.penup()
obstacle4.goto(-250, 200)
obstacle4.direction = "down"

obstacle5 = turtle.Turtle()
obstacle5.color("red")
obstacle5.shape("square")
obstacle5.penup()
obstacle5.goto(250, 200)
obstacle5.direction = "down"

obstacle6 = turtle.Turtle()
obstacle6.color("red")
obstacle6.shape("square")
obstacle6.penup()
obstacle6.goto(200, 200)
obstacle6.direction = "down"

#def move_road_left_lines():
#    if road_left_line.direction == "down" and road_left_line2.direction == "down":
#        y_coordinate_for_left_line1 = road_left_line.ycor()
#        road_left_line.sety(y_coordinate_for_left_line1 - 20)
#        y_coordinate_for_left_line2 = road_left_line2.ycor()
#        road_left_line2.sety(y_coordinate_for_left_line2 - 20)
#        time.sleep(delay)
#
#    if road_left_line.ycor() <= -290:
#        road_left_line.sety(290)
#
#    if road_left_line2.ycor() <= -290:
#        road_left_line2.sety(290)
#
#def move_road_right_lines():
#    if road_right_line2.direction == "down" and road_right_line.direction == "down":
#        y_cor_right_line = road_right_line.ycor()
#        road_right_line.sety(y_cor_right_line - 20)
#        y_cor_right_line2 = road_right_line2.ycor()
#        road_right_line2.sety(y_cor_right_line2 - 20)
#        time.sleep(delay)
#
#    if road_right_line.ycor() <= -290:
#        road_right_line.sety(290)
#
#    if road_right_line2.ycor() <= -290:
#        road_right_line2.sety(290)
#
#def move_road_middle_lines():
#    if road_middle_line.direction == "down" and road_middle_line2.direction == "down":
#        y_cor_for_mid_line = road_middle_line.ycor()
#        road_middle_line.sety(y_cor_for_mid_line - 20)
#
#        y_cor_for_mid_line2 = road_middle_line2.ycor()
#        road_middle_line2.sety(y_cor_for_mid_line2 - 20)
#
#    if road_middle_line.ycor() <= -290:
#        road_middle_line.sety(290)
#
#    if road_middle_line2.ycor() <= -290:
#        road_middle_line2.sety(290)

def move_obstacle1():
    if obstacle.direction == "down":
        y = obstacle.ycor()
        obstacle.sety(y - 20)

    if obstacle.ycor() <= -290:
        x = random.randint(-280, 280)
        print(x)
        obstacle.goto(x, 290)
        
        
def move_obstacle4():
    
    if obstacle4.direction == "down":
        y = obstacle4.ycor()
        obstacle4.sety(y - 20)

    if obstacle4.ycor() <= -290:
        x = random.randint(-280, 280)
        print(x)
        obstacle4.goto(x, 290)
        
        
def move_obstacle5():
    
    if obstacle5.direction == "down":
        y = obstacle5.ycor()
        obstacle5.sety(y - 20)

    if obstacle5.ycor() <= -290:
        x = random.randint(-280, 280)
        obstacle5.goto(x, 290)

def move_obstacle6():    
    if obstacle6.direction == "down":
        y = obstacle6.ycor()
        obstacle6.sety(y - 20)

    if obstacle6.ycor() <= -290:
        x = random.randint(-280, 280)
        obstacle6.goto(x, 290)
        
        
def move_obstacle2():
    if obstacle2.direction == "down":
        y2 = obstacle2.ycor()
        obstacle2.sety(y2 - 20)

    if obstacle2.ycor() <=-290:
           x2 = random.randint(-280, 280)
           print(x2)
           obstacle2.goto(x2, 290)

def move_obstacle3():
    global obstacle3_delay
    if obstacle3.direction == "down":
        y3 = obstacle3.ycor()
        obstacle3.sety(y3 - 20)
        # time.sleep(obstacle3_delay)

    if obstacle3.ycor() <= -290:
        x3 = random.randint(-280, 280)
        print(x3)
        obstacle3.goto(x3, 290)


def go_left():
    x_coordinate = car.xcor()
    if car.xcor() <= -280:
        car.setx(x_coordinate)
    else:
        car.setx(x_coordinate - 30)

def go_right():
    x_coordinate = car.xcor()
    if car.xcor() >= 280:
        car.setx(x_coordinate)
    else:
        car.setx(x_coordinate + 30)

def restart_game():
#    road_left_line.direction = "down"
#    road_left_line2.direction = "down"
#    road_middle_line.direction = "down"
#    road_middle_line2.direction ="down"
#    road_right_line.direction = "down"
#    road_right_line.direction = "down"
    obstacle.direction = "down"
    obstacle2.direction = "down"
    obstacle3.direction = "down"
    obstacle4.direction = "down"
    obstacle5.direction = "down"
    obstacle6.direction = "down"

def check_for_collisions():
    if obstacle.distance(car) < 20 or obstacle2.distance(car) < 20 or obstacle3.distance(car) < 20 or obstacle4.distance(car) < 20 or obstacle5.distance(car) or obstacle6.distance(car) < 20:
        car.goto(-130, -260)
        time.sleep(1)
#        road_left_line.goto(-250, 150)
#        road_left_line2.goto(-250, -120)
#        road_middle_line.goto(0, 150)
#        road_middle_line2.goto(0, -120)
#        road_right_line.goto(250, 250)
#        road_right_line2.goto(250, -120)
        obstacle.goto(-130, 290)
        obstacle2.goto(130, 290)
        obstacle3.goto(-170, 290)
#        road_left_line.direction = "stop"
#        road_left_line2.direction = "stop"
#        road_middle_line.direction = "stop"
#        road_middle_line2.direction = "stop"
#        road_right_line.direction = "stop"
#        road_right_line2.direction = "stop"
        obstacle.direction = "stop"
        obstacle2.direction = "stop"
        obstacle3.direction = "stop"
        obstacle4.direction = "stop"
        obstacle5.direction = "stop"
        obstacle6.direction = "stop"
        car.penup()

def list_of_all_functions():
    move_obstacle1()
    move_obstacle2()
    move_obstacle3()

window.listen()
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(restart_game, "Return")
window.onkey(restart_game, "Up")
window.onkey(restart_game, "Down")
while True:
    window.update()
#    move_road_left_lines()
#    move_road_right_lines()
#    move_road_middle_lines()
    move_obstacle1()
    move_obstacle2()
    move_obstacle3()
    move_obstacle4()
    move_obstacle5()
    move_obstacle6()
    time.sleep(delay)
    check_for_collisions()

window.mainloop()
