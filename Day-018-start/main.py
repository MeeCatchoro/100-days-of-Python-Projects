import turtle as t
import random as r
timmy = t.Turtle()

t.colormode(255)

# colors = ["magenta", "darkorchid", "blue", "deepskyblue", "cyan", "lime", "greenyellow"]
# for n in range(3, 10):
#     timmy.color(colors[n-3])
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.left(360/n)

timmy.speed(8)
timmy.width(5)


def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return red, green, blue


# directions = [0, 90, 180, 270]
# for n in range(200):
#     timmy.color(random_color())
#     timmy.right(r.choice(directions))
#     timmy.forward(15)

# timmy.speed(20)
# timmy.width(3)
#
# def draw_spirograph(size_of_gap, size_of_circle):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(size_of_circle)
#         current_heading = timmy.heading()
#         timmy.setheading(current_heading + size_of_gap)

# draw_spirograph(30, 150)
# draw_spirograph(22, 110)
# draw_spirograph(15, 80)

screen = t.Screen()
screen.exitonclick()
