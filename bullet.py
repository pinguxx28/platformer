import pygame
import consts

class Bullet(pygame.sprite.Sprite):
    def __init__(self, center, dir):
        super().__init__()
        self.image = pygame.Surface((consts.BULLET_WIDTH, consts.BULLET_WIDTH))
        self.image.fill(consts.BULLET_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.dir = dir
    
    def update(self, blocks):
        self.rect.centerx += self.dir.x * consts.BULLET_SPEED
        self.rect.centery += self.dir.y * consts.BULLET_SPEED

        # outside of screen
        if self.rect.right < 0 or self.rect.left > consts.SCREEN_SIZE[0]: self.kill()
        if self.rect.bottom < 0 or self.rect.top > consts.SCREEN_SIZE[1]: self.kill()

        if self.collides_with_blocks(blocks):
            self.kill()

    def collides_with_blocks(self, blocks):
        for block in blocks:
            if block.rect.colliderect(self.rect):
                return True

        return False

