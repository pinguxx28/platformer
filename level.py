import random
import pygame
import consts

from block import Block

class Level:
    def __init__(self):
        self.screen = pygame.Surface(consts.SCREEN_SIZE)

    def load_resources(self):
        pass

    def reset(self):
        self.blocks = pygame.sprite.Group()

        for y in range(0, consts.SCREEN_SIZE[1], consts.TILE_SIZE):
            for x in range(0, consts.SCREEN_SIZE[0], consts.TILE_SIZE):
                if random.randint(0, 5) == 0:
                    self.blocks.add(Block((x, y)))

    def handle_input(self):
        keys = pygame.key.get_pressed()

    def update(self):
        pass

    def draw(self, window):
        # screen backgruond
        self.screen.fill(consts.SCREEN_COLOR)

        # screen objects
        self.blocks.draw(self.screen)

        # window background => screen => screen border
        window.fill(consts.WINDOW_COLOR) 
        window.blit(self.screen, consts.SCREEN_POS)
        pygame.draw.rect(window, consts.SCREEN_BORDER_COLOR, consts.SCREEN_BORDER_RECT, 2)

