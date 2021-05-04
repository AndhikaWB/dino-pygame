import pygame

class Dino:
    def __init__(self, road_y):
        # Posisi dino
        self.pos_x = 70
        self.pos_y = 0
        # Ketinggian jalan
        self.road_y = road_y
        # Status dino
        self.state = "IDLE"
        # Area animasi dino
        self.rect = None
        # Gerakan animasi dino
        self.anim = self.idle_anim = [
            pygame.image.load("assets/dino_idle_01.png").convert_alpha()
        ]

        self.walk_anim = [
            pygame.image.load("assets/dino_move_01.png").convert_alpha(),
            pygame.image.load("assets/dino_move_02.png").convert_alpha()
        ]

        self.jump_anim = [
            pygame.image.load("assets/dino_jump_01.png").convert_alpha()
        ]

        self.duck_anim = [
            pygame.image.load("assets/dino_duck_01.png").convert_alpha()
        ]

        self.hurt_anim = [
            pygame.image.load("assets/dino_hurt_01.png").convert_alpha()
        ]

    def update(self, display, frame):
        if self.state == "JUMP":
            if self.pos_y < 120:
                # Naik perlahan sampai batas maksimum
                self.pos_y += 7
            else:
                # Sudah di batas lompat maksimum
                self.state = "WALK"
        elif self.state == "WALK":
            if self.pos_y > 0:
                # Turun perlahan sampai batas minimum
                self.pos_y -= 7
            else:
                # Sudah di batas minimum (pada ketinggian jalan)
                self.anim = self.walk_anim

        # Haluskan animasi jalan
        frame %= 5 * len(self.anim)
        if frame < 5: frame = 0
        else: frame = 1

        self.rect = self.anim[frame].get_rect(topleft = (self.pos_x, self.pos_y))
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_y - self.anim[0].get_height() - self.pos_y))

    def walk(self):
        # Cegah jalan saat melompat
        if self.pos_y <= 0:
            self.pos_y = 0
            self.state = "WALK"
            self.anim = self.walk_anim

    def jump(self):
        # Cegah lompat berkali-kali
        if self.pos_y == 0:
            self.state = "JUMP"
            self.anim = self.jump_anim

    def duck(self):
        # Cegah jongkok saat melompat
        if self.pos_y == 0:
            self.pos_y -= 20
            self.state = "DUCK"
            self.anim = self.duck_anim