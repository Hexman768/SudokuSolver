import pygame
from SSolver import *

width = 270
height = 270
screen = pygame.display.set_mode((width, height))

screen.fill((255, 255, 255))
pygame.font.init()
pygame.display.flip()
font = pygame.font.SysFont('Comic Sans MS', 12)
BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GRAY = (200,200,200)

def fill_grid():
        for row in board:
                for col in row:
                        text_surface = myfont.render(str(board[row][col]))

def draw_grid():
        cell_size = width / 9
        square_size = width / 3
        # Draw light gray lines
        for x in range(width):
                for y in range(height):
                        rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, LIGHT_GRAY, rect, 1)
        # Draw black lines
        for x in range(width):
                for y in range(height):
                        rect = pygame.Rect(x*square_size, y*square_size, square_size, square_size)
                        pygame.draw.rect(screen, BLACK, rect, 1)

def main():
        pygame.init()
        pygame.display.set_caption('Sudoku Solver')
        clock = pygame.time.Clock()
        running = True
        draw_grid()
        while (running):
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                                running = False
                pygame.display.update()
                clock.tick(10)

if __name__ == '__main__':
        main()
