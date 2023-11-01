from turtle import Turtle

SPEED = 20
POSITION = [-350, 350]


class Paddle(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def x(self):
        return self.xcor() + 15, self.xcor() - 15

    def y(self):
        return self.ycor() + 65, self.ycor() - 65

    def up(self):
        if self.y()[0] < 400:
            self.setheading(90)
            self.forward(SPEED)

    def down(self):
        if self.y()[1] > -400:
            self.setheading(270)
            self.forward(SPEED)


class Player(Paddle):

    def __init__(self):
        super().__init__()
        self.setpos(POSITION[0], 0)


class Computer(Paddle):

    def __init__(self):
        super().__init__()
        self.setpos(POSITION[1], 0)
