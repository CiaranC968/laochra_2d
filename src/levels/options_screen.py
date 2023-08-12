import sys
import pygame
import pygame.mixer
from button import Button
from config.config_manager import ConfigService

config = ConfigService()
# Initialize Pygame
pygame.mixer.init()
pygame.init()

class OptionsScreen:
    def __init__(self):
        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode((config.get_config()['screen_width'], config.get_config()['screen_height']))
        pygame.display.set_caption("Options Screen")
        self.BG = pygame.image.load("images/main_background.jpg")
        self.BG = pygame.transform.scale(self.BG, (config.get_config()['screen_width'], config.get_config()['screen_height']))

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(pos=(640, 460),
                                  text_input="BACK", font=self.get_font(75),
                                  base_color=config.get_config()['font_colour'],
                                  hovering_color=config.get_config()['hovering_font_colour'])

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
