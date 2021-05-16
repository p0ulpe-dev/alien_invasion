import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initializes the attributes of the button."""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Button properties.
        self.width, self.height = 100, 50
        self.button_color = (89, 0, 179)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Creating a button and screen alignment.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message, create onle once
        self.perp_msg(msg)

    def perp_msg(self, msg):
        """Converts the msg to a rectangle and aligns the text in the center"""
        self.msg_image = self.font.render(msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Displays an empty button and displays a message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
