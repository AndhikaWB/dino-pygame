import pygame
import random

move_speed = 12
anim_delay = 5

class Enemy:
    def __init__(self, road_height, pos_x):
        # Posisi musuh
        self.pos_x = pos_x
        self.pos_y = 0
        # Ketinggian jalan
        self.road_height = road_height
        # Status musuh
        self.state = "EXIST"
        # Area dan animasi musuh
        self.rect = None
        self.anim = [
            pygame.image.load("assets/snail_move_01.png").convert_alpha(),
            pygame.image.load("assets/snail_move_02.png").convert_alpha()
        ]

    def reset(self, display):
        return [ Snail(self.road_height, display.get_width()) ]

    def update(self, display, frame, game_state):
        if game_state == "RUN":
            # Bergerak ke kiri sampai tidak terlihat
            if self.pos_x - self.anim[0].get_width() > self.anim[0].get_width() * -1:
                self.pos_x -= move_speed
            # Ganti status jika sudah tak terlihat
            else: self.state = "NOT_EXIST"

        # Haluskan animasi musuh
        frame %= anim_delay * len(self.anim)
        if frame < anim_delay: frame = 0
        else: frame = 1

        # Dapatkan area gambar musuh untuk pengecekan tabrakan
        self.rect = self.anim[frame].get_rect(topleft = (self.pos_x, self.pos_y))
        # Tampilkan posisi musuh saat ini ke layar game
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_height - self.anim[0].get_height() - self.pos_y))

class Snail(Enemy):
    def __init__(self, road_height, pos_x):
        super().__init__(road_height, pos_x)

class Spike(Enemy):
    def __init__(self, road_height, pos_x):
        super().__init__(road_height, pos_x)
        self.anim = [
            pygame.image.load("assets/spike_move_01.png").convert_alpha(),
            pygame.image.load("assets/spike_move_02.png").convert_alpha()
        ]

class Fly(Enemy):
    def __init__(self, road_height, pos_x):
        super().__init__(road_height, pos_x)
        self.anim = [
            pygame.image.load("assets/fly_move_01.png").convert_alpha(),
            pygame.image.load("assets/fly_move_02.png").convert_alpha()
        ]
        # Acak ketinggian musuh
        fly_height = random.randint(0, 4)
        if fly_height == 0:
            self.pos_y = 15
        elif fly_height == 1:
            self.pos_y = 35
        else: self.pos_y = 65