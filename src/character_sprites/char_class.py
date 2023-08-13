import pygame
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_speed = 10  # Adjust this value for animation speed
        self.animation_counter = 0
        self.animation_frames = {
            'ready': [],  # List to store idle animation frames
            'walk': [],   # List to store walk animation frames
            'jump': []    # List to store jump animation frames
        }

        for action in self.animation_frames.keys():
            for i in range(1, 7):  # Assuming you have 6 images named walk_1.png to walk_6.png
                frame = pygame.image.load(f"character_sprites/axe_origin/{action}_{i}.png").convert_alpha()
                frame = pygame.transform.scale(frame, (config['player_width'], config['player_height']))
                self.animation_frames[action].append(frame)

        self.current_action = 'ready'  # Set the initial action to idle
        self.frame_index = 0  # Current frame index
        self.image = self.animation_frames[self.current_action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1  # Movement speed
        self.jump_speed = -12  # Negative value for jumping upwards
        self.gravity = 1  # Gravity value for falling
        self.is_jumping = False  # Flag to track if player is currently jumping

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
            self.image = self.animation_frames[self.current_action][self.frame_index]

    def move_right(self):
        self.current_action = 'walk'
        self.rect.x += self.speed

    def move_left(self):
        self.current_action = 'walk'
        self.rect.x -= self.speed

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.current_action = 'jump'
            self.jump_speed = -12  # Reset jump speed for each jump

    def update_jump(self):
        if self.is_jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += self.gravity
            if self.rect.y >= config['ground_level']:  # Adjust the ground level as needed
                self.is_jumping = False
                self.rect.y = config['ground_level']

    def stop(self):
        self.current_action = 'ready'
