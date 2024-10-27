from turtle import Turtle
import random

colo = ["red","yellow","green"]
class Tiles(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=0.5,stretch_len=1.5)
        self.speed(1000)
        self.color(colo[random.randrange(0,3)])
        self.penup()
        # self.goto(0, 250)
        self.color(colo[random.randrange(0,3)])



