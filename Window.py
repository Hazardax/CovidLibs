import pygame

pygame.init()


class Window:
    def __init__(self, width, height, title="Game"):
        self.width = width
        self.height = height
        self.tick = 128
        self.win_obj = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def set(self, width, height):
        self.win_obj = pygame.display.set_mode((width, height))

    def get(self):
        return self.win_obj

    def get_size(self):
        return self.win_obj.get_size()

    def get_title(self):
        return pygame.display.get_caption()

    def get_tick(self):
        return self.tick

    def set_title(self, title):
        pygame.display.set_caption(title)

    def set_tick(self, tick):
        self.tick = tick

    def draw(self, obj, pos_x, pos_y):
        self.win_obj.blit(obj, (pos_x, pos_y))

    def fill(self, background):
        self.win_obj.fill(background)

    def close(self):
        pygame.quit()

    def update(self):
        pygame.time.Clock().tick(self.tick)
        pygame.display.flip()

    def __del__(self):
        self.width = None
        self.height = None
        self.title = None
        self.tick = None
        self.win_obj = None
        self.surf = None
        self.opened = None
