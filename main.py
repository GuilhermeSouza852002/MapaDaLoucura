import pygame, sys
from settings import *
from level import Level
from game_data import level_0

# Setup do pygame
#iniciação do jogo
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height)) #Definindo a janela de exibição
pygame.display.set_caption('Praise the Sun') #nome do display
clock = pygame.time.Clock()
level = Level(level_0, screen)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
    screen.fill('black')
    level.run()                    
    pygame.display.update()
    clock.tick(fps)  