import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for controlling bullets fired by a ship."""
    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the current position of the ship."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet at position (0,0) and assign the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # The bullet position is stored in real format.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen."""
        # Bullet position update in real format.
        self.y -= self.speed_factor
        # Updating the position of the rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Bullet output to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
