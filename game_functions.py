import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reacts to keystrokes."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def check_events(ai_settings, screen, ship, bullets):
    """Handles keys and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """The screen is redrawn on each pass of the loop."""
    screen.fill(ai_settings.bg_color)
    # All bullets are displayed behind the ship and alien images.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.update()


def update_bullets(aliens, bullets):
    """Updates bullet positions and destroys old bullets."""
    # Update bullets position.
    bullets.update()

    # Deleting old bullets.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    # Check for alien hits.
    # If a hit is detected, remove the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


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


def update_aliens(ai_settings, aliens):
    """
    Checks if the fleet has reached the edge of the screen,
    and then updates the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
