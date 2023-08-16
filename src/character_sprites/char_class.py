import pygame
import sys
from config.config_manager import ConfigService

config_service = ConfigService()
config = config_service.get_config()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.direction = None
        self.animation_speed = 60
        self.attack_duration = 400  # Duration of attack animation in milliseconds
        self.speed = 8  # Increased movement speed for smoother gameplay
        self.jump_speed = -12
        self.last_jump_time = 0
        self.gravity = 1
        self.is_jumping = False
        self.old_x = x
        self.old_y = y
        self.current_action = 'ready'
        self.velocity = [0, 0]  # [x_velocity, y_velocity]
        self.attacking = False
        self.attack_start_time = 0

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

        self.frame_index = 0
        self.image = self.animation_frames[self.current_action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def attack(self):
        if not self.attacking:
            self.attacking = True
            self.attack_start_time = pygame.time.get_ticks()
            self.current_action = 'attack1'

            # Store the player's original position
            self.old_x = self.rect.x
            self.old_y = self.rect.y

            # Move the sprite down 200 pixels
            self.rect.y -= 200

        # Check if the attack animation is finished
        if self.attack_start_time + self.attack_duration <= pygame.time.get_ticks():
            self.attacking = False
            self.current_action = 'ready'

            # Move the sprite back to its original position
            self.rect.y = self.old_y

    def update_animation(self, current_time):
        time_elapsed = current_time - self.last_update_time

        if self.current_action == 'walk':
            # Flip the sprite image when moving left
            if self.direction == 'left':
                self.image = pygame.transform.flip(self.animation_frames[self.current_action][self.frame_index], True,
                                                   False)
            else:
                self.image = self.animation_frames[self.current_action][self.frame_index]

        if self.attacking and (current_time - self.attack_start_time >= self.attack_duration):
            self.attacking = False
            self.current_action = 'ready'
            self.rect.x = self.old_x
            self.rect.y = self.old_y

        if self.current_action == 'jump' and self.frame_index == len(self.animation_frames['jump']) - 1:
            self.current_action = 'ready'

        if self.current_action == 'jump':
            # Slow down the jump animation by 2 times
            if time_elapsed >= self.animation_speed * 4:
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
                self.image = self.animation_frames[self.current_action][self.frame_index]
                self.last_update_time = current_time
                self.rect.x += self.velocity[0]  # Update horizontal position during jump
            elif time_elapsed >= self.animation_speed * 2:
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
                self.image = self.animation_frames[self.current_action][self.frame_index]
                self.last_update_time = current_time

        elif self.current_action == 'attack1':
            # Display the attack animation frames with a slightly bigger size
            if time_elapsed >= self.animation_speed:
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
                attack_frame = self.animation_frames[self.current_action][self.frame_index]
                self.image = pygame.transform.scale(attack_frame,
                                                    (config['player_width'] * 2, config['player_height'] * 2))
                self.last_update_time = current_time

        else:
            # Regular animation update
            if time_elapsed >= self.animation_speed:
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames[self.current_action])
                self.image = self.animation_frames[self.current_action][self.frame_index]
                self.last_update_time = current_time
                self.rect.x += self.velocity[0]  # Update horizontal position during regular actions

                self.update_jump()

    def move(self, direction):
        if direction == 'right':
            self.velocity[0] = self.speed
            self.current_action = 'walk'
            self.direction = 'right'  # Update player direction
            print(self.direction)
        elif direction == 'left':
            self.velocity[0] = -self.speed
            self.current_action = 'walk'
            self.direction = 'left'  # Update player direction
            print(self.direction)
        else:
            self.velocity[0] = 0


    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity[1] = self.jump_speed
            self.current_action = 'jump'

    def update_jump(self):
        if self.is_jumping:
            self.rect.y += self.velocity[1]
            self.velocity[1] += self.gravity
            if self.rect.y >= config['ground_level']:
                self.is_jumping = False
                self.rect.y = config['ground_level']
                self.velocity[1] = 0

    def stop(self):
        if self.current_action == 'walk':
            self.current_action = 'ready'
            self.velocity[0] = 0  # Set horizontal velocity to 0 when stopping

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == getattr(pygame, config['player_attack']):
                    self.attack()
                elif event.key == getattr(pygame, config['player_left']):
                    self.move('left')
                elif event.key == getattr(pygame, config['player_right']):
                    self.move('right')
                elif event.key == getattr(pygame, config['player_jump']):
                    self.jump()
            elif event.type == pygame.KEYUP:
                if event.key == getattr(pygame, config['player_left']) or event.key == getattr(pygame,
                                                                                               config['player_right']):
                    self.stop()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
