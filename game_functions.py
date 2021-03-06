import sys
from time import sleep

import pygame
from pygame.constants import MOUSEBUTTONDOWN
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, stats, sb,
                         screen, ship, aliens, bullets):
    """Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif not stats.game_active and event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if the maximum has not yet been reached."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Reacts when keys are released."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb,
                 play_button, ship, aliens, bullets):
    """Handles keys and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, sb,
                                 screen, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen,
                              stats, sb, play_button,
                              ship, aliens, bullets,
                              mouse_x, mouse_y)


def check_play_button(ai_settings, screen,
                      stats, sb, play_button,
                      ship, aliens, bullets,
                      mouse_x, mouse_y):
    """Starts a new game when you click Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # Reset game settings.
        ai_settings.initialize_dynamic_settings()


def start_game(ai_settings, screen,
               stats, sb, ship, aliens, bullets):
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
    # Reset stats
    stats.reset_stats()
    stats.game_active = True
    # Resetting the scores and level images.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    # Clean groups of aliens and bullets
    aliens.empty()
    bullets.empty()
    # Creating a new fleet and placement of the ship to the center.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship,
                  bullets, aliens, play_button):
    """The screen is redrawn on each pass of the loop."""
    screen.fill(ai_settings.bg_color)

    # All bullets are displayed behind the ship and alien images.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Displays the score
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.update()

    # Displays the last drawn screen.
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb,
                   ship, aliens, bullets):
    """Updates bullet positions and destroys old bullets."""
    # Update bullets position.
    bullets.update()

    # Deleting old bullets.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  ship, aliens, bullets):
    """Determing of collisions bullets with aliens."""
    # Deleting bullets and aliens participating in collisions.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            # Update the score and high score.
            sb.prep_score()
            check_high_score(stats, sb)

    if len(aliens) == 0:
        # Destroy bullets and creating new fleet
        bullets.empty()
        ai_settings.increase_speed()
        # Increasing the level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_alians_x(ai_settings, alien_width):
    """Calculates the number of aliens in a row."""
    avalabel_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(avalabel_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates an alien and places it in a row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + ((2 * alien_width) * alien_number)
    alien.rect.y = alien.rect.height + ((2 * alien.rect.height) * row_number)
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creating fleet of aliens"""
    # Create an alien and calculate the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_alians_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
                                ai_settings,
                                ship.rect.height,
                                alien.rect.height
                                )

    # Creating first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in a row.
            create_alien(
                        ai_settings,
                        screen,
                        aliens,
                        alien_number,
                        row_number
                        )


def get_number_rows(ai_settings, ship_height, alien_height):
    """Specifies the number of rows that fit on the screen."""
    avalabel_space_y = (ai_settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(avalabel_space_y / (2 * alien_height))
    return number_rows  # = 4


def check_fleet_edges(ai_settings, aliens):
    """Reacts when the alien reaches the edge of the screen."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Reacts when the alien reaches the edge of the screen."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """
    Checks if the fleet has reached the edge of the screen,
    and then updates the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check collisions alien-ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # Checking aliens who have come to the bottom edge of the screen.
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Determing of collisions aliens with ship."""
    if stats.ships_left > 0:
        # Reducing ship_left
        stats.ships_left -= 1

        # Update game information.
        sb.prep_ships()

        # Clean groups of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Creating a new fleet and placement of the ship to the center.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(False)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Checks whether the aliens get to the lower edge of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    """Checks if a new record has appeared."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
