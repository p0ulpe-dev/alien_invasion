import pygame


class Ship():
    def __init__(self, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen

        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Move flag.
        self.moving_right = False

    def update(self):
        """Updates the ship's position with the flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
