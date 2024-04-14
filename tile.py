from turtle import Turtle


class Tile(Turtle):
    def __init__(self, coordinates: tuple) -> None:
        super().__init__()
        self.coord = coordinates
        self.shape("square")
        self.color("grey")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(coordinates)
