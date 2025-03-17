import os
from pathlib import Path

from pycparser.c_ast import Return
from pygame import USEREVENT

from Spritesheet import Spritesheet

os.environ['SDL_VIDEO_CENTERED'] = '0'  # смещение окна по центру крана / центрирование

from Cls_Button import Button
import pygame
from random import randint, choice
from MainBoard import Board

pygame.init()
pygame.font.init()

font = pygame.font.Font('PixelizerBold.ttf', 55)
little_font = pygame.font.Font('PixelizerBold.ttf', 30)

Screen_Width = 400 * 3   # Not constant
Screen_Height = 200 * 3  # Not constant

Screen = pygame.display.set_mode((Screen_Width, Screen_Height), vsync=1)

# Инициализация переменных \/
Running = True
K = 4
n = randint(1, 100)
Started = False
frame_number = 0
frame = 0

GameTitle = pygame.image.load("Tetris_logo.png").convert_alpha()

Button_sprites_Red = ['Button_Red_Standart_START(tetris style)_512x128.png', 'Button_Red_Highlighted_START(tetris style)_512x128.png', 'Button_Red_Clicked_START(tetris style)_512x128.png']
Button_sprites_Gray = ['Button_Gray_Standart_EXIT(tetris style)_384x98.png', 'Button_Gray_Highlighted_EXIT(tetris style)_384x98.png', 'Button_Gray_Clicked_EXIT(tetris style)_384x98.png']
Button_sprites_Return = ['Button_Gray_Standart_RETURN(tetris style)_96x48.png', 'Button_Gray_Highlighted_RETURN(tetris style)_96x48.png', 'Button_Gray_Clicked_RETURN(tetris style)_96x48.png']

Buttons = pygame.sprite.Group() 
Buttons_2nd_screen = pygame.sprite.Group()

Lobby_music = ['A-lobbymusic.mp3', 'B-lobbymusic.mp3',
                'C-lobbymusic.mp3']
pygame.mixer.music.load(choice(Lobby_music))
pygame.mixer.music.play()

# Инициализация переменных закончена

# Инициализация функций

def Start_BtnFunc():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Button_clicked.mp3')
    pygame.mixer.music.play()
    global Started
    Started = True
    global Screen_Width, Screen_Height
    Screen_Width = 600
    Screen_Height = 800
    pygame.display.set_mode((Screen_Width, Screen_Height))
    board.start()


def Exit_BtnFunc():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Button_clicked.mp3')
    pygame.mixer.music.play()
    global Running
    Running = False

def Return_BtnFunc():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Button_clicked.mp3')
    pygame.mixer.music.play()
    global Started
    Started = False
    global Screen_Width, Screen_Height
    Screen_Width = 400 * 3
    Screen_Height = 200 * 3
    pygame.display.set_mode((Screen_Width, Screen_Height))
    global board
    board = Board(Screen)

# Инициализация функций закончена


if n == 1:
    pygame.display.set_caption('Tetrizz')
else:
    pygame.display.set_caption('Tetris')

pygame.display.flip()  # Screen update


board = Board(Screen)



Btn_Start = Button(Screen_Width / 2 - 256, Screen_Height / 2 - 64 + 35, Button_sprites_Red, 'Start', onclickFunction=Start_BtnFunc)  # MAIN BUTTON | X is {Screen_Width / 2 - <Button.width / 2>}, Y is {Screen_Width / 2 - 70}; Button.width is 280, Button.height is {Button.width / 5}
Btn_Exit = Button(Screen_Width / 2 - 192, Screen_Height / 2 - 49 + 230, Button_sprites_Gray, 'Exit', onclickFunction=Exit_BtnFunc)  # MAIN BUTTON | X is {Screen_Width / 2 - <Button.width / 2>}, Y is {Screen_Width / 2 - 70}; Button.width is 280, Button.height is {Button.width / 5}

'''Btn_Records = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24, 240, 48, Button_sprites_Orange, 'My records', Buttons)  # X is the same as for the Start (MAIN) button, but Y is {Screen_Width / 2 + 24 * 1}, and it will be same for all other buttons (If they aren't MAIN as Start button)
Btn_Exit = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24 * K * 2, 240, 48, Button_sprites_Orange, 'Exit', Buttons)   # everything, except Y, is same as other buttons' args. Y is {Screen_Width / 2 + 24 * K * <[Button's number from the top (MAIN BUTTON is counted too)] - 1>}
'''

Btn_Return = Button(15, 730, Button_sprites_Return, 'Return', onclickFunction=Return_BtnFunc)

Buttons.add(Btn_Start)
Buttons.add(Btn_Exit)
Buttons_2nd_screen.add(Btn_Return)

pygame.display.flip()  # Screen update

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 10000)
counter = 4
while Running:
    Screen.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            board.col_selected = 4
            board.figure_rotation += 1
            board.figure_rotation = 1 if board.figure_rotation == 5 else board.figure_rotation
            board.current_figure_ss = board.get_spritesheet(board.current_figure)

        elif event.type == USEREVENT and Started == True:
            counter -= 1

        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or counter == 0:
            counter = 4
            if board.drop_down():
                frame_number = 0
                board.col_selected = 4
            else:
                Return_BtnFunc()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:  # move the figure left
            board.col_selected -= 1 if board.col_selected != 0 else 0

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # move the figure right
                    # ..................................................
            if board.current_figure == 2 or board.current_figure == 3 or board.current_figure == 7:
                if board.figure_rotation in (1, 3):
                    board.col_selected += 1 if board.col_selected != 7 else 0
                else:
                    board.col_selected += 1 if board.col_selected != 8 else 0
                    # ..................................................
            elif board.current_figure == 1:
                board.col_selected += 1 if board.col_selected != 8 else 0
                    # ..................................................
            elif board.current_figure == 5 or board.current_figure == 6:
                if board.figure_rotation in (1, 3):
                    board.col_selected += 1 if board.col_selected != 8 else 0
                else:
                    board.col_selected += 1 if board.col_selected != 7 else 0
                    # ..................................................
            else:
                if board.figure_rotation in (1, 3):
                    board.col_selected += 1 if board.col_selected != 9 else 0
                else:
                    board.col_selected += 1 if board.col_selected != 6 else 0
                    # ..................................................

        if event.type == pygame.QUIT:
            Running = False
        else:
            pass
            # pygame.event.get()

    if Started is False:
        Buttons.update()
        for N in Buttons:
            N.process()
            Screen.blit(N.current_sprite, N.sprite_rect)
            Screen.blit(GameTitle, GameTitle.get_rect(topleft=(232, 44)))
    else:
        Screen.fill((100, 100, 100))
        Buttons_2nd_screen.update()
        for N in Buttons_2nd_screen:
            N.process()
            Screen.blit(N.current_sprite, N.sprite_rect)
            if not Started:
                continue
        if Started:
            sprites = board.current_figure_ss.get_sprites(((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                                                       (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
                                                       (10, 0), (11, 0), (12, 0), (13, 0), (14, 0),
                                                       (15, 0), (16, 0), (17, 0)))
            board.render()
            board.render_cells()
            Screen.blit(sprites[frame_number // 10], board.get_cell_coords(board.col_selected, 0))
            frame_number += 2
            frame_number %= 170
            frame_number %= 1700
            # Screen.blit(fig, fig.get_rect())
            board.tetris()
            if board.play_tetris is True:
                y = 400 if board.started_tetris else y
                tetris_frame_number = 0 if board.started_tetris else tetris_frame_number
                tetris_frame_count = 0 if board.started_tetris else tetris_frame_count
                board.started_tetris = False
                tetris_sprites = Spritesheet(Path('tetris!_ss.png'), (174, 38)).get_sprites([
                    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
                    (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)])
                Screen.blit(tetris_sprites[tetris_frame_count], (130, y))
                tetris_frame_number += 1
                y -= 1
                if tetris_frame_number % 3 == 0:
                    tetris_frame_count += 1
                if tetris_frame_count == 42:
                    board.play_tetris = False


            if board.scorelist:
                number_number = 0  # literally a number of the number displayed
                text = font.render(str(sum(board.scorelist)), False, (255, 255, 255))
                Screen.blit(text, (455, 390))
                for beta in board.scorelist[::-1]:
                    text = little_font.render(str(beta), False, (160, 160, 160))
                    Screen.blit(text, (475, 400 + 30 * (number_number + 1) + 10))
                    number_number += 1
                    if number_number == 4:
                        break

    pygame.display.flip()

    clock.tick(60) # constant
