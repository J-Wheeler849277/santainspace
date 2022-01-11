import pygame, random
import math


class Bullet:
    def __init__(self, pos, path):
        self.x = pos[0]
        self.y = pos[1]
        self.path = path
        self.RGB = [random.randint(15, 255), random.randint(15, 255), random.randint(15, 255)]

    def update(self):
        self.x += math.cos(self.path) * 4
        self.y += math.sin(self.path) * 4