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



    def load_game(self):
        while True:
            load_mouse_pos = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            fullscreen = config_service.create_text_button((config['screen_width'] // 2, 250),
                                                           "Load Game", config['font_size'])
            options_back = config_service.create_text_button((config['screen_width'] // 2, 550),
                                                             "Back", config['font_size'])

            fullscreen.changeColor(load_mouse_pos)
            fullscreen.update(self.SCREEN)

            options_back.changeColor(load_mouse_pos)
            options_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(load_mouse_pos):
                        return  # Return to the main menu

            pygame.display.update()
