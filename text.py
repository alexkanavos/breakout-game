from turtle import Turtle


class Text(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto((0, 300))

    def message(self, result: bool):
        if result:
            self.write("YOU WON!", align="center", font=("Arial", 24, "normal"))
        else:
            self.write("GAME OVER.", align="center", font=("Arial", 24, "normal"))
