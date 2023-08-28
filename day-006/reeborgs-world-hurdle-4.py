def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right() == True:
        if front_is_clear() == True:
            move()
        else: 
            turn_left()
    else:
        turn_right()
        move()
        turn_right()
        move()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
