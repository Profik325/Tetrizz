from Class_Button import Button
from debug import debug
import pygame
import random


pygame.init()

Screen_Width = 400 * 2   # Constant
Screen_Height = 300 * 2  # Constant

Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
Screen.fill((130, 130, 130))

Main_Font = pygame.font.Font(None, 36)  # Шрифт
Main_Font_Color = (0, 0, 0)  # Цвет шрифта


# Инициализация переменных \/
Running = True
K = 4
n = random.randint(1, 100)
asd = False

Button_sprites_Orange = ['Button_Orange_Normal.png', 'Button_Orange_Hovered.png', 'Button_Orange_Clicked.png']

Buttons = pygame.sprite.Group()

# Инициализация переменных закончена

if n == 1:
    pygame.display.set_caption('Yarik leniviy')
else:
    pygame.display.set_caption('Tetrizz')

pygame.display.flip()  # Screen update


Btn_Start = Button(Screen_Width / 2 - 150, Screen_Height / 2 - 80, 320, 75, Button_sprites_Orange, 'Start', Buttons)  # MAIN BUTTON | X is {Screen_Width / 2 - <Button.width / 2>}, Y is {Screen_Width / 2 - 70}; Button.width is 280, Button.height is {Button.width / 5}
Btn_Records = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24, 240, 48, Button_sprites_Orange, 'My records', Buttons)  # X is the same as for the Start (MAIN) button, but Y is {Screen_Width / 2 + 24 * 1}, and it will be same for all other buttons (If they aren't MAIN as Start button)
Btn_Exit = Button(Screen_Width / 2 - 110, Screen_Height / 2 + 24 * K * 2, 240, 48, Button_sprites_Orange, 'Exit', Buttons)   # everything, except Y, is same as other buttons' args. Y is {Screen_Width / 2 + 24 * K * <[Button's number from the top (MAIN BUTTON is counted too)] - 1>}




# pygame.draw.rect(Screen, Btn_Start.Sprites[1], (Btn_Start.x, Btn_Start.y, Btn_Start.width, Btn_Start.height))  # Button colors: 'normal', 'hover', 'pressed'
# Screen.blit(Btn_Start.Text, (Btn_Start.x + 110, Btn_Start.y + 5.6 * 2.6))  # X is a random number that matches with the button's scale, Y is {Button.y + <0.1 * Button.width> * 2.6}

# Buttons.draw(Screen)

# pygame.draw.rect(Screen, Btn_Exit.Sprites[1], (Btn_Exit.x, Btn_Exit.y, Btn_Exit.width, Btn_Exit.height))
# Screen.blit(Btn_Exit.Text, (Btn_Exit.x + 95, Btn_Exit.y + 4.8 * 2.6))

pygame.display.flip()  # Screen update


clock = pygame.time.Clock()

while Running:
    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            asd = True
            for button in Buttons:
                button.Click()
        elif event.type == pygame.QUIT:
            Running = False
        else:
            pygame.event.get()

    Screen.fill((130, 130, 130))

    Buttons.draw(Screen)

    debug(pygame.mouse.get_pos(), Screen)
    debug(Btn_Start.width > pygame.mouse.get_pos()[0] > Btn_Start.x, Screen, y=30)  # Вот здесь не работает, хотя написано правильно, Тру выводит только в узком прямоугольнике высотой на весь экран, в топлэфте главной кнопки
    debug(pygame.mouse.get_pressed(), Screen, y=60)
    debug(asd and Btn_Start.width > pygame.mouse.get_pos()[0] > Btn_Start.x and Btn_Start.height > pygame.mouse.get_pos()[1] > Btn_Start.y, Screen, y=90)

    asd = False

    pygame.display.update()

    clock.tick(30)  # Setting constant FPS
