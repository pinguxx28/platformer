import random
import pygame
import consts

from block import Block
from player import Player

class Level:
    def __init__(self):
        self.screen = pygame.Surface(consts.SCREEN_SIZE)

    def load_resources(self):
        pass

    def reset(self):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle(Player((consts.SCREEN_SIZE[0] / 2, consts.SCREEN_SIZE[1] / 2)))

        # random block generation
        for y in range(0, consts.SCREEN_SIZE[1], consts.TILE_SIZE):
            for x in range(0, consts.SCREEN_SIZE[0], consts.TILE_SIZE):
                if random.randint(0, 5) != 0: continue
                self.blocks.add(Block((x, y)))

        # floor
        for x in range(0, consts.SCREEN_SIZE[0], consts.TILE_SIZE):
            self.blocks.add(Block((x, consts.SCREEN_SIZE[1])))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: self.player.sprite.jump()
        if keys[pygame.K_RIGHT]: self.player.sprite.move_horizontally( consts.PLAYER_X_ACCELERATION)
        if keys[pygame.K_LEFT ]: self.player.sprite.move_horizontally(-consts.PLAYER_X_ACCELERATION)

    def update(self):
        self.player.update(self.blocks)

    def draw(self, window):
        # screen backgruond
        self.screen.fill(consts.SCREEN_COLOR)

        # screen objects
        self.blocks.draw(self.screen)
        self.player.draw(self.screen)

        # window background => screen => screen border
        window.fill(consts.WINDOW_COLOR) 
        window.blit(self.screen, consts.SCREEN_POS)
        pygame.draw.rect(window, consts.SCREEN_BORDER_COLOR, consts.SCREEN_BORDER_RECT, 2)
