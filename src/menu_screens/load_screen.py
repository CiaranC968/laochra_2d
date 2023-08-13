import sys
import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()


class LoadScreen:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config['screen_width'], config['screen_height']))

    def get_font(self, size):
        return pygame.font.Font(config['menu_font'], size)

    def load_game(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            fullscreen = config_service.create_button((config['screen_width'] // 2, 250), "Load Game", config['font_size'], None)
            options_back = config_service.create_button((config['screen_width'] // 2, 550), "Back", config['font_size'], None)

            fullscreen.changeColor(OPTIONS_MOUSE_POS)
            fullscreen.update(self.SCREEN)

            options_back.changeColor(OPTIONS_MOUSE_POS)
            options_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
