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

    def get_font(self, size):
        return pygame.font.Font(config['menu_font'], size)

    def create(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            LEVEL_1 = config_service.create_button((config['screen_width'] // 2, 250), "Level One", config['font_size'], None)
            OPTIONS_BACK = config_service.create_button((config['screen_width'] // 2, 550), "Back", config['font_size'], None)

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
                        pygame.mixer.stop()
                        self.level1_screen.play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)
