from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.setpos(0, 280)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="Game over.", align="center", font=("Arial", 30, "normal"))
