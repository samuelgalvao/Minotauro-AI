import pygame
import os, sys
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        path = r'C:\Users\Samuel\Documents\Estudos\Minotauro-AI\game\src\player_idle_01.png'
        # img = pygame.image.load(os.path.join(path)).convert()
        img = pygame.image.load(os.path.join(path)).convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey((0, 0, 0)) # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
# SETUP


def main():
    # CONSTANTS
    W_WIDTH, W_HEIGHT = 500, 500
    
    # Init
    pygame.init()
    screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    
    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill('black')
    
    # Player
    player = Player()   # spawn player
    player.rect.x = 0   # go to x
    player.rect.y = 0   # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
        
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        player_list.draw(background)
        
        screen.blit(background, (0, 0))
        pygame.display.update()
        
        clock.tick(60)
    
    
    
if __name__ == '__main__': main()

