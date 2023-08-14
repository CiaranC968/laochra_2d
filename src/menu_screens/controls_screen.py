import sys
import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config_data = config_service.get_config()  # Use the correct method to get the config data


class ControlsScreen:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode(
            (config_data['screen_width'], config_data['screen_height']))
        self.BG = pygame.image.load(config_data['background'])
        self.sound = pygame.mixer.Sound(config_data['menu_music'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config_data['screen_width'], config_data['screen_height']))

    def controller(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            back = config_service.create_text_button((config_data['screen_width'] // 2, 550),
                                                     "Back", config_data['font_size'])

            back.changeColor(options_mouse_pos)
            back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.checkForInput(options_mouse_pos):
                        return

            pygame.display.update()
