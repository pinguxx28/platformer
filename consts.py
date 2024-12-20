import pygame

FPS = 60
WINDOW_SIZE  = (800, 600) # w, h
WINDOW_COLOR = pygame.Color(0, 0, 0)

SCREEN_POS   = ( 40,  50) # x, y
SCREEN_SIZE  = (720, 500) # w, h
SCREEN_COLOR = pygame.Color(20, 20, 20)

SCREEN_BORDER_RECT = (SCREEN_POS[0], SCREEN_POS[1], SCREEN_SIZE[0], SCREEN_SIZE[1]) # x, y, w, h
SCREEN_BORDER_COLOR = pygame.Color(200, 200, 200)

TILE_SIZE = 20
TILES_SIZE = (int(SCREEN_SIZE[0] / TILE_SIZE), int(SCREEN_SIZE[1] / TILE_SIZE))

PLAYER_FRICTION = 0.7
PLAYER_ACCELERATION = TILE_SIZE / 20
BREAK_COOLDOWN = 15
SHOOT_COOLDOWN = 15

BLOCK_COLOR = SCREEN_BORDER_COLOR
BLOCK_DESTROYED_COLOR = pygame.Color(180, 180, 180)

BULLET_SPEED = 5
BULLET_WIDTH = TILE_SIZE / 5
BULLET_COLOR = pygame.Color(0, 255, 0)
