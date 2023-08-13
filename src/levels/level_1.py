import pygame
import sys
from config.config_manager import ConfigService
from character_sprites.char_class import Player

# Initialize Pygame
pygame.mixer.init()
pygame.init()

config_service = ConfigService()
config = config_service.get_config()

class Level1Screen:
    def __init__(self):
        self.sound = pygame.mixer.Sound(config['level_1_music'])
        self.SCREEN = pygame.display.set_mode(
            (config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['level_1']).convert()
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))
        self.bg_x = 0  # Initial background position
        self.bg_y = 0
        self.player = Player(100, 450)

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        clock = pygame.time.Clock()  # Create a clock object for controlling frame rate

        # Background scrolling variables
        bg_scroll = 0
        bg_speed = 1  # Adjust this value to control scrolling speed
        bg_width = self.BG.get_width()

        while True:
            play_mouse_pos = pygame.mouse.get_pos()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()
                moving_right = True
                moving_left = False
            elif keys[pygame.K_LEFT]:
                self.player.move_left()
                moving_left = True
                moving_right = False
            else:
                self.player.stop()
                moving_left = False
                moving_right = False

            # Calculate the background scroll based on character's movement
            if moving_right:
                self.bg_x -= self.player.speed
                bg_scroll += bg_speed
            elif moving_left:
                self.bg_x += self.player.speed
                bg_scroll -= bg_speed

            # Blit the scrolling background
            for i in range(0, int(config['screen_width'] / bg_width) + 15):
                self.SCREEN.blit(self.BG, (i * bg_width - bg_scroll, self.bg_y))

            self.player.update_animation()
            self.SCREEN.blit(self.player.image, self.player.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)
            clock.tick(config['frame_rate'])  # Limit frame rate
