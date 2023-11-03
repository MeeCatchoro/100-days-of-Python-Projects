from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.x = 10, -10
        self.finish_line = FINISH_LINE_Y

    def up(self):
        self.forward(MOVE_DISTANCE)

    def y(self):
        return self.ycor() + 10, self.ycor() - 10

    def refresh(self):
        self.setpos(STARTING_POSITION)
