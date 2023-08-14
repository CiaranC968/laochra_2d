from configparser import ConfigParser
import pygame
from menu_objects.text_button import Button


class ConfigService:
    def __init__(self):
        self.path = 'config/config.ini'
        self.config_parser = ConfigParser()
        self.config_parser.read(self.path)
        screen = self.config_parser["Screen"]
        font = self.config_parser["Font"]
        images = self.config_parser['Images']
        music = self.config_parser['Music']
        player = self.config_parser['Player']
        controls = self.config_parser['Controls']

        # Initialize with default configuration values
        self.config = {
            'screen_width': int(screen["screen_width"]),
            'screen_height': int(screen["screen_height"]),
            'frame_rate': int(screen["frame_rate"]),
            'ground_level': int(screen["ground_level"]),
            'font_colour': font["font_colour"],
            'font_size': int(font["font_size"]),
            'hovering_font_colour': font["hovering_font_colour"],
            'background': images['background'],
            'menu_music': music['menu_music'],
            'level_1': images["level_1"],
            'menu_font': font["menu_font"],
            'level_1_music': music['level_1_music'],
            'volume': float(music['volume']),
            'player_width': int(player['player_width']),
            'player_height': int(player['player_height']),
            'player_left': controls['player_left'],
            'player_right': controls['player_right'],
            'player_jump': controls['player_jump'],
            'player_attack': controls['player_attack']
            # Add more configuration keys and values as needed.
        }

    def get_config(self):
        return self.config

    def update_and_write(self, section, key, value):
        self.config_parser[section][key] = value
        with open(self.path, 'w') as configfile:
            self.config_parser.write(configfile)

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
"""
This is used to load and set data from config.ini, 
In future I may change it so that it loads other ini files
"""