from configparser import ConfigParser   

config = ConfigParser()
config.read('src/config/config.ini')

class ConfigService:
    def __init__(self):
        screen = config["Screen"]
        font = config["Font"]
        images = config['Images']
        music = config['Music']

        # Initialize with default configuration values
        self.config = {
            'screen_width': int(screen["screen_width"]),
            'screen_height': int(screen["screen_height"]),
            'font_colour': font["font_colour"],
            'hovering_font_colour': font["hovering_font_colour"],
            'background': images['background'],
            'menu_music': music['menu_music'],
            'level_1': images["level_1"],
            'menu_font': font["menu_font"],
            'level_1_music': music['level_1_music'],
            'volume': float(music['volume'])
            # Add more configuration keys and values as needed.
        }

    def get_config(self):
        return self.config
