import sys
import pygame
from config.config_manager import ConfigService
from levels.level_1 import Level1Screen

config_service = ConfigService()
config = config_service.get_config()


class Character:
    def __init__(self):
        self.sound = pygame.mixer.Sound(config['menu_music'])
        self.level1_screen = Level1Screen()
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG,
                                         (config['screen_width'], config['screen_height']))

    def create(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            level_1 = config_service.create_text_button((config['screen_width'] // 2, 300),
                                                        "Create Character", config['font_size'])
            options_back = config_service.create_text_button((config['screen_width'] // 2, 550),
                                                             "Back", config['font_size'])

            level_1.changeColor(options_mouse_pos)
            level_1.update(self.SCREEN)

            options_back.changeColor(options_mouse_pos)
            options_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if level_1.checkForInput(options_mouse_pos):
                        pygame.mixer.stop()
                        self.level1_screen.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(options_mouse_pos):
                        return  # Return to the main menu

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)
