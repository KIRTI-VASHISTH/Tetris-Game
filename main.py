import pygame
import random
from tetris import Piece, create_grid
from constants import *

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris Game")

def draw_window(surface, grid):
    surface.fill(BLACK)

    
    font = pygame.font.SysFont('comicsans', 36)
    label = font.render("Tetris", True, WHITE)
    surface.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, 10))

    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x],
                (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    
    for x in range(COLUMNS):
        pygame.draw.line(surface, GREY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(ROWS):
        pygame.draw.line(surface, GREY, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))

    
    pygame.draw.rect(surface, WHITE, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 4)

def draw_piece(surface, piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, piece.color,
                    ((piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

def main():
    run = True
    clock = pygame.time.Clock()
    current_piece = Piece(5, 0, random.choice(list('SZILJOT')))
    locked_positions = {}

    while run:
        grid = create_grid(locked_positions)
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_piece.y += 1
        if current_piece.y + len(current_piece.shape) > ROWS:
            current_piece.y -= 1
            for i, row in enumerate(current_piece.shape):
                for j, cell in enumerate(row):
                    if cell:
                        locked_positions[(current_piece.x + j, current_piece.y + i)] = current_piece.color
            current_piece = Piece(5, 0, random.choice(list('SZILJOT')))

        draw_window(win, grid)
        draw_piece(win, current_piece)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
