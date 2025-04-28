from karel.stanfordkarel import *

"""
1. row: place beeper and move
2. must work no matter how big the world is
3. turn around when she hits a wall
4. go back to start of row, turn right, go up one, turn right
5. place beepers on next row
6. keep going until karel can't go up a row after returning
"""


def main():
    while no_beepers_present():
        place_beepers()
        return_to_row_start()
        up_one_row()
    if front_is_blocked():
        turn_right()
        go_to_wall()

#check for beepers
def beeper_check():
    while no_beepers_present():
        put_beeper()
        move()

#go to wall
def go_to_wall():
    while front_is_clear():
        move()

#place beepers on whole row
def place_beepers():
    while front_is_clear():
        put_beeper()
        move() 
    if front_is_blocked():
        put_beeper()
        turn_around()

#return to start of row
def return_to_row_start():
    while front_is_clear():
        move()
    if front_is_blocked():
        turn_right()

#move up one row unless it's blocked
def up_one_row():
    if front_is_clear():
        move()
        turn_right()
    

#Turn right, aka left three times
def turn_right():
   for i in range(3):
        turn_left()

#Turn to face opposite direction
def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
