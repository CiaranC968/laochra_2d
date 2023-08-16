import pygame
import sys
from menu_screens.new_game_load_screen import PlayScreen
from menu_screens.options_screen import OptionsScreen, config_service
import math


class MainMenu:
    def __init__(self, config):
        pygame.mixer.init()  # Initialize mixer before using Sound
        pygame.init()  # Initialize pygame
        pygame.display.set_caption('Laochra')

        self.clock = pygame.time.Clock()
        self.menu_mouse_pos = None
        self.config = config
        self.play_screen = PlayScreen()
        self.settings = OptionsScreen()
        self.sound = pygame.mixer.Sound(config['menu_music'])
        self.sound.set_volume(self.config['volume'])  # Adjust the volume
        pygame.mixer.Sound.play(self.sound)  # Start playing the music

        self.SCREEN = pygame.display.set_mode((config['screen_width'], config['screen_height']))
        self.FONT = pygame.font.Font(config['menu_font'], 100)
        self.BG = pygame.image.load(config['background'])
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))

        self.play_button = config_service.create_text_button((config['screen_width'] // 2, 300), "Play",
                                                             config['font_size'])
        self.options_button = config_service.create_text_button((config['screen_width'] // 2, 400), "Options",
                                                                config['font_size'])
        self.quit_button = config_service.create_text_button((config['screen_width'] // 2, 550), "Quit",
                                                             config['font_size'])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.cleanup()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.checkForInput(self.menu_mouse_pos):
                    self.play_screen.play()
                if self.options_button.checkForInput(self.menu_mouse_pos):
                    self.settings.options()
                if self.quit_button.checkForInput(self.menu_mouse_pos):
                    self.cleanup()

    def cleanup(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            self.menu_mouse_pos = pygame.mouse.get_pos()
            self.SCREEN.blit(self.BG, (0, 0))
            bg_width = self.BG.get_width()

            tiles = math.ceil(self.config['screen_width'] / bg_width)

            main_menu_text = self.FONT.render("LAOCHRA", True, "#b68f40")
            text_width, text_height = main_menu_text.get_size()

            text_x = (self.config['screen_width'] - text_width) // 2 + 10
            text_y = self.config['screen_height'] // 2 - text_height - 180  # Adjust the value as needed

            self.SCREEN.blit(main_menu_text, (text_x, text_y))

            for button in [self.play_button, self.options_button, self.quit_button]:
                button.changeColor(self.menu_mouse_pos)
                button.update(self.SCREEN)

            pygame.display.update()
            self.clock.tick(self.config['frame_rate'])
            self.handle_events()


def main():
    config = config_service.get_config()
    main_menu = MainMenu(config)
    main_menu.run()


if __name__ == "__main__":
    main()
