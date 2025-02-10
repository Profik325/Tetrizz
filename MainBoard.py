from random import choice
import pygame
from pathlib import Path
from Spritesheet import Spritesheet


class Board:
    # создание поля
    def __init__(self, screen):
        self.scorelist = []
        self.started_tetris = False
        self.play_tetris = False
        self.score = 0
        self.width = 10  # width
        self.height = 16  # height
        self.board = [
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']],
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']]]

        # значения по умолчанию
        self.left = 50
        self.top = 30
        self.cell_size = 34
        self.figures_sss = [Path('figure_1-yellow_ss.png'), Path('figure_2-red_ss.png'),
                            Path('figure_3-green_ss.png'), Path('figure_4-cyan_ss.png'),
                            Path('figure_5-blue_ss.png'), Path('figure_6-orange_ss.png'),
                            Path('figure_7-purple_ss.png')]
        self.figures = [1, 2, 3, 4, 5, 6, 7] # 7th figure is broken and i couldn't solve the bug spendding hours and hour
        self.current_figure_ss = None
        self.Screen = screen
        self.figure_rotation = 1  # may be 1 or 2 or 3 or 4

        # 1: X X    2: X X      3:   X X    4: X    5: X X    6: X X    7:   X
        #    X X         X X       X X         X       X           X       X X X    - 1 rotation
        #                                      X       X           X
        #                                      X
        #
        #    X X         X         X        X X X X    X X X         X     X
        #    X X       X X         X X                     X     X X X     X X      - 2 rotation
        #              X             X                                     X
        #
        #    X X       X X           X X       X         X       X         X X X    - 3 rotation
        #    X X         X X       X X         X         X       X           X
        #                                      X       X X       X X
        #                                      X
        #
        #    X X         X         X        X X X X    X         X X X       X
        #    X X       X X         X X                 X X X     X         X X      - 4 rotation
        #              X             X                                       X
        #
        #
        #

        self.figure_1_tile = pygame.image.load("figure_1-yellow.png").convert_alpha()
        self.figure_2_tile = pygame.image.load("figure_2-red.png").convert_alpha()
        self.figure_3_tile = pygame.image.load("figure_3-green.png").convert_alpha()
        self.figure_4_tile = pygame.image.load("figure_4-cyan.png").convert_alpha()
        self.figure_5_tile = pygame.image.load("figure_5-blue.png").convert_alpha()
        self.figure_6_tile = pygame.image.load("figure_6-orange.png").convert_alpha()
        self.figure_7_tile = pygame.image.load("figure_7-purple.png").convert_alpha()


    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.Screen, (130, 130, 130), (1 * x * self.cell_size + self.left,
                                                   1 * y * self.cell_size + self.top, 1 * self.cell_size,
                                                                1 * self.cell_size), width=1)
                pygame.draw.rect(self.Screen, 'black', (self.left - 1, self.top - 1,
                                                        1 * 10 * self.cell_size + 1, 1 * 16 * self.cell_size + 2),
                                 width=2)
        pygame.draw.rect(self.Screen, 'black', (410, 375, 170, 199), width=2)

    def render_cells(self):
        Y = 0
        for y in self.board:
            X = 0
            for x in y:
                if x[0] == 1:
                    self.Screen.blit(x[2], self.get_cell_coords(X, Y))
                X += 1
            Y += 1

    def get_cell_coords(self, cell_x, cell_y):
        if cell_y == 0:
            return self.left + cell_x * 34 + 1, 31
        return self.left + cell_x * 34 + 1, self.top + cell_y * 34 + 1

    def next_figure(self, fig):
        return choice(fig)

    def start(self):
        self.col_selected, self.row = 4, 0
        rotation = 1  # 1: standard; 2: non-standard (vertical)
        self.current_figure = self.next_figure(self.figures)
        self.current_figure_ss = self.get_spritesheet(self.current_figure)

    def fill_cells(self, row, col, sprite):
        self.board[row][col][0] = 1
        self.board[row][col][2] = sprite

    def get_spritesheet(self, current_figure):
        match current_figure:
            case 1:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (66, 66),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 2:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (100, 66),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 3:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (100, 66),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 4:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (32, 134),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 5:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (66, 100),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 6:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (66, 100),
                                   rotation=(self.figure_rotation - 1) * 90)
            case 7:
                return Spritesheet(self.figures_sss[self.current_figure - 1], (100, 66),
                                   rotation=(self.figure_rotation - 1) * 90)
        
    def cells_check_n_reg(self, figure, row, col):
        match figure:
            case 1:
                if self.board[row - 1][col][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                        and self.board[row][col][0] == 0 and \
                        self.board[row][col + 1][0] == 0 and row > -1:
                    self.fill_cells(row - 1, col, self.figure_1_tile)
                    self.fill_cells(row - 1, col + 1, self.figure_1_tile)
                    self.fill_cells(row, col, self.figure_1_tile)
                    self.fill_cells(row , col + 1, self.figure_1_tile)
                    return True

            case 2:
                if self.figure_rotation in (1, 3):
                    if self.board[row - 1][col][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                            and self.board[row][col + 1][0] == 0 and \
                            self.board[row][col + 2][0] == 0 and row - 1 > -1:
                        self.fill_cells(row - 1, col, self.figure_2_tile)
                        self.fill_cells(row - 1, col + 1, self.figure_2_tile)
                        self.fill_cells(row, col + 1, self.figure_2_tile)
                        self.fill_cells(row, col + 2, self.figure_2_tile)
                        return True
                else:
                    if self.board[row - 2][col + 1][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                            and self.board[row - 1][col][0] == 0 and \
                            self.board[row][col][0] == 0 and row - 2 > -1:
                        self.fill_cells(row - 2, col + 1, self.figure_2_tile)
                        self.fill_cells(row - 1, col + 1, self.figure_2_tile)
                        self.fill_cells(row - 1, col, self.figure_2_tile)
                        self.fill_cells(row, col, self.figure_2_tile)
                        return True

            case 3:
                if self.figure_rotation in (1, 3):
                    if self.board[row][col][0] == 0 and self.board[row][col + 1][0] == 0 \
                            and self.board[row - 1][col + 1][0] == 0 and \
                            self.board[row - 1][col + 2][0] == 0 and row - 1 > -1:
                        self.fill_cells(row - 1, col + 1, self.figure_3_tile)
                        self.fill_cells(row - 1, col + 2, self.figure_3_tile)
                        self.fill_cells(row, col, self.figure_3_tile)
                        self.fill_cells(row, col + 1, self.figure_3_tile)
                        return True
                else:
                    if self.board[row - 2][col][0] == 0 and self.board[row - 1][col][0] == 0 \
                            and self.board[row - 1][col + 1][0] == 0 and \
                            self.board[row][col + 1][0] == 0 and row - 2 > -1:
                        self.fill_cells(row - 2, col, self.figure_3_tile)
                        self.fill_cells(row - 1, col, self.figure_3_tile)
                        self.fill_cells(row - 1, col + 1, self.figure_3_tile)
                        self.fill_cells(row, col + 1, self.figure_3_tile)
                        return True

            case 4:
                if self.figure_rotation in (1, 3):
                    if self.board[row][col][0] == 0 and self.board[row - 1][col][0] == 0 \
                            and self.board[row - 2][col][0] == 0 and \
                            self.board[row - 3][col][0] == 0 and row - 3 > -1:
                        self.fill_cells(row - 3, col, self.figure_4_tile)
                        self.fill_cells(row - 2, col, self.figure_4_tile)
                        self.fill_cells(row - 1, col, self.figure_4_tile)
                        self.fill_cells(row, col, self.figure_4_tile)
                        return True
                else:
                    if self.board[row][col][0] == 0 and self.board[row][col + 1][0] == 0 \
                            and self.board[row][col + 2][0] == 0 and \
                            self.board[row][col + 3][0] == 0 and row > -1:
                        self.fill_cells(row, col + 3, self.figure_4_tile)
                        self.fill_cells(row, col + 2, self.figure_4_tile)
                        self.fill_cells(row, col + 1, self.figure_4_tile)
                        self.fill_cells(row, col, self.figure_4_tile)
                        return True

            case 5:
                match self.figure_rotation:
                    case 1:
                        if self.board[row - 2][col][0] == 0 and self.board[row - 2][col + 1][0] == 0 \
                                and self.board[row - 1][col][0] == 0 and \
                                self.board[row][col][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col + 1, self.figure_5_tile)
                            self.fill_cells(row - 2, col, self.figure_5_tile)
                            self.fill_cells(row - 1, col, self.figure_5_tile)
                            self.fill_cells(row, col, self.figure_5_tile)
                            return True
                    case 2:
                        if self.board[row - 1][col][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                                and self.board[row - 1][col + 2][0] == 0 and \
                                self.board[row][col + 2][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col + 2, self.figure_5_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_5_tile)
                            self.fill_cells(row - 1, col, self.figure_5_tile)
                            self.fill_cells(row, col + 2, self.figure_5_tile)
                            return True
                    case 3:
                        if self.board[row - 2][col + 1][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                                and self.board[row][col + 1][0] == 0 and \
                                self.board[row][col][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col + 1, self.figure_5_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_5_tile)
                            self.fill_cells(row, col + 1, self.figure_5_tile)
                            self.fill_cells(row, col, self.figure_5_tile)
                            return True
                    case 4:
                        if self.board[row - 1][col][0] == 0 and self.board[row][col][0] == 0 \
                                and self.board[row][col + 1][0] == 0 and \
                                self.board[row][col + 2][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col, self.figure_5_tile)
                            self.fill_cells(row, col, self.figure_5_tile)
                            self.fill_cells(row, col + 1, self.figure_5_tile)
                            self.fill_cells(row, col + 2, self.figure_5_tile)
                            return True
            case 6:
                match self.figure_rotation:
                    case 1:
                        if self.board[row - 2][col][0] == 0 and self.board[row - 2][col + 1][0] == 0 \
                                and self.board[row - 1][col + 1][0] == 0 and \
                                self.board[row][col + 1][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col, self.figure_6_tile)
                            self.fill_cells(row - 2, col + 1, self.figure_6_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_6_tile)
                            self.fill_cells(row, col + 1, self.figure_6_tile)
                            return True
                    case 2:
                        if self.board[row - 1][col + 2][0] == 0 and self.board[row][col + 1][0] == 0 \
                                and self.board[row][col + 2][0] == 0 and \
                                self.board[row][col][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col + 2, self.figure_6_tile)
                            self.fill_cells(row, col, self.figure_6_tile)
                            self.fill_cells(row, col + 1, self.figure_6_tile)
                            self.fill_cells(row, col + 2, self.figure_6_tile)
                            return True
                    case 3:
                        if self.board[row - 2][col][0] == 0 and self.board[row - 1][col][0] == 0 \
                                and self.board[row][col][0] == 0 and \
                                self.board[row][col + 1][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col, self.figure_6_tile)
                            self.fill_cells(row - 1, col, self.figure_6_tile)
                            self.fill_cells(row, col, self.figure_6_tile)
                            self.fill_cells(row, col + 1, self.figure_6_tile)
                            return True
                    case 4:
                        if self.board[row - 1][col][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                                and self.board[row - 1][col + 2][0] == 0 and \
                                self.board[row][col][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col, self.figure_6_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_6_tile)
                            self.fill_cells(row - 1, col + 2, self.figure_6_tile)
                            self.fill_cells(row, col, self.figure_6_tile)
                            return True

            case 7:
                match self.figure_rotation:
                    case 1:
                        if self.board[row - 1][col + 1][0] == 0 and self.board[row][col][0] == 0 \
                                and self.board[row][col + 1][0] == 0 and \
                                self.board[row][col + 2][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col + 1, self.figure_7_tile)
                            self.fill_cells(row, col, self.figure_7_tile)
                            self.fill_cells(row, col + 1, self.figure_7_tile)
                            self.fill_cells(row, col + 2, self.figure_7_tile)
                            return True
                    case 2:
                        if self.board[row - 2][col][0] == 0 and self.board[row - 1][col][0] == 0 \
                                and self.board[row][col][0] == 0 and \
                                self.board[row - 1][col + 1][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col, self.figure_7_tile)
                            self.fill_cells(row - 1, col, self.figure_7_tile)
                            self.fill_cells(row, col, self.figure_7_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_7_tile)
                            return True
                    case 3:
                        if self.board[row - 1][col][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                                and self.board[row - 1][col + 2][0] == 0 and \
                                self.board[row][col + 1][0] == 0 and row - 1 > -1:
                            self.fill_cells(row - 1, col + 2, self.figure_7_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_7_tile)
                            self.fill_cells(row - 1, col, self.figure_7_tile)
                            self.fill_cells(row, col + 1, self.figure_7_tile)
                            return True
                    case 4:
                        if self.board[row - 2][col + 1][0] == 0 and self.board[row - 1][col + 1][0] == 0 \
                                and self.board[row][col + 1][0] == 0 and \
                                self.board[row - 1][col][0] == 0 and row - 2 > -1:
                            self.fill_cells(row - 2, col + 1, self.figure_7_tile)
                            self.fill_cells(row - 1, col + 1, self.figure_7_tile)
                            self.fill_cells(row, col + 1, self.figure_7_tile)
                            self.fill_cells(row - 1, col, self.figure_7_tile)
                            return True
        return False

    def drop_down(self):
        row = 15
        while True:
            if self.cells_check_n_reg(self.current_figure, row, self.col_selected):
                self.current_figure = self.alpha()
                self.current_figure_ss = self.get_spritesheet(self.current_figure)
                return True
            row -= 1
            if row == -1:

                return False

    def tetris(self):
        tetris_count = 0
        for y in self.board:
            counter = 0
            for x in y:
                if x[0] == 1:
                    counter += 1
            if counter == 10:
                self.board.pop(-1)
                tetris_count += 1
                self.score += 100
                self.scorelist.append(100)
                self.board.insert(0,
[[0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface'], [0, 0, 'tile:pygame.Surface']])
                if tetris_count == 4:
                    tetris_count = 0
                    self.score += 500
                    self.scorelist.remove(100)
                    self.scorelist.remove(100)
                    self.scorelist.remove(100)
                    self.scorelist.remove(100)
                    self.scorelist.append(500)
                    self.play_tetris = True
                    self.started_tetris = True

    # \/ Функции, использованные всего два или три раза, поэтому не имеющие специального названия \/

    def alpha(self):
        n_figure = self.next_figure(self.figures)
        if n_figure != self.current_figure:
            return n_figure
        else:
            return self.alpha()

                    
                        


