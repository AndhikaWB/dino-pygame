import pygame
import random

min_gap = 450
max_gap = 650
move_speed = 12
anim_delay = 5

class Enemy:
    # List musuh yang ada
    instances = []

    def __init__(self, road_height):
        # Ketinggian jalan
        self.road_height = road_height

    def reset(self, display):
        # Reset keberadaan musuh
        self.instances.clear()
        self.generate(display)

    def generate(self, display):
        if len(self.instances) == 0:
            # Tambahkan musuh pertama pada ujung kanan layar
            self.instances.append(Papan(self.road_height, display.get_width()))
        elif len(self.instances) == 1:
            # Tambahkan musuh kedua dengan jarak acak dari musuh pertama
            enemy_gap = random.randrange(self.instances[0].pos_x + min_gap, self.instances[0].pos_x + max_gap, 25)
            self.instances.append(Papan(self.road_height, enemy_gap))

    def update(self, display, frame, menu, dino):
            # Tambahkan musuh terus-menerus
            self.generate(display)
            for enemy in self.instances:
                # Update posisi musuh secara perlahan
                enemy.update(display, frame, menu.state)
                if menu.state == "RUN":
                    # Hapus musuh yang sudah di luar layar
                    if enemy.state == "NOT_EXIST":
                        self.instances.remove(enemy)
                        menu.add_score()
                    # Cek apakah dino bertabrakan dengan musuh
                    if dino.rect.colliderect(enemy.rect):
                        dino.hurt()
                        menu.game_end()

class Papan:
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
        self.snail_anim = [
            pygame.image.load("assets/snail_move_01.png").convert_alpha(),
            pygame.image.load("assets/snail_move_02.png").convert_alpha()
        ]
        self.spike_anim = [
            pygame.image.load("assets/spike_move_01.png").convert_alpha(),
            pygame.image.load("assets/spike_move_02.png").convert_alpha()
        ]
        self.fly_anim = [
            pygame.image.load("assets/fly_move_01.png").convert_alpha(),
            pygame.image.load("assets/fly_move_02.png").convert_alpha()
        ]
        # Acak tipe musuh
        self.randomize()

    def randomize(self):
        enemy_type = random.randint(0, 4)
        # Ubah animasi musuh
        if enemy_type == 0:
            self.anim = self.snail_anim
        elif enemy_type == 1:
            self.anim = self.spike_anim
        elif enemy_type > 1:
            self.anim = self.fly_anim
            # Ubah ketinggian musuh
            if enemy_type == 2:
                self.pos_y = 15
            elif enemy_type == 3:
                self.pos_y = 35
            else: self.pos_y = 60

    def update(self, display, frame, game_state):
        if game_state == "RUN":
            # Musuh bergerak ke kiri sampai tidak terlihat
            if self.pos_x - self.anim[0].get_width() > self.anim[0].get_width() * -1:
                self.pos_x -= move_speed
            # Ganti status musuh jika sudah tak terlihat
            else: self.state = "NOT_EXIST"

        # Haluskan animasi musuh
        frame %= anim_delay * len(self.anim)
        if frame < anim_delay: frame = 0
        else: frame = 1

        # Dapatkan area gambar musuh untuk pengecekan tabrakan
        self.rect = self.anim[frame].get_rect(topleft = (self.pos_x, self.pos_y))
        # Tampilkan posisi musuh saat ini ke layar game
        display.blit(self.anim[frame], (self.pos_x, display.get_height() - self.road_height - self.anim[0].get_height() - self.pos_y))