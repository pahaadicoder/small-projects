def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def go():
    while not at_goal():
        if front_is_clear() and right_is_clear():
            turn_right()
            move()
            
        if front_is_clear():
            move()
            
        elif right_is_clear():
            turn_right()
            if front_is_clear():
               move()
        elif wall_on_right():
            turn_left()
            
         

      
go()           

             
    
        
        
        


