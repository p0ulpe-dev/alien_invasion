class Settings():
    """Class for storing all game settings Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (77, 37, 84)

        # Ship's settings.
        self.ship_speed_factor = 1.5
