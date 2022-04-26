from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(2)
        self.color("white")
        self.penup()
        self.x_move = 8
        self.y_move = 8


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if self.ycor() >= 315 or self.ycor() <= -315:
            self.vertical_bounce()


    def vertical_bounce(self):
        self.y_move *= -1


    def horizontal_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.setpos(0, 0)
        self.horizontal_bounce()