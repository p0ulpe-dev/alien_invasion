class Settings():
    """Class for storing all game settings Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship's settings.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet's settings.
        self.bullet_speed_factor = 3
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0  # 255, 255, 255
        self.bullets_allowed = 3

        # Alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means movement to the right; and -1 - to the left
        self.fleet_direction = 1
