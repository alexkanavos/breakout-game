from turtle import Turtle


class Ball(Turtle):

    def __init__(self, coordinates: tuple) -> None:
        super().__init__()
        self.coord = coordinates
        self.shape("circle")
        self.color("white", "white")
        self.penup()
        self.goto(coordinates)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
