def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def completed_goal():
    while not at_goal():
        if front_is_clear():
            if right_is_clear() and not wall_on_right():
                turn_right()
                move()
            elif not right_is_clear() and wall_on_right():
                move()
        elif not wall_on_right() and right_is_clear():
            turn_right()
            move()
        elif wall_on_right() and not right_is_clear():
            turn_left()
            if not front_is_clear() and wall_in_front():
                turn_left()
                move()
            else:
                move()
        else:
            done()
        
       
        
            
            
completed_goal()
            
        
    


    
    





