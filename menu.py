import pygame

# Font untuk tampilan skor
font_color = 255, 255, 255
font_size = 28

# Batas kecepatan game
min_speed = 30
max_speed = 60

# Skor +10 tiap 5 rintangan
score_add = 10
score_gap = 5

# Speed +3 tiap 10 rintangan
speed_add = 3
speed_gap = 30

class Menu:
    def __init__(self):
        # Skor game
        self.score = 0
        # Status game
        self.state = "DIED"
        # Kecepatan game
        self.speed = min_speed
        # Font untuk skor game
        self.font = pygame.font.Font("assets/VT323-Regular.ttf", font_size)
        # Gambar untuk menu game
        self.title_text = [
            pygame.image.load("assets/title_start_01.png").convert_alpha(),
            pygame.image.load("assets/title_pause_01.png").convert_alpha(),
            pygame.image.load("assets/title_end_01.png").convert_alpha()
        ]
        self.menu_continue = [
            pygame.image.load("assets/menu_continue_01.png").convert_alpha(),
            pygame.image.load("assets/menu_continue_02.png").convert_alpha()
        ]
        self.menu_start = [
            pygame.image.load("assets/menu_start_01.png").convert_alpha(),
            pygame.image.load("assets/menu_start_02.png").convert_alpha()
        ]
        self.menu_exit = [
            pygame.image.load("assets/menu_exit_01.png").convert_alpha(),
            pygame.image.load("assets/menu_exit_02.png").convert_alpha()
        ]
        # Judul dan pilihan menu yang ditampilkan
        self.title = self.title_text[0]
        self.choices = [ self.menu_start, self.menu_exit ]
        # Indeks pilihan menu yang sedang dipilih
        self.choose = 0

    def prev(self):
        # Pilih pilihan sebelumnya pada menu
        if self.choose - 1 >= 0:
            self.choose -= 1

    def next(self):
        # Pilih pilihan selanjutnya pada menu
        if self.choose + 1 < len(self.choices):
            self.choose += 1

    def add_score(self):
        self.score += 1
        # Bonus skor tiap X rintangan
        if self.score % score_gap == 0:
            self.score += score_add
            print(f"Score +{score_gap} ({self.score})")
        # Tambah kecepatan tiap X rintangan
        if self.score % speed_gap == 0:
            if self.speed < max_speed:
                self.speed += speed_add
                print(f"Speed +{speed_add} ({self.speed})")

    def reset(self):
        # Ulangi game dari posisi awal
        self.__init__()
        self.state = "RUN"

    def unpause(self):
        # Lanjutkan game dari posisi terakhir
        self.state = "RUN"
        self.choose = 0

    def pause(self):
        # Menampilkan menu pause
        self.state = "PAUSE"
        # Judul pada menu pause
        self.title = self.title_text[1]
        # Pilihan pada menu pause
        self.choices = [ self.menu_continue, self.menu_start, self.menu_exit ]

    def endgame(self):
        # Menampilkan menu game over
        self.state = "DIED"
        # Judul pada menu game over
        self.title = self.title_text[2]
        # Pilihan pada menu game over
        self.choices = [ self.menu_start, self.menu_exit ]

    def update(self, display):
        # Ikuti perubahan skor secara realtime
        score_text = self.font.render("Skor: " + str(self.score), True, font_color)
        # Tampilkan skor di layar pada koordinat (10, 10)
        display.blit(score_text, (10, 10))

        # Jika game sedang pause atau game over
        if self.state != "RUN":
            # Ketinggian judul pada menu
            title_pos_y = 170
            # Ketinggian pilihan pada menu
            menu_pos_y = title_pos_y + 70
            # Jarak antar pilihan pada menu
            menu_gap = 40

            # Tampilkan judul menu
            title_rect = self.title.get_rect(center = (display.get_width() // 2, title_pos_y))
            display.blit(self.title, title_rect)

            # Enumerasi tiap-tiap pilihan pada menu
            for index, choice in enumerate(self.choices):
                # Kalkulasikan posisi gambar untuk pilihan ke X
                choice_rect = choice[0].get_rect(center = (display.get_width() // 2, menu_pos_y))

                # Tampilkan pilihan sebagai gambar pada layar
                if self.choose == index:
                    # Gambar berwarna gelap jika sedang dipilih
                    display.blit(choice[1], choice_rect)
                # Gambar berwarna terang jika tidak sedang dipilih
                else: display.blit(choice[0], choice_rect)

                # Tambah jarak untuk gambar pilihan ke X+1
                menu_pos_y += menu_gap