import pygame
import math


class Bullet:
    def __init__(self, direction):
        self.x = 0
        self.y = 0
        self.direction = direction

    def update(self):
        self.x -= math.cos(self.direction)
        self.y -= math.sin(self.direction) 