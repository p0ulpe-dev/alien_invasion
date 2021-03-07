import pygame
from pygame.sprite import Sprite
from random import randrange


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Initializes the alien and sets its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading random a alien image and getting a rectangle.
        aliens_skins = [
                'images/aliens/alien1.png',
                'images/aliens/alien2.png',
                'images/aliens/alien3.png',
                'images/aliens/alien4.png',
                'images/aliens/alien5.png'
                ]
        random_skin = randrange(0, len(aliens_skins))
        skin_location = str(aliens_skins[random_skin])
        self.image = pygame.image.load(skin_location)
        self.rect = self.image.get_rect()
        # self.screen_rect = self.screen.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draws the alien at the current position."""
        self.screen.blit(self.image, self.rect)
