from turtle import Screen
from paddle import Paddle
from tile import Tile
from ball import Ball
import time
import math


MAX_Y = 370
MIN_Y = -370
MAX_X = 330
MIN_X = -330
DIST = 20 * math.sqrt(10)

screen = Screen()
screen.bgcolor("black")
screen.title("Breakout")
screen.setup(width=720, height=800)
screen.tracer(0)

paddle = Paddle(coordinates=(0, -370))
ball = Ball(coordinates=(0, -350))

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

tiles = []

for i in range(0, 211, 30):
    y = i
    for j in range(0, 671, 70):
        x = 315 - j
        tiles.append(Tile(coordinates=(x, y)))


while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > MAX_Y or ball.distance(paddle) < DIST and ball.ycor() < -340:
        ball.bounce_y()

    if ball.xcor() > MAX_X:
        ball.bounce_x()

    if ball.xcor() < MIN_X:
        ball.bounce_x()

    if ball.ycor() < -370:
        break

# if __name__ == "__main__":
#     print("ok")

screen.exitonclick()
