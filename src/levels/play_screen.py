import pygame
import sys
from button import Button
import pygame.mixer
import json
import os

# Initialize Pygame
pygame.mixer.init()
pygame.init()

class PlayScreen:
    def __init__(self):
        # Get the absolute path to the directory of this script
        script_directory = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_directory, 'options', 'config.json')

        with open(config_path) as json_file:
            self.data = json.load(json_file)


        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode((self.data['screen_width'], self.data['screen_height']))
        pygame.display.set_caption("Play Screen")

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("black")

            PLAY_TEXT = self.get_font(45).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460),
                               text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

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
