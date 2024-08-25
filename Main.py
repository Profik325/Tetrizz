# from Class_Button import Button
from Cls_Button import Button
from Cls_Button import objects
from debug import debug
import pygame
import random


pygame.init()

Screen_Width = 400 * 3   # Constant
Screen_Height = 200 * 3  # Constant

Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
# Screen.fill((130, 130, 130))

Main_Font = pygame.font.Font(None, 36)  # Шрифт
Main_Font_Color = (0, 0, 0)  # Цвет шрифта


# Инициализация переменных \/
Running = True
K = 4
n = random.randint(1, 100)
Started = False

GameTitle = pygame.image.load("Tetris_logo.png").convert_alpha()

Button_sprites_Red = ['Button_Red_Standart_START(tetris style)_512x128.png', 'Button_Red_Highlighted_START(tetris style)_512x128.png', 'Button_Red_Clicked_START(tetris style)_512x128.png']
Button_sprites_Gray = ['Button_Gray_Standart_EXIT(tetris style)_384x98.png', 'Button_Gray_Highlighted_EXIT(tetris style)_384x98.png', 'Button_Gray_Clicked_EXIT(tetris style)_384x98.png']

Buttons = pygame.sprite.Group() 


# Инициализация переменных закончена

# Инициализация функций

def Start_BtnFunc():
    global Started
    Started = True

def Exit_BtnFunc():
    global Running
    Running = False

# Инициализация функций закончена


if n == 1:
    pygame.display.set_caption('Yarik leniviy')
else:
    pygame.display.set_caption('Tetrizz')

pygame.display.flip()  # Screen update





Btn_Start = Button(Screen_Width / 2 - 256, Screen_Height / 2 - 64 + 50, Button_sprites_Red, 'Start', onclickFunction=Start_BtnFunc)  # MAIN BUTTON | X is {Screen_Width / 2 - <Button.width / 2>}, Y is {Screen_Width / 2 - 70}; Button.width is 280, Button.height is {Button.width / 5}
Btn_Exit = Button(Screen_Width / 2 - 192, Screen_Height / 2 - 49 + 200, Button_sprites_Gray, 'Exit', onclickFunction=Exit_BtnFunc)  # MAIN BUTTON | X is {Screen_Width / 2 - <Button.width / 2>}, Y is {Screen_Width / 2 - 70}; Button.width is 280, Button.height is {Button.width / 5}

'''Btn_Records = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24, 240, 48, Button_sprites_Orange, 'My records', Buttons)  # X is the same as for the Start (MAIN) button, but Y is {Screen_Width / 2 + 24 * 1}, and it will be same for all other buttons (If they aren't MAIN as Start button)
Btn_Exit = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24 * K * 2, 240, 48, Button_sprites_Orange, 'Exit', Buttons)   # everything, except Y, is same as other buttons' args. Y is {Screen_Width / 2 + 24 * K * <[Button's number from the top (MAIN BUTTON is counted too)] - 1>}
'''



# pygame.draw.rect(Screen, Btn_Start.Sprites[1], (Btn_Start.x, Btn_Start.y, Btn_Start.width, Btn_Start.height))  # Button colors: 'normal', 'hover', 'pressed'
# Screen.blit(Btn_Start.Text, (Btn_Start.x + 110, Btn_Start.y + 5.6 * 2.6))  # X is a random number that matches with the button's scale, Y is {Button.y + <0.1 * Button.width> * 2.6}

# Buttons.draw(Screen)

# pygame.draw.rect(Screen, Btn_Exit.Sprites[1], (Btn_Exit.x, Btn_Exit.y, Btn_Exit.width, Btn_Exit.height))
# Screen.blit(Btn_Exit.Text, (Btn_Exit.x + 95, Btn_Exit.y + 4.8 * 2.6))

Buttons.add(Btn_Start)
Buttons.add(Btn_Exit)

pygame.display.flip()  # Screen update




clock = pygame.time.Clock()

while Running:
    for event in pygame.event.get():
        for button in Buttons:
            button.process()
        if event.type == pygame.QUIT:
            Running = False
        else:
            pygame.event.get()

    Screen.fill((130, 130, 130))
    Screen.blit(GameTitle, GameTitle.get_rect(topleft = (232, 44)))
    Buttons.update()
    for X in Buttons:
        if Started is False:
            Screen.blit(X.current_sprite, X.sprite_rect)

    #debug(pygame.mouse.get_pos(), Screen)
    #debug(Btn_Start.sprite_rect.collidepoint(pygame.mouse.get_pos()), Screen, y=35)  # Вот здесь не работает, хотя написано правильно, Тру выводит только в узком прямоугольнике высотой на весь экран, в топлэфте главной кнопки
    #debug(pygame.mouse.get_pressed(), Screen, y=60)
    #debug(Started, Screen, y=85)
    # debug(asd, Screen, y=110)
    # debug(asd and Btn_Start.width > pygame.mouse.get_pos()[0] > Btn_Start.x and Btn_Start.height > pygame.mouse.get_pos()[1] > Btn_Start.y, Screen, y=90)

    pygame.display.flip()

    clock.tick(60)  # Setting constonant FPS
