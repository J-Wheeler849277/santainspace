import pygame

class Player:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.width = 100
        self.speed = 4
        self.jumping = False
        self.jump_speed = 5

    def update(self, key):
        

        

        if key[pygame.K_a]:
            self.x -= self.speed
        elif key[pygame.K_d]:
            self.x += self.speed



        if self.y <= 600 - self.width and not self.jumping:
            self.y += 3
        
        elif self.jumping:
            pass
        