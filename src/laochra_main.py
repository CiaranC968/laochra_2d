import pygame
import sys
from button import Button
from levels.play_screen import PlayScreen

from levels.options_screen import OptionsScreen
from config.config_manager import ConfigService
config = ConfigService()


class MainMenu:
    def __init__(self, config):
        self.menu_mouse_pos = None
        self.config = config
        self.play_screen = PlayScreen()
        self.settings = OptionsScreen()
        self.sound = pygame.mixer.Sound("sounds/Celtic_01_main_menu.mp3")
        self.SCREEN = pygame.display.set_mode((config['screen_width'], config['screen_height']))
        self.FONT = pygame.font.Font("fonts/MedievalMystery.ttf", 100)
        self.BG = pygame.image.load("images/main_background.jpg")
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))

        self.play_button = Button(
                                  pos=(config['screen_width'] // 2, 250),
                                  text_input="PLAY", font=self.FONT, base_color=config['font_colour'],
                                  hovering_color=config['hovering_font_colour'])
        self.options_button = Button(
                                     pos=(config['screen_width'] // 2, 400),
                                     text_input="OPTIONS", font=self.FONT, base_color=config['font_colour'],
                                     hovering_color=config['hovering_font_colour'])
        self.quit_button = Button(
                                  pos=(config['screen_width'] // 2, 550),
                                  text_input="QUIT", font=self.FONT, base_color=config['font_colour'],
                                  hovering_color=config['hovering_font_colour'])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.checkForInput(self.menu_mouse_pos):
                    self.play_screen.play()
                if self.options_button.checkForInput(self.menu_mouse_pos):
                    self.settings.options()
                if self.quit_button.checkForInput(self.menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

    def run(self):
        while True:
            self.menu_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))

            main_menu_text = self.FONT.render("LAOCHRA", True, "#b68f40")
            text_width, text_height = main_menu_text.get_size()

            text_x = (self.config['screen_width'] - text_width) // 2 + 10
            text_y = self.config['screen_height'] // 2 - text_height - 180 # Adjust the value as needed

            self.SCREEN.blit(main_menu_text, (text_x, text_y))

            for button in [self.play_button, self.options_button, self.quit_button]:
                button.changeColor(self.menu_mouse_pos)
                button.update(self.SCREEN)

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)
            self.sound.set_volume(.8)

            self.handle_events()


def main():
    pygame.mixer.init()
    pygame.init()

    config_service = ConfigService()
    config = config_service.get_config()

    pygame.display.set_caption("Menu")

    main_menu = MainMenu(config)
    main_menu.run()


if __name__ == "__main__":
    main()

