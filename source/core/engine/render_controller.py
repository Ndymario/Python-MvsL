'''
Authors: Nolan Y.
Descripion: File that will house any rendering functions
'''

'''
Planned functions:
 - Dynamic Image Loading
 - Sprite divider (take one image, and crate sprite objects with the image data. Reduces number of overall files needed)
'''

import json

# Image instance: will handle loading and splitting the image as needed
class Image():
    def __init__(self, image_path, name) -> None:
        self.image_path = image_path
        self.name = name

    # Take the input image and generate a list of split images using the provided JSON file
    def create_sheet(self, image_path, json_path):
        # Store each SET in a Dictionary
        set_dict = {}

        # Flags to determine where the import fails
        incorrect_meta_data = False

        # Try to open and parse the passed json file
        with open(json_path, "r") as file:
            sheet_info = json.load(file)

            # Fetch Sheet "meta data", then store it in a list
            creator = sheet_info.get("creator")
            name = sheet_info.get("name")
            set_count = sheet_info.get("set_count")
            border_color = sheet_info.get("border_color")
            is_playable = sheet_info.get("is_playable")
            has_sounds = sheet_info.get("has_sounds")
            has_keys = sheet_info.get("has_keys")
            meta_data = [creator, name, set_count, border_color, is_playable, has_sounds, has_keys]

            # All meta data should exist. If any part doesn't, mark a flag and abandon the import process
            for data in meta_data:
                if data == None:
                    incorrect_meta_data = True
        
        if incorrect_meta_data:
            return True
        else:
            return set_dict

    # Function to load an image from a given path
    def load_image(self, image_name):
        # [TODO] Load image from given image path
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