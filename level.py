import consts
import pygame

class Level:
    def __init__(self):
        self.screen = pygame.Surface(consts.SCREEN_SIZE)

    def load_resources(self):
        pass

    def reset(self):
        pass

    def handle_input(self):
        keys = pygame.key.get_pressed()

    def update(self):
        pass

    def draw(self, window):
        # screen backgruond
        self.screen.fill(consts.SCREEN_COLOR)

        # screen objects
        # -------------

        # window background => screen => screen border
        window.fill(consts.WINDOW_COLOR) 
        window.blit(self.screen, consts.SCREEN_POS)
        pygame.draw.rect(window, consts.SCREEN_BORDER_COLOR, consts.SCREEN_BORDER_RECT, 2)

