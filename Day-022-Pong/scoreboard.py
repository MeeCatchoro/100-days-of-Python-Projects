from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.score = 0

    def update_score(self):
        self.write(arg=f"{self.score}", align="center", font=("Arial", 30, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def computer_wins(self):
        self.setpos(0, 0)
        self.write(arg="Computer wins. You lose", align="center", font=("Arial", 30, "normal"))

    def player_wins(self):
        self.setpos(0, 0)
        self.write(arg="You won. Congratulations!", align="center", font=("Arial", 30, "normal"))


class PlayerScore(Scoreboard):

    def __init__(self):
        super().__init__()
        self.setpos(-50, 330)
        self.update_score()


class ComputerScore(Scoreboard):

    def __init__(self):
        super().__init__()
        self.setpos(50, 330)
        self.update_score()


class Division(Scoreboard):

    def __init__(self):
        super().__init__()
        self.setpos(x=0, y=-400)
        self.setheading(90)
        for _ in range(20):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
