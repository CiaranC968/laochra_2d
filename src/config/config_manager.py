import pygame

from menu_objects.text_button import Button


class ConfigService:
    def __init__(self):
        # Configuration values
        self.config = {
            'screen_width': 1280,
            'screen_height': 700,
            'font_colour': 'black',
            'hovering_font_colour': '#b68f40',
            'background': 'images/main_background.png',
            'menu_music': 'sounds/Celtic_01_main_menu.mp3',
            'level_1': 'images/level_1.png',
            'menu_font': 'fonts/MedievalMystery.ttf',
            'level_1_music': 'sounds/Celtic_02_level_1.mp3',
            'volume': .8,
            'font_size': 75,
            'fps': 60

            # Add more configuration keys and values as needed.
        }

    def create_text_button(self, pos, text, font_size):
        return Button(image=None,
                      pos=pos,
                      text_input=text, font=self.get_font(font_size),
                      base_color=self.config['font_colour'],
                      hovering_color=self.config['hovering_font_colour'])

    def create_image_bg_button(self, pos, text, font_size, image_path):
        image = pygame.image.load(image_path)
        return Button(image=image,
                      pos=pos,
                      text_input=text, font=self.get_font(font_size),
                      base_color=self.config['font_colour'],
                      hovering_color=self.config['hovering_font_colour'])

    def get_font(self, size):
        return pygame.font.Font(self.config['menu_font'], size)

    def get_config(self):
        return self.config
