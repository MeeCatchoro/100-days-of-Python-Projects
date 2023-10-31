from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.speed = 20

    def create_snake(self):
        x = 0
        for _ in range(3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.setpos(x=x, y=0)
            x -= 20
            self.snake_body.append(segment)

    def add_segment(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.setpos(self.snake_body[-1].position())
        self.snake_body.append(segment)

    def move(self):
        for n in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[n - 1].xcor()
            y = self.snake_body[n - 1].ycor()
            self.snake_body[n].setpos(x=x, y=y)
        self.head.forward(self.speed)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
