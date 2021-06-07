class Settings():
    """Class for storing all game settings Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship's settings.
        self.ship_limit = 3

        # Bullet's settings.
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0  # 255, 255, 255
        self.bullets_allowed = 3

        # Alien setting
        self.fleet_drop_speed = 10

        # Game acceleration rate
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes the settings that change during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction = 1 means movement to the right; and -1 - to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases the speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
