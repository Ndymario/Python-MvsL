'''
Authors: Nolan Y.
Descripion: File that will house any rendering functions
'''

'''
Planned functions:
 - Dynamic Image Loading
 - Sprite divider (take one image, and crate sprite objects with the image data. Reduces number of overall files needed)
'''

# Image instance: will handle loading and splitting the image as needed
class Image():
    def __init__(self, image_path, name) -> None:
        self.image_path = image_path(image_path)
        self.name = name

    # Function to load an image from a given path
    def load_image(self, image_path):
        # [TODO]
        pass

    # Print the image_path & name if print() is passed an Image
    def __str__(self) -> str:
        return "Image Path: {0}\nImage Name: {1}\n".format(self.image_path, self.name)

# Sprite instance: will represent any sprites drawn to the screen. Inherits from Image, as all Sprites are images with location information
class Sprite(Image):
    def __init__(self, image_path, name, x_pos, y_pos) -> None:
        super().__init__(image_path, name)
        self.x_pos = x_pos
        self.y_pos = y_pos

    # Print the image_path, name, x_pos, & y_pos if print() is passed an Image
    def __str__(self) -> str:
        return super().__str__() + "Sprite X-pos: {0}\nSprite Y-pos: {1}\n".format(self.x_pos, self.y_pos)