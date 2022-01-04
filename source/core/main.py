'''
Authors: Nolan Y.
Descripion: The (you guessed it) main file that gets ran for running Python MvsL
'''

# Import using * to we don't need to use "raylibpy." every time we wnt to do something
from raylibpy import *
from input import *
from player import *

# controls = player_inputs 

player = Player()

def main(): 
    # Initialization:
    do_console = False
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "Python MvsL")
    set_target_fps(60)
    # Main game loop
    while not window_should_close():
        
        # Test stuff
        # print(controls.s)
        # print(controls.d())
        
        # Draw
        begin_drawing()

        if (do_console): 
            # TODO
            console()
        else:
            parse_inputs(detect_input(),player)
            player.move_player()
        clear_background(RAYWHITE)
        player.draw_player()

        end_drawing()

    # Cleanup
    close_window()

if __name__ == '__main__':
    main()
