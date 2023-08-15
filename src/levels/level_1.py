import pygame
from config.config_manager import ConfigService
from character_sprites.char_class import Player

pygame.mixer.init()
pygame.init()

config_service = ConfigService()
config = config_service.get_config()


class Level1Screen:
    def __init__(self):
        self.bg_width = config['screen_width']
        self.bg_speed = 5
        self.bg_scroll = 0
        self.sound = pygame.mixer.Sound(config['level_1_music'])
        self.SCREEN = pygame.display.set_mode((config['screen_width'], config['screen_height']))
        self.BG = pygame.image.load(config['level_1']).convert()
        self.BG = pygame.transform.scale(self.BG, (config['screen_width'], config['screen_height']))
        self.bg_x = 0
        self.bg_y = 0
        self.current_time = 0
        self.player = Player(100, 450)

    def update_display(self):
        current_time = pygame.time.get_ticks()

        # Scroll the background
        amount_to_scroll = self.player.rect.x - self.bg_scroll

        # Calculate the speed modifier
        if self.player.rect.x > config['screen_width'] / 4:
            speed_modifier = 0.1
        elif self.player.rect.x > config['screen_width'] / 2:
            speed_modifier = 0.2
        elif self.player.rect.x > 3 * config['screen_width'] / 4:
            speed_modifier = 0.3
        else:
            speed_modifier = 0

        # Check if the amount to scroll is greater than the width of the background
        if amount_to_scroll > self.BG.get_width() * speed_modifier:
            # Scroll the background to the left
            self.bg_scroll -= amount_to_scroll * speed_modifier

            # Keep the background within the screen bounds
            if self.bg_scroll < 0:
                self.bg_scroll = 0

        # Otherwise, scroll the background normally
        else:
            self.bg_scroll += amount_to_scroll * speed_modifier

        # Scroll the background based on the player's movement
        self.bg_scroll += self.player.velocity[0] * current_time / 9000

        self.SCREEN.blit(self.BG, (self.bg_x - self.bg_scroll, self.bg_y))

        for i in range(0, int(config['screen_width'] / self.BG.get_width()) + 15):
            self.SCREEN.blit(self.BG, (i * self.BG.get_width() - self.bg_scroll, self.bg_y))

        # Update the player's position
        self.player.handle_events()
        self.player.rect.clamp_ip(self.SCREEN.get_rect())  # Clamp the player's position

        # Update animations and display
        self.SCREEN.blit(self.player.image, self.player.rect)
        self.player.update_animation(current_time)
        pygame.display.update()

    def play(self):
        clock = pygame.time.Clock()

        while True:
            self.player.handle_events()
            # Update animations and display
            current_time = pygame.time.get_ticks()
            self.player.update_animation(current_time)
            self.update_display()

            pygame.mixer.Sound.play(self.sound)
            clock.tick(config['frame_rate'])