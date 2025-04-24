from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    obtain_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_around()
    move_til_cant()
    turn_right()
    move_til_cant()
    turn_around()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def obtain_beeper():
    while no_beepers_present():
        move()
    pick_beeper()

def turn_around():
    turn_left()
    turn_left()

def move_til_cant():
    while front_is_clear():
        move()    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
