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

    def play(self):
        new_game = config_service.create_text_button((config['screen_width'] // 2, 300),
                                                      "New Game", config['font_size'])
        load_game = config_service.create_text_button((config['screen_width'] // 2, 400),
                                                      "Load Game", config['font_size'])
        back = config_service.create_text_button((config['screen_width'] // 2, 550),
                                                      "BACK", config['font_size'])

        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            new_game.changeColor(play_mouse_pos)
            new_game.update(self.SCREEN)

            load_game.changeColor(play_mouse_pos)
            load_game.update(self.SCREEN)

            back.changeColor(play_mouse_pos)
            back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game.checkForInput(play_mouse_pos):
                        self.new_char.create()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if load_game.checkForInput(play_mouse_pos):
                        self.load.load_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back.checkForInput(play_mouse_pos):
                        return  # Return to the main menu

            pygame.display.update()
