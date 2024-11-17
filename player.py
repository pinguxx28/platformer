import pygame
import consts

from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((consts.TILE_SIZE * 0.8, consts.TILE_SIZE * 0.8))
        self.image.fill("red")

        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.velocity = pygame.math.Vector2(0, 0)
        self.facing = pygame.math.Vector2(1, 0)

        self.shoot_cooldown = 0

    def update(self, blocks):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        diagonal_multiplier = 1
        if self.velocity.y != 0 and self.velocity.x != 0:
            diagonal_multiplier = 0.707

        self.velocity.y *= consts.PLAYER_FRICTION
        self.rect.y += self.velocity.y * diagonal_multiplier
        self.vertical_collision(blocks)

        self.velocity.x *= consts.PLAYER_FRICTION
        self.rect.x += self.velocity.x * diagonal_multiplier
        self.horizontal_collision(blocks)

    def move_vertically(self, y_velocity):
        self.velocity.y += y_velocity
        self.facing = pygame.math.Vector2(0, y_velocity)

    def vertical_collision(self, blocks):
        self.on_ground = False

        for block in blocks:
            if not self.rect.colliderect(block.rect): continue

            if self.velocity.y > 0: # moving down
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            self.velocity.y = 0
            break

    def move_horizontally(self, x_velocity):
        self.velocity.x += x_velocity
        self.facing = pygame.math.Vector2(x_velocity, 0)

    def horizontal_collision(self, blocks):
        for block in blocks:
            if not self.rect.colliderect(block.rect): continue

            if self.velocity.x > 0: # moving right
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

            self.velocity.x = 0
            break

    def draw_facing(self, screen):
        facing = pygame.math.Vector2(
                self.rect.centerx + self.facing.x * (self.rect.width / 2),
                self.rect.centery + self.facing.y * (self.rect.height / 2))

        pygame.draw.circle(screen, "red", facing, 3)

    def mine_block(self, blocks):
        pos = pygame.math.Vector2(
                self.rect.centerx + self.facing.x * self.rect.width,
                self.rect.centery + self.facing.y * self.rect.height)

        map = pygame.math.Vector2(
                int(pos.x / consts.TILE_SIZE) * consts.TILE_SIZE,
                int(pos.y / consts.TILE_SIZE) * consts.TILE_SIZE)

        for block in blocks:
            if block.rect.topleft == map:
                block.destroy()

    def shoot(self, bullets):
        if self.shoot_cooldown > 0: return

        bullets.add(Bullet(self.rect.center, self.facing))
        self.shoot_cooldown = 20


