import pygame
import sys
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
        self.player = Player(100, 450)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player.move('right')
            self.bg_scroll += self.bg_speed
        elif keys[pygame.K_LEFT]:
            self.player.move('left')
            self.bg_scroll -= self.bg_speed
        elif keys[pygame.K_f]:
            if self.player.current_action != 'attack1':
                self.player.attack()
        elif keys[pygame.K_SPACE]:
            self.player.jump()
        else:
            self.player.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_display(self):
        current_time = pygame.time.get_ticks()

        self.SCREEN.blit(self.BG, (self.bg_x, self.bg_y))

        for i in range(0, int(config['screen_width'] / self.bg_width) + 15):
            self.SCREEN.blit(self.BG, (i * self.bg_width - self.bg_scroll, self.bg_y))
        self.SCREEN.blit(self.player.image, self.player.rect)
        self.player.update_animation(current_time)
        pygame.display.update()

        self.bg_x -= self.bg_speed
        if self.bg_x <= -self.bg_width:
            self.bg_x = 0

        pygame.display.update()

    def play(self):
        clock = pygame.time.Clock()

        while True:
            self.handle_input()
            self.handle_events()
            self.update_display()

            pygame.mixer.Sound.play(self.sound)
            clock.tick(config['frame_rate'])
