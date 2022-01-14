import pygame, sys, threading
from Player import Player
from Bullets import Bullet
from Enemies import Enemy
import math



def game():

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SantaInSpace")

    #pygame.image.load("Example.GIF")d
    #screen.blit(texture, (x, y), (imageX, imageY, ImageW, ImageH))

    white = (255, 255, 255)
    #green = (0, 255, 0)
    green = (110, 254, 23)
    blue = (0, 0, 128)
    black = (20, 20, 20)

    R,G,B = 255,0,0
    x,y = 100,100

    player = Player([0, 0])
    bullets = []
    enemies = []

    gun_timer = 0

    score = 0

    while True:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():        
            if event.type == pygame.QUIT:       
                pygame.quit()                   
                sys.exit()   

        screen.fill((0,0,0))

        if len(enemies) <= 4:
            enemies.append(Enemy())


        player.update(key)

        gun_timer += 1
        if event.type == pygame.MOUSEBUTTONDOWN and gun_timer > 4:
            gun_timer = 0

            x,y = pygame.mouse.get_pos()
            path = math.atan2(player.y - y, player.x - x) 
            bullets.append(Bullet([player.x + (player.width/2), player.y], path + (6.2/2)))
            
            
        enemies_active = []
        for i in enemies:
            pygame.draw.rect(screen, (255,255,255), (i.x, i.y, i.width, i.height))
            
            if i.update(bullets):
                score += 1

            if not i.dead:
                enemies_active.append(i)
            

        enemies = enemies_active

        FONT = pygame.font.Font("GAME_FONT.ttf", 40)

        

        for i in bullets:
            pygame.draw.rect(screen, (i.RGB), (i.x, i.y, 10, 10))
            i.update()
            pygame.time.wait(100)

        pygame.draw.rect(screen, (R,G,B), (player.x,player.y, player.width, player.width))

        GAME_SCORE = FONT.render(str(f"Score: {score}"), True, green)
        
        print(f"Game Score: {score}")


        screen.blit(GAME_SCORE, (10, 0))

        clock.tick(120)
        pygame.display.update() 
        
        
x = threading.Thread(function=game)

x.start()