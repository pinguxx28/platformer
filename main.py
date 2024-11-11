import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame
import consts
from level import Level

def main():
    pygame.init()
    window = pygame.display.set_mode(consts.WINDOW_SIZE)
    clock = pygame.time.Clock()

    level = Level()
    level.reset()
    level.load_resources()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        level.handle_input()
        level.update()
        level.draw(window)
        pygame.display.flip()

        clock.tick(consts.FPS)


    pygame.quit()

if __name__ == '__main__':
    main()
