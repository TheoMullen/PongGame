import time
from turtle import Turtle, Screen

screen = Screen()





class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.penup()
        self.color("White")
        self.speed("fastest")
        self.goto(x, y)



    def up(self):
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
            self.goto(self.xcor(), self.ycor() - 20)

    def w(self):
            self.goto(self.xcor(), self.ycor() + 20)

    def s(self):
            self.goto(self.xcor(), self.ycor() - 20)
