import pygame
import random

from menu import Menu
from dino import Dino
from enemy import EnemyMgr

# Ukuran layar game
display_width = 800
display_height = 600

# Ketinggian jalan
road_height = 50

def dino_game():
    # Instansiasi objek
    menu = Menu()
    dino = Dino(road_height)
    enemy = EnemyMgr(road_height)

    # Frame mula-mula
    frame = 0

    while True:
        # Tampilkan background game
        display.blit(background, (0, 0))

        # Dapatkan informasi event saat ini
        for event in pygame.event.get():
            # Keluar dari game jika layar ditutup
            if event.type == pygame.QUIT:
                return

            # Game sedang berjalan
            elif menu.state == "RUN":
                if event.type == pygame.KEYDOWN:
                    # Tekan UP untuk melompat
                    if event.key == pygame.K_UP:
                        dino.jump()
                    # Tekan DOWN untuk menunduk
                    elif event.key == pygame.K_DOWN:
                        dino.duck()
                    # Tekan ESC untuk berhenti sejenak
                    elif event.key == pygame.K_ESCAPE:
                        menu.pause()
                # Kembali berjalan sesudah menekan tombol
                elif event.type == pygame.KEYUP:
                    dino.walk()

            # Game sedang berhenti pada menu
            elif menu.state != "RUN":
                if event.type == pygame.KEYDOWN:
                    # Tekan UP untuk pilihan sebelumnya
                    if event.key == pygame.K_UP:
                        menu.prev()
                    # Tekan DOWN untuk pilihan selanjutnya
                    elif event.key == pygame.K_DOWN:
                        menu.next()
                    # Tekan ENTER untuk memilih pilihan menu
                    elif event.key == pygame.K_RETURN:
                        # Posisi pilihan pada menu pause sebagai basis
                        if menu.state == "PAUSE":
                            choose = menu.choose
                        # Sesuaikan posisi pilihan seperti menu pause
                        elif menu.state == "DIED":
                            choose = menu.choose + 1

                        # Memilih "Lanjutkan permainan"
                        if choose == 0:
                            menu.unpause()
                        # Memilih "Permainan baru"
                        elif choose == 1:
                            menu.reset()
                            dino.reset()
                            enemy.reset(display)
                        # Memilih "Keluar"
                        elif choose == 2:
                            return

        # Update gerakan dino
        dino.update(display, frame, menu)

        # Update musuh, skor, dan cek tabrakan
        enemy.update(display, frame, menu, dino)

        # Update gerakan menu dan layar
        menu.update(display)
        pygame.display.update()

        # Atur frame untuk loop selanjutnya
        frame = (frame + 1) % menu.speed
        fps.tick(menu.speed)

if __name__ == "__main__":
    # Inisialisasi layar
    pygame.init()

    # Inisialisasi game
    pygame.display.set_caption("Bellatrix's Dino Game")
    background = pygame.image.load("assets/background_01.png")
    display = pygame.display.set_mode((display_width, display_height))
    fps = pygame.time.Clock()

    # Panggil game
    dino_game()
    pygame.quit()