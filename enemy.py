import pygame
import random

class Enemy:
    def __init__(self, road_y):
        # Posisi musuh
        self.pos_x = None
        self.pos_y = 0
        # Ketinggian jalan
        self.road_y = road_y
        # Status musuh
        self.state = "NOT_EXIST"
        # Area animasi musuh
        self.rect = None
        # Gerakan animasi musuh
        self.anim = [
            pygame.image.load("assets/snail_move_01.png").convert_alpha(),
            pygame.image.load("assets/snail_move_02.png").convert_alpha()
        ]

    def update(self, display, frame):
        if self.pos_x == None:
            # Mulai dari ujung kanan
            self.pos_x = display.get_width()
        elif self.pos_x - self.anim[0].get_width() > self.anim[0].get_width() * -1:
            # Bergerak perlahan ke kiri (selama masih terlihat di layar)
            self.pos_x -= 12
        else:
            # Sudah sampai ke ujung kiri
            self.state = "NOT_EXIST"

        # Haluskan animasi jalan
        frame %= 5 * len(self.anim)
        if frame < 5: frame = 0
        else: frame = 1

        self.rect = self.anim[frame].get_rect(topleft = (self.pos_x, self.pos_y))
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_y - self.anim[0].get_height() - self.pos_y))

class Snail(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        # Status musuh
        self.state = "EXIST"

class Spike(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        # Status musuh
        self.state = "EXIST"
        # Gerakan animasi musuh
        self.anim = [
            pygame.image.load("assets/spike_move_01.png").convert_alpha(),
            pygame.image.load("assets/spike_move_02.png").convert_alpha()
        ]

class Fly(Enemy):
    def __init__(self, road_y):
        super().__init__(road_y)
        # Status musuh
        self.state = "EXIST"
        # Gerakan animasi musuh
        self.anim = [
            pygame.image.load("assets/fly_move_01.png").convert_alpha(),
            pygame.image.load("assets/fly_move_02.png").convert_alpha()
        ]
        # Acak ketinggian musuh
        fly_height = random.randint(0, 2)
        if fly_height == 0:
            self.pos_y = 65
        elif fly_height == 1:
            self.pos_y = 40
        elif fly_height == 2:
            self.pos_y = 15