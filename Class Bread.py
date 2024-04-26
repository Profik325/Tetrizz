import pygame


class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False
        self.text = buttonText

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

    def Click(self):
        if self.width > pygame.mouse.get_pos()[0] > self.x and self.height > pygame.mouse.get_pos()[1] > self.y:
            # for event in pygame.event.get():
            #     if event.type == pygame.KEYDOWN and event.key == pygame.mouse.get_pressed()[0]:
            self.onclickFunction()
