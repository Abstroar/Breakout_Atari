from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("square")
        self.color("white")
        self.goto(-325, -270)
        self.shapesize(stretch_wid=0.7, stretch_len=4)


    def move_left(self):
        movement = self.xcor() - 30
        if movement <= -355:
            movement = -355
        self.goto(movement, self.ycor())
    def move_right(self):
        movement = self.xcor() + 30
        if movement > 355:
            movement = 355
        self.goto(movement, self.ycor())

