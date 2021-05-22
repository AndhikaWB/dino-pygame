import glob
import pygame
import random

def muat_gambar(nama_animasi):
    # Muat gambar (bisa lebih dari satu) yang terdapat pada folder "assets"
    return [ pygame.image.load(gambar).convert_alpha() for gambar in glob.glob(f"assets/{nama_animasi}*.png") ]

class Papan:
    def __init__(self, tinggi_jalan, pos_x):
        # Ketinggian jalan dari bagian bawah layar
        self.tinggi_jalan = tinggi_jalan

        # Jarak musuh dari bagian kiri layar
        self.pos_x = pos_x
        # Jarak musuh dari jalan
        self.pos_y = 0

        # Kecepatan gerak musuh
        self.laju_musuh = 12

        # Status musuh mula-mula
        self.status = "DIHADANG"

        # Animasi musuh mula-mula
        self.animasi = []
        # Jeda animasi musuh tiap X frame
        self.jeda_animasi = 5

        # Area tabrakan bagi musuh
        self.area_anim = None

    def perbarui(self, layar, frame, menu):
        # Agar animasi musuh tidak berganti terlalu cepat
        # Misalkan jeda animasi = 5 dan maks frame = 30
        # 1) Untuk frame 0-4 indeks animasinya 0
        # 2) Untuk frame 5-9 indeks animasinya 1
        # 3) Untuk frame 10-14 indeks animasinya 0
        # 4) Untuk frame 15-19 indeks animasinya 1
        # Dan seterusnya sampai frame ke 30...
        frame = frame % (self.jeda_animasi * len(self.animasi))
        if frame < self.jeda_animasi: indeks_anim = 0
        else: indeks_anim = 1

        # Game dalam keadaan bermain
        if menu.status == "BERMAIN":
            # Musuh bergerak ke kiri sampai tidak terlihat
            if self.pos_x > self.animasi[indeks_anim].get_width() * -1:
                self.pos_x -= self.laju_musuh
            # Ganti status musuh setelah tidak terlihat
            else: self.status = "DILEWATI"

        # Kalkulasikan ketinggian musuh berdasarkan tinggi layar, tinggi jalan, tinggi animasi, dan tinggi tambahan bila terbang
        # Perlu diingat bahwa koordinat awal (0, 0) pada layar dimulai dari pojok kiri atas, bukan pojok kiri bawah
        ketinggian_papan = layar.get_height() - self.tinggi_jalan - self.animasi[indeks_anim].get_height() - self.pos_y
        # Tampilkan gambar animasi musuh pada koordinat tertentu dalam layar game
        layar.blit(self.animasi[indeks_anim], (self.pos_x, ketinggian_papan))

        # Perbarui juga area animasi musuh untuk pengecekan tabrakan
        # Area animasi merupakan kotak transparan (hitbox) di sekeliling musuh
        self.area_anim = self.animasi[indeks_anim].get_rect(topleft = (self.pos_x, ketinggian_papan))

class Siput(Papan):
    def __init__(self, tinggi_jalan, pos_x):
        super().__init__(tinggi_jalan, pos_x)
        # Dapatkan animasi untuk siput
        self.animasi = muat_gambar("snail_move")

class Simerah(Papan):
    def __init__(self, tinggi_jalan, pos_x):
        super().__init__(tinggi_jalan, pos_x)
        # Dapatkan animasi untuk simerah
        self.animasi = muat_gambar("spike_move")

class Lalat(Papan):
    def __init__(self, tinggi_jalan, pos_x):
        super().__init__(tinggi_jalan, pos_x)
        # Dapatkan animasi untuk lalat
        self.animasi = muat_gambar("fly_move")
        # Acak ketinggian lalat terhadap jalan
        self.pos_y = random.choice((15, 30, 60))

class Lebah(Papan):
    def __init__(self, tinggi_jalan, pos_x):
        super().__init__(tinggi_jalan, pos_x)
        # Dapatkan animasi untuk lebah
        self.animasi = muat_gambar("bee_move")
        # Acak ketinggian lebah terhadap jalan
        self.pos_y = random.choice((20, 30, 65))