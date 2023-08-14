import sys
import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config_data = config_service.get_config()  # Use the correct method to get the config data


class OptionsScreen:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode(
            (config_data['screen_width'], config_data['screen_height']))
        self.BG = pygame.image.load(config_data['background'])
        self.sound = pygame.mixer.Sound(config_data['menu_music'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config_data['screen_width'], config_data['screen_height']))

    def options(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            fullscreen = config_service.create_text_button((config_data['screen_width'] // 2, 240),
                                                           "Toggle Video", config_data['font_size'])
            audio_change = config_service.create_text_button((config_data['screen_width'] // 2, 320),
                                                             "Audio", config_data['font_size'])
            controls_change = config_service.create_text_button((config_data['screen_width'] // 2, 400),
                                                                "Controls", config_data['font_size'])
            back = config_service.create_text_button((config_data['screen_width'] // 2, 550),
                                                     "Back", config_data['font_size'])

            fullscreen.changeColor(options_mouse_pos)
            fullscreen.update(self.SCREEN)

            audio_change.changeColor(options_mouse_pos)
            audio_change.update(self.SCREEN)

            controls_change.changeColor(options_mouse_pos)
            controls_change.update(self.SCREEN)

            back.changeColor(options_mouse_pos)
            back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if fullscreen.checkForInput(options_mouse_pos):
                        pygame.display.toggle_fullscreen()
                    if back.checkForInput(options_mouse_pos):
                        return

            pygame.display.update()
