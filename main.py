import pygame

from dino import Dino
from nilai import Nilai
from menu import Menu
from pabrik import Pabrik

class Game:
    def __init__(self):
        # Ukuran layar game
        self.lebar_layar = 800
        self.tinggi_layar = 600

        # Inisialisasi dino game
        self.layar = pygame.display.set_mode((self.lebar_layar, self.tinggi_layar))
        self.gambar_latar = pygame.image.load("assets/background_01.png").convert()
        pygame.display.set_caption("Bellatrix's Dino Game")
        self.fps = pygame.time.Clock()
        pygame.mouse.set_visible(False)

        # Ketinggian jalan
        self.tinggi_jalan = 50

        # Instansiasi kelas
        self.menu = Menu()
        self.nilai = Nilai()
        self.dino = Dino(self.tinggi_jalan)
        self.pabrik = Pabrik(self.tinggi_jalan)

        # Frame mula-mula
        self.frame = 0

    def jalankan(self):
        while True:
            # Tampilkan gambar latar
            self.layar.blit(self.gambar_latar, (0, 0))

            for event in pygame.event.get():
                # Cek event yang sedang terjadi
                keluar = self.cek_event(event)
                # Keluar dari game jika diminta
                if keluar == True: return

            # Tampilkan menu bila tidak sedang bermain
            self.menu.perbarui(self.layar)
            # Perbarui posisi dino
            self.dino.perbarui(self.layar, self.frame, self.menu)
            # Perbarui posisi musuh, cek tabrakan, dan tambah nilai skor
            self.pabrik.perbarui(self.layar, self.frame, self.menu, self.nilai, self.dino)
            # Tampilkan nilai skor
            self.nilai.perbarui(self.layar)

            # Terapkan semua perubahan pada layar
            pygame.display.update()

            # Atur frame untuk perulangan selanjutnya
            self.frame = (self.frame + 1) % self.nilai.laju
            self.fps.tick(self.nilai.laju)

    def cek_event(self, event):
        # Keluar game saat tombol silang diklik
        if event.type == pygame.QUIT:
            return True
        # Game dalam keadaan bermain
        elif self.menu.status == "BERMAIN":
            if event.type == pygame.KEYDOWN:
                # Lompat saat tombol panah atas ditekan
                if event.key == pygame.K_UP:
                    self.dino.lompat()
                # Jongkok saat tombol panah bawah ditekan
                elif event.key == pygame.K_DOWN:
                    self.dino.jongkok()
                # Berhenti saat tombol escape ditekan
                elif event.key == pygame.K_ESCAPE:
                    self.menu.berhenti()
            elif event.type == pygame.KEYUP:
                # Berlari saat tombol panah bawah dilepas
                if event.key == pygame.K_DOWN:
                    self.dino.lari()
        # Game sedang berada pada menu
        elif self.menu.status != "BERMAIN":
            if event.type == pygame.KEYDOWN:
                # Pilihan sebelumnya saat tombol panah atas ditekan
                if event.key == pygame.K_UP:
                    self.menu.sebelumnya()
                # Pilihan berikutnya saat tombol panah bawah ditekan
                elif event.key == pygame.K_DOWN:
                    self.menu.berikutnya()
                # Pilih pilihan tersebut saat tombol enter ditekan
                elif event.key == pygame.K_RETURN:
                    if self.menu.pilih() == "LANJUTKAN":
                        self.menu.reset()
                    elif self.menu.pilih() == "MAIN_BARU":
                        for objek in (self.menu, self.nilai, self.dino, self.pabrik):
                            objek.reset()
                        self.dino.lari()
                    elif self.menu.pilih() == "KELUAR":
                        return True

if __name__ == "__main__":
    # Inisialisasi layar dan suara
    pygame.init()
    pygame.mixer.init()

    # Jalankan dino game
    dino_game = Game()
    dino_game.jalankan()

    # Matikan layar dan suara
    pygame.quit()
    pygame.mixer.quit()