class Settings():
    """Class for storing all game settings Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (77, 37, 84)

        # Ship's settings.
        self.ship_speed_factor = 1.5

        # Bullet's settings.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
