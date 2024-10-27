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

for i in range(-380, 390, 32):
    y = Tiles()
    yy = Tiles()
    yyy = Tiles()
    y.goto(i, 290)
    yy.goto(i + 5, 277)
    yyy.goto(i, 265)

screen.listen()
# screen.onkey(player.move_left, "w")
screen.update()
player.move_left()
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "Right")



while game_status:

    screen.update()
    # print(x.position())
    if x.ycor() > 290:
        x.ybounce()
    elif x.xcor() > 390 or x.xcor() < -390:
        x.xbounce()

    if x.distance(player) < 30 and x.ycor() > - 290:
        x.ybounce()



    x.move()




screen.exitonclick()

