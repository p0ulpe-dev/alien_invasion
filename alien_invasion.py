import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


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
    ship = Ship(ai_settings, screen)
    alien = Alien(screen)

    # Starting the main game loop.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, alien)

    # Displays the last drawn screen.
    pygame.display.flip()


run_game()
