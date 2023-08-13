import sys
import pygame
from button import Button
from config.config_manager import ConfigService
from levels.level_1 import Level1Screen

config_service = ConfigService()
config = config_service.get_config()


class Character:
    def __init__(self):
        self.level1_screen = Level1Screen()
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config['screen_width'], config['screen_height']))


    def get_font(self, size):
        return pygame.font.Font(config['menu_font'], size)

    def create(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first


            LEVEL_1 = Button(pos=(640, 300),
                                  text_input="Level One", font=self.get_font(75),
                                  base_color=config['font_colour'],
                                  hovering_color=config['hovering_font_colour'])

            OPTIONS_BACK = Button(pos=(640, 460),
                                  text_input="BACK", font=self.get_font(75),
                                  base_color=config['font_colour'],
                                  hovering_color=config['hovering_font_colour'])

            LEVEL_1.changeColor(OPTIONS_MOUSE_POS)
            LEVEL_1.update(self.SCREEN)

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LEVEL_1.checkForInput(OPTIONS_MOUSE_POS):
                        self.level1_screen.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
