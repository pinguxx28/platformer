import pygame
import consts

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((consts.TILE_SIZE * 0.8, consts.TILE_SIZE * 0.8))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.velocity = pygame.math.Vector2(0, 0)
        self.on_ground = False

    def update(self, blocks):
        self.velocity.y += consts.PLAYER_GRAVITY
        self.velocity.y = min(self.velocity.y, consts.PLAYER_MAX_Y_VELOCITY)
        self.rect.y += self.velocity.y
        self.vertical_collision(blocks)

        self.velocity.x *= consts.PLAYER_X_FRICTION
        self.rect.x += self.velocity.x
        self.horizontal_collision(blocks)

    def jump(self):
        if not self.on_ground: return
        self.velocity.y = consts.PLAYER_JUMP_VELOCITY

    def vertical_collision(self, blocks):
        self.on_ground = False

        for block in blocks:
            if not self.rect.colliderect(block.rect): continue

            if self.velocity.y > 0:
                self.rect.bottom = block.rect.top
                self.on_ground = True
            elif self.velocity.y < 0:
                self.rect.top = block.rect.bottom

            self.velocity.y = 0
            break

    def move_horizontally(self, x_velocity):
        self.velocity.x += x_velocity

    def horizontal_collision(self, blocks):
        for block in blocks:
            if not self.rect.colliderect(block.rect): continue

            if self.velocity.x > 0: # moving right
                self.rect.right = block.rect.left
            elif self.velocity.x < 0: # moving left
                self.rect.left = block.rect.right

            self.velocity.x = 0
            break
