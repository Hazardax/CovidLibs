import pygame


class Surface:
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.surf = pygame.Surface((width, height))

    def get_alpha(self):
        return self.surf.get_alpha()

    def set_alpha(self, alpha):
        self.surf.set_alpha(alpha)

    def get(self):
        return self.surf

    def set(self, width, height):
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw(self, window):
        window.get().blit(self.surf, (self.pos_x, self.pos_y))

    def fill(self, color):
        self.surf.fill(color)

    def __del__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.surf = None
