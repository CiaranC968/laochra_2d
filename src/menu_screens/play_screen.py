import pygame
import sys
from button import Button

from config.config_manager import ConfigService

# Initialize Pygame
pygame.mixer.init()
pygame.init()

config_service = ConfigService()
config = config_service.get_config()


class PlayScreen:
    def __init__(self):
        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        pygame.display.set_caption("Play Screen")
        self.BG = pygame.image.load("images/main_background.jpg")
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        PLAY_GAME = Button(pos=(config['screen_width'] // 2, 250),
                           text_input="New Game", font=self.get_font(75),
                           base_color=config['font_colour'],
                           hovering_color=config['hovering_font_colour'])

        PLAY_LOAD = Button(pos=(config['screen_width'] // 2, 400),
                           text_input="Load", font=self.get_font(75),
                           base_color=config['font_colour'],
                           hovering_color=config['hovering_font_colour'])

        PLAY_BACK = Button(pos=(config['screen_width'] // 2, 550),
                           text_input="BACK", font=self.get_font(75),
                           base_color=config['font_colour'],
                           hovering_color=config['hovering_font_colour'])

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
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()

