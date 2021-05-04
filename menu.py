class Menu:
    def __init__(self):
        self.score = 0
        self.state = "RUN"

    def add_score(self, max_fps):
        self.score += 1
        # Bonus skor tiap melewati 5 rintangan
        if self.score % 5 == 0:
            self.score += 10
        if self.score % 30 == 0:
            return max_fps + 3
        return max_fps

    def change_state(self, state):
        self.state = state

    def reset(self, dino, enemy, min_fps):
        self.__init__()
        dino.reset()
        enemy.reset()
        return min_fps

    def update(self, display, font):
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