from turtle import Screen, Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(500)
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 1
        self.y_move = 1

    def xbounce(self):
        # current_heading = self.heading()
        # print("se",self.heading())
        # if self.heading() == 90 or self.heading() == 270:
        #     # self.x_move *= -1
        self.x_move *= -1
    def ybounce(self):
        # current_heading = self.heading()
        # print("se",self.heading())
        # if self.heading() == 90 or self.heading() == 270:
        #     # self.x_move *= -1
        self.y_move *= -1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


