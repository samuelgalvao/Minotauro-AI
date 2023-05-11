import pygame
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))  # Create a player image
        self.image.fill((255, 255, 255))  # Fill it with red color
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.rect.center = (width // 2, height // 2)  # Set initial position

    def update(self, speed):
        keys = pygame.key.get_pressed()  # Get the pressed keys
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed  # Move left
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed  # Move right
        if keys[pygame.K_UP]:
            self.rect.y -= speed  # Move up
        if keys[pygame.K_DOWN]:
            self.rect.y += speed  # Move down

    def draw(self):
        screen.blit(self.image, self.rect)  # Draw the player on the screen

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update(0.1)  # Update player position
    screen.fill((0, 0, 0))  # Clear the screen
    player.draw()  # Draw the player
    pygame.display.flip()  # Update the display
