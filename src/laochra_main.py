import pygame
import sys
from button import Button
import pygame.mixer
import os
from levels.play_screen import PlayScreen
from config.config_manager import ConfigService
from levels.options_screen import OptionsScreen

config = ConfigService()

play_screen = PlayScreen()
settings = OptionsScreen()


# Initialize Pygame
pygame.mixer.init()
pygame.init()

# Get the absolute path to the directory of this script
script_directory = os.path.dirname(os.path.abspath(__file__))

sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
SCREEN = pygame.display.set_mode((config.get_config()['screen_width'], config.get_config()['screen_height']))
pygame.display.set_caption("Menu")


def get_font(size):
    return pygame.font.Font("fonts/MedievalMystery.ttf", size)


# Load the background image
BG = pygame.image.load("images/main_background.jpg")
BG = pygame.transform.scale(BG, (config.get_config()['screen_width'], config.get_config()['screen_height']))  # Scale image to fit screen


def main_menu():
    while True:
        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(config.get_config()['screen_width'] // 2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play_Rect.png"), pos=(config.get_config()['screen_width'] // 2, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("images/Play_Rect.png"), pos=(config.get_config()['screen_width'] // 2, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Play_Rect.png"), pos=(config.get_config()['screen_width'] // 2, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_screen.play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings.options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        pygame.display.update()
        pygame.mixer.Sound.play(sound)
        sound.set_volume(.8)


if __name__ == "__main__":
    main_menu()
