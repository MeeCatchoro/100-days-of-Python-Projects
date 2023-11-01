from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.velocity = 5
        self.x = -5
        self.y = -5

    def move(self):
        self.setheading(0)
        self.forward(self.x)
        self.setheading(90)
        self.forward(self.y)

    def refresh(self, direction):
        self.goto(0, 0)
        self.velocity *= 1.1
        if direction == "right":
            self.x = self.velocity
            self.y = self.velocity
        elif direction == "left":
            self.x = -self.velocity
            self.y = -self.velocity

    def wall_collision(self):
        self.y = int(self.y * (-1))

    def paddle_collision(self):
        self.x = int(self.x * (-1.2))
        self.y *= 1.2
