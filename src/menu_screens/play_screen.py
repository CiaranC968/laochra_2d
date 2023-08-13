import pygame
import sys
from menu_screens.load_screen import LoadScreen
from config.config_manager import ConfigService
from menu_screens.create_char import Character

config_service = ConfigService()
config = config_service.get_config()


class PlayScreen:
    def __init__(self):
        self.load = LoadScreen()
        self.config = config
        self.new_char = Character()  # Create an instance of the Character class
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))

    def get_font(self, size):
        return pygame.font.Font(config['menu_font'], size)

    def play(self):
        PLAY_GAME = config_service.create_button((config['screen_width'] // 2, 250),  "New Game", 75)
        PLAY_LOAD = config_service.create_button((config['screen_width'] // 2, 400), "Load Game", 75)
        PLAY_BACK = config_service.create_button((config['screen_width'] // 2, 550), "BACK", 75)

        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            PLAY_GAME.changeColor(PLAY_MOUSE_POS)
            PLAY_GAME.update(self.SCREEN)

            PLAY_LOAD.changeColor(PLAY_MOUSE_POS)
            PLAY_LOAD.update(self.SCREEN)

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_GAME.checkForInput(PLAY_MOUSE_POS):
                        self.new_char.create()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_LOAD.checkForInput(PLAY_MOUSE_POS):
                        self.load.load_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()
