# import colorgram as cg
#
# rgb_colors = []
#
# colors = cg.extract("image.jpg", 20)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random as rd

t.colormode(255)

color_list = [(209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)]

rick = t.Turtle()
screen = t.Screen()

rick.hideturtle()
rick.speed(0)

y_pos = 50

for y in range(10):
    for x in range(10):
        rick.penup()
        rick.dot(20, rd.choice(color_list))
        rick.forward(50)
    rick.teleport(0, y_pos)
    y_pos += 50


screen.exitonclick()
