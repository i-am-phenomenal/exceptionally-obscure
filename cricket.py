# import turtle

# shouldNotExit = True

# window = turtle.Screen()
# window.title("Cricket")
# window.bgcolor("green")
# window.setup(800, 600)
# window.tracer()

# pitch = turtle.Turtle()
# pitch.speed(0)
# pitch.color("white")
# pitch.shape("square")
# pitch.penup()
# pitch.shapesize(13, 3)
# pitch.goto(0, 0)


# ball = turtle.Turtle()
# ball.penup()
# ball.speed(0)
# ball.color("red")
# ball.shape("circle")
# ball.shapesize(0.8, 0.8)
# ball.goto(0, -130)
# ball.dx = 3
# ball.dy = 3

# leftStump = turtle.Turtle()
# leftStump.speed(0)
# leftStump.color("black")
# leftStump.penup()
# leftStump.goto(-5, 150)
# leftStump.shape("square")
# leftStump.shapesize(1.5, 0.1)

# middleStump = turtle.Turtle()
# middleStump.speed(0)
# middleStump.color("black")
# middleStump.penup()
# middleStump.goto(0, 150)
# middleStump.shape("square")
# middleStump.shapesize(1.5, 0.1)


# rightStump = turtle.Turtle()
# rightStump.speed(0)
# rightStump.color("black")
# rightStump.penup()
# rightStump.goto(5, 150)
# rightStump.shape("square")
# rightStump.shapesize(1.5, 0.1)


# #Functions
# def throw_ball():
#     while ball.ycor() <= 150: 
#         ball.sety(ball.ycor() + 2)
#     ball.goto(0, -130)
    
# window.listen()
# window.onkey(throw_ball, "Up")

# while shouldNotExit:
#     window.update()








import pygame


ground_color = [127, 255, 0]
pygame.init()
window = pygame.display.set_mode((800, 600))
shouldExitGame = False
window.fill(ground_color)

pitch_color = (255, 239, 219)
ball_color = (238, 59, 59)
bat_color = (238, 154, 73)
clock = pygame.time.Clock()
ballXCoordinate = 420
ballYCoordinate = 420
bat_rotation_angle = 0

# ball = pygame.draw.circle(window, ball_color, (ballXCoordinate, ballYCoordinate), 7)
pitch = pygame.draw.rect(window, pitch_color, pygame.Rect(400, 200, 60, 200))
# bat = pygame.draw.rect(window, bat_color, (430, 170, 10, 50))
# wicket_image = pygame.transform.scale(
#     pygame.image.load("C:/practice Programs/wickets.jpeg"), (50, 50)
# )


# Functions

while not shouldExitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shouldExitGame = True

    pressedKey = pygame.key.get_pressed()
    if pressedKey[pygame.K_UP]:
        ballYCoordinate -= 3
        if ballYCoordinate <= 150:
            ballYCoordinate = 420

    pygame.draw.rect(window, pitch_color, pygame.Rect(400, 200, 60, 200))
    window.blit(
        pygame.transform.scale(
            pygame.image.load("C:/practice Programs/wickets.jpeg"), (35, 50)
        ),
        (410, 150),
    )
    pygame.draw.circle(window, ball_color, (ballXCoordinate, ballYCoordinate), 7)
    bat = pygame.draw.rect(window, bat_color, pygame.Rect(430, 170, 10, 50))
    bat_surface = pygame.Surface((bat.w, bat.h))
    pygame.transform.rotate(bat_surface, 180)
    # window.blit(surface)
    # pygame.transform.rotate(
    #     pygame.draw.rect(window, bat_color, pygame.Rect(430, 170, 10, 50)),
    #     bat_rotation_angle,
    # )

    pygame.display.flip()
    clock.tick(60)
    window.fill(ground_color)


