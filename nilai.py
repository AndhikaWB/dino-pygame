import pygame

def mainkan_musik(nama_musik):
    # Mainkan suara/musik yang terdapat pada folder "assets"
    musik = pygame.mixer.Sound(f"assets/{nama_musik}.ogg")
    musik.play()

class Nilai:
    def __init__(self):
        # Posisi skor pada layar
        self.pos_x = 10
        self.pos_y = 10

        # Skor game mula-mula
        self.skor = 0
        # Skor +10 tiap 5 rintangan
        self.tambah_skor = 10
        self.gap_skor = 5

        # Batas kecepatan game
        self.laju_min = 30
        self.laju_maks = 60

        # Kecepatan game mula-mula
        self.laju = self.laju_min
        # Kecepatan +3 tiap 10 rintangan
        self.tambah_laju = 3
        self.gap_laju = 30

        # Inisialisasi font yang dipakai
        self.ukuran_font = 28
        self.warna_font = (255, 255, 255) # Putih
        self.font = pygame.font.Font(f"assets/VT323-Regular.ttf", self.ukuran_font)

    def perbarui(self, layar):
        # Perbarui skor secara terus-menerus
        teks_skor = self.font.render("Skor: " + str(self.skor), True, self.warna_font)
        # Tampilkan skor yang telah diperbarui ke layar
        layar.blit(teks_skor, (self.pos_x, self.pos_y))

    def reset(self):
        # Reset skor seperti semula
        self.__init__()

    def tambah(self):
        # Tambah satu skor
        self.skor += 1
        # Skor tambahan setelah X rintangan
        if self.skor % self.gap_skor == 0:
            self.skor += self.tambah_skor
            mainkan_musik("dino_score")
        # Kecepatan tambahan setelah Y rintangan
        if self.skor % self.gap_laju == 0:
            if self.laju < self.laju_maks:
                self.laju += self.tambah_laju