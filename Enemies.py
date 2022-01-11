import pygame, random

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 550)
        self.y = -50
        self.speed = 1
        self.dead = False
        self.rect = pygame.Rect(0,0,0,0)
        self.width = 30
        self.height = 50

    def update(self, bullets):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for i in bullets:
            if self.rect.colliderect(i.rect):
                self.dead = True
                return True

        if self.y > 600:
            self.dead = True
        
        return False
            

