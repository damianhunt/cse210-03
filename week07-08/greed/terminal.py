import pygame


class Terminal:

    def __init__(self):
        self._WIDTH = 900
        self._HEIGHT = 500
        self._WINDOW = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
        self._BLACK = (0, 0, 0)
        self.event = ""
        self.run = True
        self.FPS = 40
        self.clock = pygame.time.Clock()

    def draw_terminal(self):
        pygame.display.set_caption("Greed")
        self._WINDOW.fill(self._BLACK)
        pygame.display.update()

    def activate_terminal(self):
        while self.run:
            self.clock.tick(self.FPS)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.run = False
            self.draw_terminal()
        pygame.quit()
