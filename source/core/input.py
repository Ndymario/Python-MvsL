'''
Authors: Nolan Y., Christopher D.
Descripion: File that will house input functions
'''

from raylibpy import *

def function_name():
    print("Test Function is in fact running :)");
    return 2

def do_sprint(player):
    player.acceleration = .5;

def move_left(player):
    player.adjust_speed(-1)

def move_right(player):
    player.adjust_speed(1)

def look_up(player):
    # player.y += player.speed;
    #print("up has yet to be implemented")
    pass

def look_down(player):
    # TODO
    # player.y -= player.speed;
    pass

def console():
    # TODO
    key = get_key_pressed()
    print(key)
    print(int(key))


def do_jump(player):
    player.attempt_jump()

class player_inputs:
    # A test class to test viability of setting functions to variables
    s = 1
    d = function_name



# TODO

# Inputs are mapped using basically a map using two lists. Did not really think to use a dictionary before, will look into that.
key_strings = ("sprint","move_left","look_up","move_right","look_down","do_jump")
keymaps = (KEY_LEFT_SHIFT,KEY_A,KEY_W,KEY_D,KEY_S,KEY_SPACE)
key_action = (do_sprint,move_left,look_up,move_right,look_down,do_jump)

# Detects is any keys in keymaps are pressed, returns a binary number with each key having one bit dedicated to it
def detect_input():
    key_inputs = 0
    key_number = 0
    for key in keymaps:
        # Bit shifts each key value over by its ID so each key has its own bit in the return number
        key_inputs += is_key_down(key) << key_number
        key_number += 1

        # Test code to see if the keys were being pressed, kept in case anyone else needs it
        # print(key)
        # print(is_key_down(key))
        # print(key_inputs)
    return key_inputs

# Processes the input number provided by detect_inputs() and runs each function associated with each key
def parse_inputs(inputs: int,player):
    for function in key_action:
        if (inputs & 1): 
            function(player)
        inputs = inputs>>1
    # Move somewhere else later
    player.acceleration = .2
