import sys

import pygame
from config.config_manager import ConfigService
from character_sprites.char_class import Player

pygame.mixer.init()
pygame.init()

config_service = ConfigService()
config = config_service.get_config()

# ... (your imports and initialization code)

class Level1Screen:
    def __init__(self):
        self.bg_speed = 10
        self.bg_scroll = 0
        self.sound = pygame.mixer.Sound(config['level_1_music'])
        self.SCREEN = pygame.display.set_mode((config['screen_width'], config['screen_height']))

        # Load and scale the background images
        self.backgrounds = []
        for i in range(1, 3):
            bg_image = pygame.image.load(f"images/background_layer_{i}.png").convert_alpha()
            bg_image = pygame.transform.scale(bg_image, (config['screen_width'], config['screen_height']))
            self.backgrounds.append(bg_image)

        self.background_width = self.backgrounds[0].get_width()  # Assuming all background images have the same width
        self.current_time = 0
        self.player = Player(100, 450)  # Set sprite initial position
        self.player_rect = self.player.rect  # Update player_rect attribute

    def update_display(self):
        current_time = pygame.time.get_ticks()

        # Update the player's position based on velocity
        self.player.handle_events()
        self.player_rect = self.player_rect.move(self.player.velocity)  # Move the player's rect

        # Calculate the clamping bounds based on the player's position
        clamp_left = 400
        clamp_right = 400
        self.player_rect.x = max(clamp_left, min(clamp_right, self.player_rect.x))

        # Determine when to start scrolling based on player's position and an offset
        scroll_start_offset = config['screen_width'] // 4  # Adjust this offset as needed
        if self.player_rect.right >= scroll_start_offset:
            self.bg_scroll -= self.player.velocity[0]  # Scroll the background

        # Clear the screen
        self.SCREEN.fill((0, 0, 0))

        # Draw the background layers
        for i, bg in enumerate(self.backgrounds):
            visible_background_right = (self.bg_scroll // (i + 1)) % self.background_width
            self.SCREEN.blit(bg, (visible_background_right - self.background_width, 0))
            self.SCREEN.blit(bg, (visible_background_right, 0))

        # Update animations and display
        self.player.update_animation(current_time)
        self.SCREEN.blit(self.player.image, self.player_rect.topleft)  # Draw the player sprite
        pygame.display.update()

    def play(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update animations and display
            current_time = pygame.time.get_ticks()
            self.player.update_animation(current_time)
            self.update_display()

            pygame.mixer.Sound.play(self.sound)
            clock.tick(config['frame_rate'])


