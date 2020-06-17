import pygame, sys
from SSolver import *

width = 270
height = 270
screen = pygame.display.set_mode((width, height))

screen.fill((255, 255, 255))
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 12)

BLACK = (0,0,0)
WHITE = (255,255,255)
LIGHT_GRAY = (200,200,200)
BLUE = (0,0,255)

square_size = width / 3
cell_size = square_size / 3
num_size = cell_size / 3

def initiate_grid():
        CG = {}
        fullCell = [1,2,3,4,5,6,7,8,9]
        for x in range(0,9):
                for y in range(0,9):
                        CG[x,y] = list(fullCell)
        return CG

def populate_cells(cell_info, x, y):
        cell_surf = BASICFONT.render('%s' %(cell_info), True, LIGHT_GRAY)
        cell_rect = cell_surf.get_rect()
        cell_rect.topleft = (x, y)
        screen.blit(cell_surf, cell_rect)

def draw_box(mx, my):
        bx = ((mx*27) / width) * (num_size)
        by = ((my*27) / height) * (num_size)
        pygame.draw.rect(screen, BLUE, (bx, by, num_size, num_size), 1)

def display_cells(CG):
        xOffset = 0
        yOffset = 0
        for item in CG:
                cell_info = CG[item]
                for number in cell_info:
                        if number != ' ':
                                xOffset = ((number-1)%3)
                                if number <= 3:
                                        yOffset = 0
                                elif number <=6:
                                        yOffset = 1
                                else:
                                        yOffset = 2
                                populate_cells(number, (item[0]*cell_size)+(xOffset*num_size),(item[1]*cell_size)+(yOffset*num_size))
        return None

def draw_grid():
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
        global BASICFONT, BASICFONTSIZE
        BASICFONTSIZE = 15
        BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
        clock = pygame.time.Clock()
        fps = 30
        mouse_clicked = False
        m_x = 0 # mouse x value
        m_y = 0 # mouse y value
        CG = initiate_grid()
        display_cells(CG)
        draw_grid()
        while True:
                mouse_clicked = False
                for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                                pygame.quit()
                                sys.exit()
                        elif (event.type == pygame.MOUSEMOTION):
                                m_x, m_y = event.pos
                        elif (event.type == pygame.MOUSEBUTTONUP):
                                m_x, m_y = event.pos
                                mouse_clicked = True
                if (mouse_clicked == True):
                        print(m_x)
                        print(m_y)
                # repaint the screen
                screen.fill(WHITE)
                display_cells(CG)
                draw_grid()
                draw_box(m_x, m_y)
                pygame.display.update()
                clock.tick(fps)

if __name__ == '__main__':
        main()

