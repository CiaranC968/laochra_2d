import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_speed = 10
        self.animation_counter = 0
        self.animation_frames = {
            'ready': [],
            'walk': [],
            'jump': [],
            'attack1': []
        }

        self.original_size = (config['player_width'], config['player_height'])  # Store original size

        for action in self.animation_frames.keys():
            for i in range(1, 7):
                frame = pygame.image.load(f"character_sprites/axe_origin/{action}_{i}.png").convert_alpha()
                frame = pygame.transform.scale(frame, (config['player_width'], config['player_height']))
                self.animation_frames[action].append(frame)

        self.current_action = 'ready'
        self.frame_index = 0
        self.image = self.animation_frames[self.current_action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.49# Increased movement speed for smoother gameplay
        self.jump_speed = -12
        self.gravity = 1
        self.is_jumping = False

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
            self.image = self.animation_frames[self.current_action][self.frame_index]

    def move(self, direction):
        if direction == 'right':
            self.current_action = 'walk'
            self.rect.x += self.speed
        elif direction == 'left':
            self.current_action = 'walk'
            self.rect.x -= self.speed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.current_action = 'jump'
            self.jump_speed = -12

    def update_jump(self):
        if self.is_jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += self.gravity
            if self.rect.y >= config['ground_level']:
                self.is_jumping = False
                self.rect.y = config['ground_level']

    def attack(self):
        if self.current_action != 'attack1':
            self.current_action = 'attack1'
            self.frame_index = 0  # Reset frame index for attack animation

    def stop(self):
        self.current_action = 'ready'
        self.frame_index = 0  # Reset frame index when stopping
