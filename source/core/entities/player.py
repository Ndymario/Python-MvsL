'''
Authors: Nolan Y.
Descripion: File that will house any player functions
'''

'''
Planned functions:
 - Collisions
 - Intuitive player handling too allow for easy multiplayer
'''

from entity import Entity

class Player(Entity):
    def __init__(self) -> None:
        super().__init__()