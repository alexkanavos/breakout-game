from turtle import Turtle


MOVE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, coordinates: tuple) -> None:
        super().__init__()
        self.coord = coordinates
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(coordinates)

    def move_right(self) -> None:
        if self.xcor() < 300:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_left(self) -> None:
        if self.xcor() > -300:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
