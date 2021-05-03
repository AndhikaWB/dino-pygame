import pygame
import random

class Enemy:
    def __init__(self, road_y, anim = None):
        # Posisi musuh
        self.pos_x = None
        self.pos_y = 0
        # Ketinggian jalan
        self.road_y = road_y
        # Status musuh
        self.state = "NOT_EXIST"
        # Animasi dan bentuk musuh
        if anim == None:
            self.anim = [
                pygame.image.load("assets/snail_move_01.png").convert_alpha(),
                pygame.image.load("assets/snail_move_02.png").convert_alpha()
            ]
        else: self.anim = anim

        self.rect = self.anim[0].get_rect()

    def update(self, display, frame):
        if self.pos_x == None:
            # Mulai dari ujung kanan
            self.pos_x = display.get_width()
        elif self.pos_x - self.anim[0].get_width() > 0:
            # Bergerak perlahan ke kiri
            self.pos_x -= 12
        else:
            # Sudah sampai ke ujung kiri
            self.state = "NOT_EXIST"

        # Haluskan animasi jalan
        frame %= 5 * len(self.anim)
        if frame < 5: frame = 0
        else: frame = 1

        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_y - self.anim[0].get_height() - self.pos_y))

class Snail(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        self.state = "EXIST"

class Spike(Enemy):
    def __init__(self, road_y):
        spike_anim = [
            pygame.image.load("assets/spike_move_01.png").convert_alpha(),
            pygame.image.load("assets/spike_move_02.png").convert_alpha()
        ]

        super().__init__(road_y, spike_anim)
        self.state = "EXIST"

class Fly(Enemy):
    def __init__(self, road_y):
        fly_anim = [
            pygame.image.load("assets/fly_move_01.png").convert_alpha(),
            pygame.image.load("assets/fly_move_02.png").convert_alpha()
        ]

        super().__init__(road_y, fly_anim)
        self.state = "EXIST"
        # Acak posisi terbang
        self.pos_y = random.randrange(45, 60, 5)