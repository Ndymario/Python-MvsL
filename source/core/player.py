

from typing import Any
from raylibpy import BLACK, draw_circle


class Player:
    def __init__(self) -> None:
        pass

    x = 0
    y = 0
    speed = 0
    max_speed = 1.3
    acceleration = .2
    vertical_speed = 0
    gravity = 1.5
    friction = .15

    def draw_player(self):
        # We will use screenheight - y when drawing so that way Y starts at the bottom of the screen and goes up when positive
        draw_circle(self.x,448 - self.y,2,BLACK)

    def adjust_speed(self, amount):
        # Change speed         
        self.speed += self.acceleration * amount

        # Cap Speed
        if (self.speed > self.max_speed):
            self.speed = self.max_speed
        if (self.speed < -self.max_speed):
            self.speed = -self.max_speed

    def apply_friction(self):
        if (self.speed > 0):
            if (self.speed - self.friction < 0):
                self.speed = 0
            else:
                self.speed -= self.friction
        elif (self.speed < 0):
            if (self.speed + self.friction > 0):
                self.speed = 0
            else:
                self.speed += self.friction
        
    def attempt_jump(self):
        if (self.y == 0):
            self.y = 150

    def move_player(self):
        self.x += self.speed
        self.apply_friction()
        if (self.y > 0):
            self.y -= self.gravity
        else:
            self.y = 0