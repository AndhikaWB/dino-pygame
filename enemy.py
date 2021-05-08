import pygame
import random

# Ganti animasi tiap 5 frame
anim_delay = 5

# Jarak antar musuh
min_gap = 450
max_gap = 600

# Kecepatan gerak musuh
move_speed = 12

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
        # Dapatkan tipe secara acak
        enemy_type = random.randint(0, 2)
        if enemy_type == 0:
            # Animasi musuh snail
            self.anim = self.snail_anim
        elif enemy_type == 1:
            # Animasi musuh spike
            self.anim = self.spike_anim
        elif enemy_type == 2:
            # Animasi musuh fly
            self.anim = self.fly_anim
            # Dapatkan ketinggian secara acak
            fly_height = random.randint(0, 3)
            # Ubah ketinggian musuh
            if fly_height == 0:
                self.pos_y = 15
            elif enemy_type == 1:
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

# EnemyMgr digunakan untuk:
# 1) Menambah musuh baru
# 2) Menghapus musuh lama
# 3) Menambah skor menu
# 4) Mengecek tabrakan

class EnemyMgr:
    # List musuh yang ada
    enemies = []

    def __init__(self, road_height):
        # Ketinggian jalan
        self.road_height = road_height

    def reset(self, display):
        # Reset keberadaan musuh
        self.enemies.clear()
        # Tambahkan musuh baru
        self.generate(display)

    def generate(self, display):
        if len(self.enemies) == 0:
            # Tambahkan musuh pertama pada ujung kanan layar
            self.enemies.append(Papan(self.road_height, display.get_width()))
        elif len(self.enemies) == 1:
            # Tambahkan musuh kedua dengan jarak acak dari musuh pertama
            enemy_gap = random.randrange(self.enemies[0].pos_x + min_gap, self.enemies[0].pos_x + max_gap, 25)
            self.enemies.append(Papan(self.road_height, enemy_gap))

    def update(self, display, frame, menu, dino):
        # Tambahkan musuh terus-menerus
        self.generate(display)
        for enemy in self.enemies[:]:
            # Update posisi musuh secara perlahan
            enemy.update(display, frame, menu.state)
            if menu.state == "RUN":
                # Cek apakah dino bertabrakan dengan musuh
                if dino.rect.colliderect(enemy.rect):
                    dino.hurt()
                    menu.endgame()
                    print(f"Game over ({menu.score})")
                # Hapus musuh yang sudah di luar layar
                elif enemy.state == "NOT_EXIST":
                    self.enemies.remove(enemy)
                    # Tambahkan skor menu
                    menu.add_score()