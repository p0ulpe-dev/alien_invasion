import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """Initializes the ship and sets its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the ship center.
        self.center = self.rect.centerx
        # Move flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position with the flag."""
        # The center attribute is updated, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Updating the rect attribute based on self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
