import pygame
import consts

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((consts.TILE_SIZE, consts.TILE_SIZE))
        self.image.fill(consts.SCREEN_BORDER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

