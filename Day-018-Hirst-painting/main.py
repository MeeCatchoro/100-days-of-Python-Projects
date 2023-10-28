# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     c = (r, g, b)
#     rgb_colors.append(c)
#
# print(rgb_colors)
import turtle
from random import choice
from turtle import *
color_list = [(238, 251, 245), (188, 19, 46), (244, 233, 61), (252, 230, 236), (217, 238, 244), (195, 76, 34), (218, 66, 106), (15, 142, 89), (196, 176, 19), (21, 125, 173), (108, 182, 209), (18, 167, 213), (209, 153, 90), (26, 40, 75), (36, 43, 110), (79, 175, 96), (181, 44, 65), (235, 231, 5), (216, 67, 48), (217, 129, 153), (125, 185, 119), (238, 161, 180), (8, 61, 38), (148, 209, 221), (9, 92, 53), (6, 87, 109), (160, 30, 27), (237, 169, 162), (159, 212, 183)]

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.setpos(-230, -230)
colormode(255)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)
    pos = tim.pos()
    tim.setpos(pos[0] - 500, pos[1] + 50)

screen = turtle.Screen()
screen.exitonclick()
