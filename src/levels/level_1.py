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
        self.BG = pygame.image.load(config['level_1'])
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))
        self.player = Player(100, 380)

    def get_font(self, size):
        return pygame.font.Font("fonts/MedievalMystery.ttf", size)

    def play(self):
        while True:
            play_mouse_pos = pygame.mouse.get_pos()

            self.SCREEN.blit(self.BG, (0, 0))  # Blit the background image first

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()  # Call move_right when right arrow key is pressed
            elif keys[pygame.K_LEFT]:
                self.player.move_left()  # Call move_left when left arrow key is pressed
            elif keys[pygame.K_SPACE]:
                self.player.jump()
            else:
                self.player.stop()

            self.player.update_animation()  # Update player's animation frame
            self.SCREEN.blit(self.player.image, self.player.rect)  # Blit the player sprite

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            pygame.mixer.Sound.play(self.sound)

