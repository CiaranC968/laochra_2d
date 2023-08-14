import sys
import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()


class OptionsScreen:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['background'])
        self.sound = pygame.mixer.Sound(config['menu_music'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config['screen_width'], config['screen_height']))


    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            fullscreen = config_service.create_text_button((config['screen_width'] // 2, 250),
                                                           "Toggle Fullscreen", config['font_size'])
            mute = config_service.create_text_button((config['screen_width'] // 2, 300),
                                                           "Toggle Mute Sounds", config['font_size'])
            options_back = config_service.create_text_button((config['screen_width'] // 2, 550),
                                                             "Back", config['font_size'])

            fullscreen.changeColor(OPTIONS_MOUSE_POS)
            fullscreen.update(self.SCREEN)

            mute.changeColor(OPTIONS_MOUSE_POS)
            mute.update(self.SCREEN)

            options_back.changeColor(OPTIONS_MOUSE_POS)
            options_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if fullscreen.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.display.toggle_fullscreen()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mute.checkForInput(OPTIONS_MOUSE_POS):
                        if pygame.mixer.music:
                            pygame.mixer.pause()
                        else:
                            pygame.mixer.Sound.play(self.sound)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
