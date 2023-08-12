class ConfigService:
    def __init__(self):
        # Initialize with default configuration values
        self.config = {
            'screen_width': 1280,
            'screen_height': 700
            # Add more configuration keys and values as needed
        }

    def get_config(self):
        return self.config
