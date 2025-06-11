import pygame
import random
from constants import *

SHAPES = {
    'S': [[1, 1, 0],
          [0, 1, 1]],
    'Z': [[0, 1, 1],
          [1, 1, 0]],
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]]
}

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = SHAPES[shape]
        self.shape_key = shape
        self.color = COLORS[list(SHAPES.keys()).index(shape)]

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid
