from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
"""
pre: karel in lower left spot, no beepers
post: karel in lower righ spot, beepers placed

1. place beepers up 5 spots (build column)
2. return to bottom of column
3. move to next column 4 spots to right
4. turn left
5. build column
6. stop building columns when you hit wall

"""
def main():
    for i in range(4):
        build_column()
        return_to_bottom()
        next_column()


#Turn right, aka left three times
def turn_right():
   for i in range(3):
        turn_left()

#Place beepers vertically up 5 units
def build_column():
    turn_left()
    put_beeper()
    for i in range(4):
        move()
        put_beeper()
    turn_left()
    turn_left()    

#return to bottom of column
def return_to_bottom():
    for i in range(4):
        move()
    turn_left()    

#go 4 spaces to next column
def next_column():
    if front_is_clear():
        for h in range(4):
            move()



if __name__ == '__main__':
    main()
