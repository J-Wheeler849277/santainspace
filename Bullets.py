import pygame, random
import math


class Bullet:
    def __init__(self, pos, path):
        self.x = pos[0]
        self.y = pos[1]
        self.path = path
        self.RGB = [random.randint(15, 255), random.randint(15, 255), random.randint(15, 255)]
        self.rect = pygame.Rect(0,0,0,0)

    def update(self):
        self.x += math.cos(self.path) * 4
        self.y += math.sin(self.path) * 4

        self.rect = pygame.Rect(self.x, self.y, 10, 10)