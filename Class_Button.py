import pygame


pygame.init()
Main_Font = pygame.font.Font(None, 36)  # Шрифт
Main_Font_Color = (0, 0, 0)  # Цвет шрифта
Screen_Width = 400 * 2   # Constant
Screen_Height = 300 * 2  # Constant


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, button_sprites=None, button_text='Button', group=None, on_click_function=None, already_pressed=False):
        pygame.sprite.Sprite.__init__(self)
        self.add(group)
        self.x = x
        self.y = y
        self.width = self.x + width
        self.height = self.y + height
        self.Sprites = button_sprites  # ['normal.png', 'hovered.png', 'pressed.png']
        self.image = pygame.image.load(self.Sprites[0])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        self.Text = Main_Font.render(button_text, True, Main_Font_Color)
        self.Function = on_click_function
        # self.onePress = onePress
        self.Already_pressed = already_pressed

    def Hover(self):
        if self.width > pygame.mouse.get_pos()[0] > self.x and self.height > pygame.mouse.get_pos()[1] > self.y:
            self.image = pygame.image.load(self.Sprites[1])
            pygame.display.flip()
            self.update()

    def Click(self):
        if self.width > pygame.mouse.get_pos()[0] > self.x and self.height > pygame.mouse.get_pos()[1] > self.y:
            # for event in pygame.event.get():
            #     if event.type == pygame.KEYDOWN and event.key == pygame.mouse.get_pressed()[0]:
            self.image = pygame.image.load(self.Sprites[2])
            pygame.display.flip()
            self.update()
            self.Function()
