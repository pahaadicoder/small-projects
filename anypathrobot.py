def go():
    
 while not at_goal():
     if front_is_clear():
        move()
     elif wall_in_front():
        turn_left()
     if right_is_clear():
        turn_right()
        move()     
move()           
go()           
        
    
    