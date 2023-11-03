from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(10):
            new_car = Turtle("square")
            new_car.speed("fastest")
            new_car.color(choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.setpos(randint(-290, 301), randint(-230, 231))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)
            if car.xcor() < -300:
                car.setpos(300, car.ycor())

    def hitbox(self):
        hitbox = []
        for car in self.cars:
            carx = car.xcor() + 20, car.xcor() - 20
            cary = car.ycor() + 10, car.ycor() - 10
            hitbox.append((carx, cary))
        return hitbox

    def increase_movement(self):
        self.move_distance += MOVE_INCREMENT

    def refresh(self):
        self.increase_movement()
        for car in self.cars:
            car.setpos(randint(-290, 301), randint(-230, 231))
