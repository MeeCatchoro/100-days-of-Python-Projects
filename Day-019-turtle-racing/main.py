from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

height = 100
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=height)
    height -= 40
    turtles.append(new_turtle)

racing = False

if user_bet:
    racing = True
else:
    print("You did not make a bet")

while racing:
    winner = 0
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner += 1
            racing = False

            if user_bet.lower() == turtle.pencolor() and winner == 1:
                print(f"Congratulations! The {turtle.pencolor()} turtle is the winner.")
            elif winner == 1:
                print(f"Too bad... The {turtle.pencolor()} turtle is the winner.")
        distance = randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
