import sys

import pygame


def check_events(ship):
    """Handles keys and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            ship.moving_right = False


def update_screen(ai_settings, screen, ship, alien):
    # The screen is redrawn on each pass of the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
    pygame.display.update()