import random
import noise
import numpy
import consts

def generate():
    seed = random.randint(0, 1000000)
    map = numpy.zeros((consts.TILES_SIZE[1], consts.TILES_SIZE[0]), dtype=int)

    for y in range(consts.TILES_SIZE[1]):
        for x in range(consts.TILES_SIZE[0]):
            noise_value = noise.snoise2(x * 0.1, y * 0.2, base=seed)
            if noise_value > 0.0: map[y][x] = 1

    return map
