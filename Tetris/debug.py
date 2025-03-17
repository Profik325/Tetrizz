import pygame


pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, surf, x=10, y=10):
    debug_surf = font.render(str(info), True, (255, 255, 255))
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    surf.blit(debug_surf, debug_rect)
