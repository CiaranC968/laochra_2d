import pygame
import sys

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

        play_back = config_service.create_text_button((config['screen_width'] // 2, 550), "BACK", config['font_size'])

        while True:
            play_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            play_back.changeColor(play_mouse_pos)
            play_back.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_back.checkForInput(play_mouse_pos):
                        pygame.mixer.stop()
                        return  # Return to the main menu

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)
