import pygame
from src import globals


class Cell:

    def __init__(self, x, y, status='empty'):
        self._status = status
        self._x = x
        self._y = y
        if status == 'empty':
            self._img = pygame.image.load('images/Empty.PNG').convert()
        elif status == 'wound':
            self._img = pygame.image.load('images/Wound.PNG').convert()
        elif status == 'past':
            self._img = pygame.image.load('images/Past.PNG').convert()
        elif status == 'boat' or status == 'reserved':
            self._img = pygame.image.load('images/Boat.PNG').convert()

    def change_status(self, new_status='empty'):
        self._status = new_status
        if new_status == 'empty':
            self._img = pygame.image.load('images/Empty.PNG').convert()
        elif new_status == 'wound':
            self._img = pygame.image.load('images/Wound.PNG').convert()
        elif new_status == 'past':
            self._img = pygame.image.load('images/Past.PNG').convert()
        elif new_status == 'border':
            self._img = pygame.image.load('images/Reserved.PNG').convert()
        elif new_status == 'boat' or new_status == 'reserved':
            self._img = pygame.image.load('images/Boat.PNG').convert()

    def get_status(self):
        return self._status

    def draw_cell(self, screen, x, y):
        width = globals.cell_width
        height = globals.cell_height
        img = pygame.transform.scale(self._img, (width, height))
        screen.blit(img, img.get_rect(center=(x, y)))

    def draw_close_cell(self, screen, x, y):
        width = globals.cell_width
        height = globals.cell_height
        if self._status == 'boat' or self._status == 'empty':
            img = pygame.image.load('images/Reserved.PNG').convert()
            img = pygame.transform.scale(img, (width, height))
        else:
            img = pygame.transform.scale(self._img, (width, height))
        screen.blit(img, img.get_rect(center=(x, y)))
