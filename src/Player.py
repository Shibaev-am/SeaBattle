import pygame.time
from src.Field import Field
from src.Shot import Shot
from src import globals


class Player:
    def __init__(self, system):
        self._field = Field()
        self._name = "eee"
        self._system = system
        self._boats = 0

    def get_field(self):
        return self._field

    def get_boats(self):
        return self._boats

    def get_field_size(self):
        return self._field.get_size()

    def get_name(self):
        return self._name

    def update_name(self, name):
        self._name = name

    def unreserved(self):
        for i in range(self._field.get_size()):
            for j in range(self._field.get_size()):
                if self.get_cell_status(i, j) == 'reserved':
                    self.upd_cell_status(i, j, 'empty')

    def update_boats(self, sizes_of_boat):
        boats = []
        i = 0
        while i < len(sizes_of_boat):
            curr_boat = self._system.get_interface().get_boat(
                sizes_of_boat[i], self)
            check = curr_boat.check_boat()
            if not check:
                self.unreserved()
                pygame.time.delay(100)
            else:
                check = self.set_boat_on_field(curr_boat)
                if not check:
                    self.unreserved()
                    pygame.time.delay(100)
                else:
                    boats.append(curr_boat)
                    i += 1
        pygame.time.delay(100)
        self._boats = boats

    def get_cell_status(self, x, y):
        return self._field.get_cell_status(x, y)

    def upd_cell_status(self, x, y, new_status):
        self._field.upd_cell_status(x, y, new_status)

    def set_boat_on_field(self, boat):
        res = self._field.set_boat(boat)
        return res

    def clear_field(self):
        self._field.clear()

    def fire(self, opponent):
        target = self._system.get_interface().get_target(self, opponent)
        x = int(target[1:]) - 1
        y = globals.lettrs[target[0]]
        return Shot([x, y], self, opponent)

    def draw_cell(self, i, j, screen, x, y):
        self._field.draw_cell(i, j, screen, x, y)

    def draw_close_cell(self, i, j, screen, x, y):
        self._field.draw_close_cell(i, j, screen, x, y)
