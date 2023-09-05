import turtle as turtle_module
import random

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]
turtle_module.colormode(255)
honey = turtle_module.Turtle()
honey.speed(0)
honey.hideturtle()

honey.setheading(225)
honey.penup()
honey.forward(250)
honey.pendown()
honey.setheading(0)
number_of_dots = 10
def row_of_dots():
    for _ in range(number_of_dots):
        honey.dot(20, random.choice(color_list))
        honey.penup()
        honey.forward(50)
        honey.pendown()


def reposition_honey(y):
    for _ in range(number_of_dots):
        honey.penup()
        honey.goto(-176.77669529663686, y)
        return

reposition_honey(-176.7766952966369)
row_of_dots()
reposition_honey(-126.7766952966369)
row_of_dots()
reposition_honey(-76.7766952966369)
row_of_dots()
reposition_honey(-26.7766952966369)
row_of_dots()
reposition_honey(23.2233047033631)
row_of_dots()
reposition_honey(73.2233047033631)
row_of_dots()
reposition_honey(123.2233047033631)
row_of_dots()
reposition_honey(173.2233047033631)
row_of_dots()
reposition_honey(223.2233047033631)
row_of_dots()
reposition_honey(273.2233047033631)
row_of_dots()

screen = turtle_module.Screen()
screen.exitonclick()

#I want to come back eventually and fix the outputs because I know there is a more efficient way instead of hardcoding the numbers, but my brain is not braining right now
