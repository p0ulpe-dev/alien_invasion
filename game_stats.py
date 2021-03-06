class GameStats():
    """Statistics tracking for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initializing statistic."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        """Initializes statistics changing during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
