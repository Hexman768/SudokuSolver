import pygame
from SSolver import *

width = 300
height = 300
screen = pygame.display.set_mode((width, height))

screen.fill((255, 255, 255))
pygame.font.init()
pygame.display.flip()
font = pygame.font.SysFont('Comic Sans MS', 12)

def fill_grid():
        for row in board:
                for col in row:
                        text_surface = myfont.render(str(board[row][col]))

def draw_grid():
        cell_size = 33.33
        for x in range(width):
                for y in range(height):
                        rect = pygame.Rect(x*cell_size, y*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, (0, 0, 0), rect, 1)

def main():
        pygame.init()
        pygame.display.set_caption('Sudoku Solver')
        clock = pygame.time.Clock()
        running = True
        while (running):
                draw_grid()
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                                running = False
                pygame.display.update()
                clock.tick(10)

if __name__ == '__main__':
        main()
