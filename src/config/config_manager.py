class ConfigService:
    def __init__(self):
        # Initialize with default configuration values
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
            'volume': .8

            # Add more configuration keys and values as needed
        }

    def get_config(self):
        return self.config
