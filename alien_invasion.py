import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
# Создание поверхности
# surf_screen = pygame.Surface(
#   (ai_settings.screen_width, ai_settings.screen_height))
# Окраска поверхности
# surf_screen.fill((ai_settings.bg_color))
# Помещение поверхности на другую поверхность в нашем случае на сам экран
# screen.blit(surf_screen, (0, 0))
# pygame.display.update()


def run_game():
    # Initializes pygame, settings and a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    win_icon = pygame.image.load('images/alien_invasion_icon.png')
    pygame.display.set_icon(win_icon)
    # Creation of the ship.
    ship = Ship(screen)
    alien = Alien(screen)

    # Starting the main game loop.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, alien)

    # Displays the last drawn screen.
    pygame.display.flip()


run_game()
