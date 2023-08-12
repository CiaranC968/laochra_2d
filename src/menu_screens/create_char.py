import sys
import pygame
from button import Button
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()
pygame.init()


class Character:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        pygame.display.set_caption("Options Screen")
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config['screen_width'], config['screen_height']))

    def set_difficulty(value, difficulty):
        print(value)
        print(difficulty)

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def create(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first


            OPTIONS_BACK = Button(pos=(640, 460),
                                  text_input="BACK", font=self.get_font(75),
                                  base_color=config['font_colour'],
                                  hovering_color=config['hovering_font_colour'])


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
