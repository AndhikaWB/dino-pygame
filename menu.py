import pygame

# Font untuk teks skor
font_size = 28
font_color = (255, 255, 255)

# Batas kecepatan game
min_speed = 30
max_speed = 60

# Skor +10 tiap 5 rintangan
score_point_add = 10
score_point_gap = 5

# Speed +3 tiap 10 rintangan
score_speed_add = 3
score_speed_gap = 30

class Menu:
    def __init__(self):
        # Skor game
        self.score = 0
        # Status game
        self.state = "DIED"
        # Kecepatan game
        self.speed = min_speed
        # Font game
        self.font = pygame.font.Font("assets/VT323-Regular.ttf", font_size)
        # Animasi pada menu game
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
        self.menu = [ self.menu_start, self.menu_exit ]
        # Posisi mouse pada pilihan menu
        self.hover = None

    def add_score(self):
        self.score += 1
        # Bonus skor tiap X rintangan
        if self.score % score_point_gap == 0:
            self.score += score_point_add
            print(f"Score +{score_point_add} ({self.score})")
        # Tambah kecepatan tiap X rintangan
        if self.score % score_speed_gap == 0:
            if self.speed < max_speed:
                self.speed += score_speed_add
                print(f"Speed +{score_speed_add} ({self.speed})")

    def game_run(self):
        # Posisi game sedang berjalan
        self.state = "RUN"

    def game_pause(self):
        # Posisi game sedang di menu pause
        self.state = "PAUSE"
        # Atur judul dan pilihan menu
        self.hover = None
        self.title = self.title_text[1]
        self.menu = [ self.menu_continue, self.menu_start, self.menu_exit ]

    def game_end(self):
        # Posisi game sedang di menu game over
        print(f"Game over ({self.score})")
        self.state = "DIED"
        # Atur judul dan pilihan menu
        self.hover = None
        self.title = self.title_text[2]
        self.menu = [ self.menu_start, self.menu_exit ]

    def reset(self, display, dino, enemy):
        # Reset skor dan status
        self.__init__()
        self.state = "RUN"
        # Reset posisi dino dan musuh
        dino.reset()
        enemy.reset(display)

    def update(self, display, mouse_pos):
        # Update skor secara terus menerus
        score_text = self.font.render("Skor: " + str(self.score), True, font_color)
        display.blit(score_text, (10, 10))

        # Tampilkan menu pause/game over
        if self.state != "RUN":
            # Ketinggian judul menu
            title_pos_y = 170
            # Ketinggian pilihan menu saat ini
            menu_pos_y = title_pos_y + 70
            # Jarak untuk pilihan menu selanjutnya
            menu_gap = 40
    
            # Tampilkan judul menu
            title_rect = self.title.get_rect(center = (display.get_width() // 2, title_pos_y))
            display.blit(self.title, title_rect)

            # Enumerasi tiap-tiap pilihan menu
            for index, choice in enumerate(self.menu):
                # Dapatkan posisi pilihan ke X pada menu
                choice_rect = choice[0].get_rect(center = (display.get_width() // 2, menu_pos_y))
                # Jika posisi mouse pada pilihan ke X
                if choice_rect.collidepoint(mouse_pos):
                    display.blit(choice[1], choice_rect)
                    self.hover = index
                # Jika posisi mouse dikoordinat lain
                else: display.blit(choice[0], choice_rect)
                # Cegah overlap untuk pilihan menu selanjutnya
                menu_pos_y += menu_gap