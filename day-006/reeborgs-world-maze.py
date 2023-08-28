def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    else:
        move()
        
#Per course: After Day 15, come back to Day 6 to debug this code (due to edge case infinite loops).
