import pygame

min_speed = 30
max_speed = 60

class Menu:
    def __init__(self):
        # Skor game
        self.score = 0
        # Status game
        self.state = "DIED"
        # Kecepatan game
        self.speed = min_speed

    def add_score(self):
        self.score += 1
        # Bonus skor tiap 5 rintangan
        if self.score % 5 == 0:
            self.score += 10
            print(f"Game score +10 ({self.score})")
        # Tambah kecepatan tiap 10 rintangan
        if self.score % 30 == 0:
            if self.speed < max_speed:
                self.speed += 3
                print(f"Game speed +3 ({self.speed})")

    def game_run(self):
        # Posisi game sedang berjalan
        self.state = "RUN"

    def game_pause(self):
        # Posisi game sedang di menu pause
        self.state = "PAUSE"

    def game_end(self):
        # Posisi game sedang di menu game over
        print(f"Game over ({self.score})")
        self.state = "DIED"

    def reset(self, display, dino, enemy):
        # Reset skor dan status
        self.__init__()
        self.state = "RUN"
        # Reset posisi dino dan musuh
        dino.reset()
        enemy.reset(display)

    def update(self, display, font):
        # Update skor secara terus menerus
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        display.blit(score_text, (10, 10))

        if self.state == "PAUSE":
            help_text = font.render("Press R to reset or ESC to continue", True, (255, 255, 255))
            help_text_rect = help_text.get_rect()
            help_text_rect.center = (display.get_width() // 2, 70)
            display.blit(help_text, help_text_rect)
        elif self.state == "DIED":
            help_text = font.render("Press ANY KEY to (re)start", True, (255, 255, 255))
            help_text_rect = help_text.get_rect()
            help_text_rect.center = (display.get_width() // 2, 70)
            display.blit(help_text, help_text_rect)