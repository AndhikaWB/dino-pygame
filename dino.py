import pygame

# Ganti animasi tiap 5 frame
anim_delay = 5

# Pengaturan lompatan dino
jump_speed = 7
jump_height = 120

class Dino:
    def __init__(self, road_height):
        # Posisi dino
        self.pos_x = 70
        self.pos_y = 0
        # Ketinggian jalan
        self.road_height = road_height
        # Status dino
        self.state = "IDLE"
        # Area dan animasi dino
        self.rect = None
        self.anim = [
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

    def reset(self):
        # Reset keberadaan dino
        self.__init__(self.road_height)

    def update(self, display, frame, menu):
        if menu.state == "RUN":
            if self.state == "JUMP":
                # Dino naik perlahan-lahan sampai titik maksimum
                if self.pos_y < jump_height:
                    self.pos_y += jump_speed
                # Ganti status dino jika sudah di titik maksimum
                else: self.state = "WALK"
            elif self.state == "WALK":
                # Dino turun perlahan-lahan sampai titik minimum
                if self.pos_y > 0:
                    self.pos_y -= jump_speed
                # Ganti animasi dino jika sudah di titik minimum
                else: self.anim = self.walk_anim

        # Haluskan animasi dino
        frame %= anim_delay * len(self.anim)
        if frame < anim_delay: frame = 0
        else: frame = 1

        # Dapatkan area gambar dino untuk pengecekan tabrakan
        self.rect = self.anim[frame].get_rect(topleft = (self.pos_x, self.pos_y))
        # Tampilkan posisi dino saat ini ke layar game
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_height - self.anim[0].get_height() - self.pos_y))

    def walk(self):
        # Cegah berjalan saat melompat
        if self.pos_y <= 0:
            self.pos_y = 0
            self.state = "WALK"
            self.anim = self.walk_anim

    def jump(self):
        # Cegah melompat berkali-kali
        if self.pos_y == 0:
            self.state = "JUMP"
            self.anim = self.jump_anim

    def duck(self):
        # Cegah menunduk saat melompat
        if self.pos_y == 0:
            self.pos_y -= 20
            self.state = "DUCK"
            self.anim = self.duck_anim

    def hurt(self):
        # Animasi ketika menabrak musuh
        self.anim = self.hurt_anim