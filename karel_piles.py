from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    while front_is_clear():
        obtain_all_beepers()
        if no_beepers_present():
            move()
        
    
   
# My Karel functions
#Turn right, aka left three times
def turn_right():
   for i in range(3):
        turn_left()

#Move until you find a beeper and then pick them all up
def obtain_all_beepers():
     while beepers_present():
            pick_beeper()

#Turn to face opposite direction
def turn_around():
    turn_left()
    turn_left()

#Move to wall
def wall_move():
    while front_is_clear():
        move()     
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
