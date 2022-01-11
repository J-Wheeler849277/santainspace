import pygame, sys
from Player import Player
from Bullets import Bullet
import math

pygame.init()

clock = pygame.time.Clock()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")

#pygame.image.load("Example.GIF")
#screen.blit(texture, (x, y), (imageX, imageY, ImageW, ImageH))


R,G,B = 255,0,0
x,y = 100,100

player = Player([0, 0])
bullets = []

while True:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():        
        if event.type == pygame.QUIT:       
            pygame.quit()                   
            sys.exit()   

    screen.fill((0,0,0))

     
    player.update(key)

    if key[pygame.K_b]:
        x,y = pygame.mouse.get_pos()
        
        path = math.atan2(x - player.x, y - player.y)
        bullets.append(path)
        

    

    pygame.draw.rect(screen, (R,G,B), (player.x,player.y, player.width, player.width))



    clock.tick(120)
    pygame.display.update() 