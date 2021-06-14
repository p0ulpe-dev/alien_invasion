import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button


def run_game():
    # Initializes pygame, settings and a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    win_icon = pygame.image.load('images/alien_invasion_icon.png')
    pygame.display.set_icon(win_icon)

    # Create "PLay" button
    play_button = Button(ai_settings, screen, "PLAY")

    # Creating a GameStats and Scorebord instances for storing game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Creation of the ship, group of bullets and group of aliens.
    ship = Ship(ai_settings, screen)
    # Creating group for bullets.
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Starting the main game loop.
    while True:
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb,
                             screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         bullets, aliens, play_button)


run_game()
