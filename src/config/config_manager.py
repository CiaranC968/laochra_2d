from configparser import ConfigParser   

config = ConfigParser()
config.read('src/config/config.ini')

class ConfigService:
    def __init__(self):
        screen = config["Screen"]
        font = config["Font"]
        images = config['Images']
        music = config['Music']
        player = config['Player']

        # Initialize with default configuration values
        self.config = {
            'screen_width': int(screen["screen_width"]),
            'screen_height': int(screen["screen_height"]),
            'frame_rate': int(screen["frame_rate"]),
            'ground_level' : int(screen["ground_level"]),
            'font_colour': font["font_colour"],
            'font_size': int(font["font_size"]),
            'hovering_font_colour': font["hovering_font_colour"],
            'background': images['background'],
            'menu_music': music['menu_music'],
            'level_1': images["level_1"],
            'level_1_1': images["level_1"],
            'menu_font': font["menu_font"],
            'level_1_music': music['level_1_music'],
            'volume': float(music['volume']),
            'player_width':int(player['player_width']),
            'player_height':int(player['player_height']),
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
