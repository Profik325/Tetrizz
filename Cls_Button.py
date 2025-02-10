import pygame


pygame.init()
pygame.mixer.init()

objects = []

class Button(pygame.sprite.Sprite): 
    def __init__(self, x, y, images, buttonText='Button', onclickFunction=None):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        # self.width = width
        # self.height = height
        self.onclickFunction = onclickFunction

        self.sprites = images
        self.normal = pygame.image.load(self.sprites[0]).convert_alpha()
        self.hovered = pygame.image.load(self.sprites[1]).convert_alpha()
        self.clicked = pygame.image.load(self.sprites[2]).convert_alpha()
        self.sprite_rect = self.normal.get_rect(topleft=(x, y))

        self.current_sprite = self.normal

        # self.buttonTxt = Main_Font.render(buttonText, True, (20, 20, 20))

        objects.append(self)

    def process(self):
        self.current_sprite = self.normal
        mousePos = pygame.mouse.get_pos()
        if self.sprite_rect.collidepoint(mousePos):
            self.current_sprite = self.hovered
            if pygame.mouse.get_pressed(num_buttons=3)[0] == 1:
                pygame.mixer.music.play()
                self.current_sprite = self.clicked
                if self.onclickFunction is not None:
                    self.onclickFunction()
