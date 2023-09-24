from turtle import Turtle, Screen

bee = Turtle()
screen = Screen()

def move_forwards():
    bee.forward(10)

def move_backwards():
    bee.backward(10)

def move_ccw():
    bee.left(10)

def move_cw():
    bee.right(10)

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_ccw, key="a")
screen.onkey(fun=move_cw, key="d")
screen.onkey(fun=bee.reset, key="c")
screen.exitonclick()
