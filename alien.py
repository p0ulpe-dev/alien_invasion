import pygame


class Alien():
    def __init__(self, screen):
        """Initializes the alien and sets its starting position."""
        self.screen = screen

    # Можно сделать цыкл который будет создавать пришельцев
    # с разными скинами.
        # Loading a alien image and getting a rectangle.
        self.image = pygame.image.load('images/aliens/alien1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Each new alien appears at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draws the alien at the current position."""
        self.screen.blit(self.image, self.rect)
