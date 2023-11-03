from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.setpos(-280, 260)
        self.level = 1
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.setpos(0, 0)
        self.write("Game Over", align="center", font=("Courier", 30, "normal"))