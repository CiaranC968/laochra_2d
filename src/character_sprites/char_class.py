import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_speed = 70
        self.animation_counter = 0
        self.animation_frames = {
            'ready': [],
            'walk': [],
            'jump': [],
            'attack1': []
        }

        self.original_size = (config['player_width'], config['player_height'])  # Store original size
        self.last_update_time = pygame.time.get_ticks()

        for action in self.animation_frames.keys():
            for i in range(1, 7):
                frame = pygame.image.load(f"character_sprites/axe_origin/{action}_{i}.png")
                frame = pygame.transform.scale(frame, (config['player_width'], config['player_height']))
                self.animation_frames[action].append(frame)

        self.current_action = 'ready'
        self.frame_index = 0
        self.image = self.animation_frames[self.current_action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0.49  # Increased movement speed for smoother gameplay
        self.jump_speed = -12
        self.gravity = 1
        self.is_jumping = False
        self.old_x = x

    def update_animation(self, current_time):
        time_elapsed = current_time - self.last_update_time

        if time_elapsed >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
            self.image = self.animation_frames[self.current_action][self.frame_index]
            self.last_update_time = current_time

    def move(self, direction):
        if direction == 'right':
            self.current_action = 'walk'
            self.rect.x += self.speed
            self.old_x = self.rect.x
        elif direction == 'left':
            self.current_action = 'walk'
            self.rect.x -= self.speed
            self.old_x = self.rect.x

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

    def is_moving(self):
        if self.rect.x != self.old_x:
            return True
        else:
            return False

    def stop(self):
        self.current_action = 'ready'
        self.frame_index = 0  # Reset frame index when stopping
