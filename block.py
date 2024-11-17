import pygame
import consts

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((consts.TILE_SIZE, consts.TILE_SIZE))
        self.image.fill(consts.BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.break_cooldown = 0
        self.break_status = 2

    def destroy(self):
        if self.break_cooldown > 0: return

        self.break_status -= 1
        self.break_cooldown = 20

        if self.break_status == 0:
            self.kill()
        elif self.break_status == 1:
            self.image.fill(consts.BLOCK_DESTROYED_COLOR)

    def update(self):
        if self.break_cooldown > 0:
            self.break_cooldown -= 1

