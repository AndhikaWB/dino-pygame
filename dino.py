import glob
import pygame

def muat_gambar(nama_animasi):
    # Muat gambar (bisa lebih dari satu) yang terdapat pada folder "assets"
    return [ pygame.image.load(gambar).convert_alpha() for gambar in glob.glob(f"assets/{nama_animasi}*.png") ]

def mainkan_musik(nama_musik):
    # Mainkan suara/musik yang terdapat pada folder "assets"
    musik = pygame.mixer.Sound(f"assets/{nama_musik}.ogg")
    musik.play()

class Dino:
    def __init__(self, tinggi_jalan):
        # Ketinggian jalan dari bagian bawah layar
        self.tinggi_jalan = tinggi_jalan
    
        # Jarak dino dari bagian kiri layar
        self.pos_x = 70
        # Jarak dino dari jalan
        self.pos_y = 0

        # Batas lompatan dino
        self.tinggi_lompat = 126
        self.laju_lompat = 7

        # Status dino mula-mula
        self.status = "DIAM"

        # Animasi dino mula-mula
        self.animasi = muat_gambar("dino_idle")
        # Jeda animasi dino tiap X frame
        self.jeda_animasi = 5

        # Animasi lain yang dibutuhkan (hemat proses)
        self.anim_lari = muat_gambar("dino_move")
        self.anim_lompat = muat_gambar("dino_jump")
        self.anim_jongkok = muat_gambar("dino_duck")
        self.anim_mati = muat_gambar("dino_hurt")
    
        # Area tabrakan bagi dino
        self.area_anim = None

    def perbarui(self, layar, frame, menu):
        # Game dalam keadaan bermain
        if menu.status == "BERMAIN":
            # Jika status dino sedang melompat
            # 1) Tambah ketinggian sampai titik maksimum
            # 2) Ubah status menjadi lari (cegah terbang)
            if self.status == "LOMPAT":
                if self.pos_y < self.tinggi_lompat:
                    self.pos_y += self.laju_lompat
                else: self.status = "LARI"
            # Jika status dino sedang berlari
            # 1) Kurangi ketinggian sampai setara jalan
            # 2) Ganti animasi menjadi berlari
            elif self.status == "LARI":
                if self.pos_y > 0:
                    self.pos_y -= self.laju_lompat
                else: self.animasi = self.anim_lari

        # Agar animasi dino tidak berganti terlalu cepat
        # Misalkan jeda animasi = 5 dan maks frame = 30
        # 1) Untuk frame 0-4 indeks animasinya 0
        # 2) Untuk frame 5-9 indeks animasinya 1
        # 3) Untuk frame 10-14 indeks animasinya 0
        # 4) Untuk frame 15-19 indeks animasinya 1
        # Dan seterusnya sampai frame ke 30...
        frame = frame % (self.jeda_animasi * len(self.animasi))
        if frame < self.jeda_animasi: indeks_anim = 0
        else: indeks_anim = 1

        # Kalkulasikan ketinggian dino berdasarkan tinggi layar, tinggi jalan, tinggi animasi, dan tinggi tambahan bila melompat
        # Perlu diingat bahwa koordinat awal (0, 0) pada layar dimulai dari pojok kiri atas, bukan pojok kiri bawah
        ketinggian_dino = layar.get_height() - self.tinggi_jalan - self.animasi[indeks_anim].get_height() - self.pos_y
        # Tampilkan gambar animasi dino pada koordinat tertentu dalam layar game
        layar.blit(self.animasi[indeks_anim], (self.pos_x, ketinggian_dino))

        # Perbarui juga area animasi dino untuk pengecekan tabrakan
        # Area animasi merupakan kotak transparan (hitbox) di sekeliling dino
        self.area_anim = self.animasi[indeks_anim].get_rect(topleft = (self.pos_x, ketinggian_dino))

    def reset(self):
        # Reset dino seperti semula
        self.__init__(self.tinggi_jalan)

    def lari(self):
        # Cegah berlari saat sedang melompat
        if self.pos_y <= 0:
            self.status = "LARI"
            self.animasi = self.anim_lari
            # Reset posisi dino bila sedang jongkok
            self.pos_y = 0

    def lompat(self):
        # Cegah lompat berkali-kali
        if self.pos_y == 0:
            self.status = "LOMPAT"
            self.animasi = self.anim_lompat
            mainkan_musik("dino_jump")

    def jongkok(self):
        # Cegah jongkok saat sedang melompat
        if self.pos_y == 0:
            self.status = "JONGKOK"
            self.animasi = self.anim_jongkok
            # Turunkan sedikit posisi dino
            self.pos_y = -20

    def mati(self):
        # Saat dino menabrak musuh
        self.animasi = self.anim_mati
        mainkan_musik("dino_hurt")