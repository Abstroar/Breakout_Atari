from turtle import Screen, Turtle
from tiles import Tiles
import time
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
# screen.tracer(0)

game_status = True

screen.tracer(0)
x = Ball()
player = Paddle()
tiles = []
for i in range(-380, 390, 32):
    y = Tiles()
    yy = Tiles()
    yyy = Tiles()
    y.goto(i, 290)
    yy.goto(i + 5, 277)
    yyy.goto(i, 265)
    tiles.append(y)
    tiles.append(yy)
    tiles.append(yyy)

screen.listen()
# screen.onkey(player.move_left, "w")
screen.update()
player.move_left()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

def gettiles(tar_x,tar_y,threshhold):
    selected = []
    for t in tiles:
        if t.distance(tar_x, tar_y) < threshhold:
            selected.append(t)
            t.hideturtle()
            tiles.remove(t)
            t.clear()
            return True
            # print("hii")
while game_status:
    screen.update()
    # print(x.position())
    if x.ycor() > 290:
        x.ybounce()
    elif x.xcor() > 390 or x.xcor() < -390:
        x.xbounce()
    elif x.y_move < 0 and x.distance(player) < 30 and x.ycor() > - 290:
        x.ybounce()
    elif x.ycor() < -287:
        print("game over")
        game_status = False
    elif x.y_move > 0 and gettiles(x.xcor(), x.ycor(), 10):
        x.ybounce()
    elif x.ycor() < -290:
        game_status= False
    x.move()




screen.exitonclick()

