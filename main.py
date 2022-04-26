from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(700, 600)
screen.title("pong")
screen.tracer(0)


left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
delay = 0.1

screen.listen()
screen.onkey(left_paddle.w, "w")
screen.onkey(left_paddle.s, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_on = True

while game_on:
    screen.update()
    time.sleep(delay)
    ball.move()

    #Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.horizontal_bounce()
        delay *= 0.75

    #Right misses
    if ball.xcor() > 350:
        ball.reset_position()
        scoreboard.l_point()
        delay = 0.1

    #Left misses
    if ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
        delay = 0.1

screen.exitonclick()