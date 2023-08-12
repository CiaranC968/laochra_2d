import pygame
import sys
from button import Button
import pygame.mixer

from config.config_manager import ConfigService

config = ConfigService()

# Initialize Pygame
pygame.mixer.init()
pygame.init()

class PlayScreen:
    def __init__(self):
        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode((config.get_config()['screen_width'], config.get_config()['screen_height']))
        pygame.display.set_caption("Play Screen")

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            PLAY_TEXT = self.get_font(45).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(pos=(640, 460),
                               text_input="BACK", font=self.get_font(75), base_color=config.get_config()['font_colour'], hovering_color=config.get_config()['hovering_font_colour'])

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
