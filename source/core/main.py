'''
Authors: Nolan Y.
Descripion: The (you guessed it) main file that gets ran for running Python MvsL
'''

# Import using * to we don't need to use "raylibpy." every time we wnt to do something
from raylibpy import *

def main():
    # Initialization:
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "Python MvsL")

    # Main game loop
    while not window_should_close():
        # Draw
        begin_drawing()

        clear_background(RAYWHITE)

        end_drawing()

    # Cleanup
    close_window()

if __name__ == '__main__':
    main()
