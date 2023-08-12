import pygame
import sys
from button import Button
import pygame.mixer
import json

# Initialize Pygame
pygame.mixer.init()
pygame.init()

class OptionsScreen:
    def __init__(self):
        with open('config.json') as json_file:
            self.data = json.load(json_file)

        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode((self.data['screen_width'], self.data['screen_height']))
        pygame.display.set_caption("Options Screen")

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460),
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        return  # Return to the main menu

            pygame.display.update()


