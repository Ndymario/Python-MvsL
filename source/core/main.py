'''
Authors: Nolan Y.
Descripion: The (you guessed it) main file that gets ran for running Python MvsL
'''

from raylibpy import init_window, set_target_fps, window_should_close, begin_drawing, clear_background, RAYWHITE, end_drawing, close_window
from input import console, parse_inputs, detect_input
from player import Player

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
