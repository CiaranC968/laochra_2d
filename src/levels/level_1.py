import pygame
import sys
from button import Button

from config.config_manager import ConfigService


# Initialize Pygame
pygame.mixer.init()
pygame.init()

config_service = ConfigService()
config = config_service.get_config()


class Level1Screen:
    def __init__(self):
        self.sound = pygame.mixer.Sound(config['level_1_music'])
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['level_1'])
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        PLAY_BACK = Button(pos=(config['screen_width'] // 2, config['screen_height'] - 100),
                           text_input="BACK", font=self.get_font(75),
                           base_color=config['font_colour'],
                           hovering_color=config['hovering_font_colour'])

        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

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
            pygame.mixer.Sound.play(self.sound)
            self.sound.set_volume(config['volume'])


