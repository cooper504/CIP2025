from karel.stanfordkarel import *

"""
This is a list of functions I've come up with for Karel. Will keep adding as CIP 2025 progresses.
"""
def main():
  turn_right()
  obtain_beeper()
  turn_around()
  wall_move()
  

# My Karel functions
#Turn right, aka left three times
def turn_right():
   for i in range(3):
        turn_left()

#Move until you find a beeper and then pick it up
def obtain_beeper():
    while no_beepers_present():
        move()
    pick_beeper()

#Turn to face opposite direction
def turn_around():
    turn_left()
    turn_left()

#Move forward to wall
def wall_move():
    if front_is_clear():
        move()     
