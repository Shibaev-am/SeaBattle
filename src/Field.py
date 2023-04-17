from src.Cell import Cell
from src import globals


class Field:

    def __init__(self, size=globals.field_size):
        self._size = size
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(Cell(i, j))
            if i == 0:
                self._arr = [temp]
            else:
                self._arr.append(temp)

    def update(self, cells):
        for cell in cells:
            x = int(cell[1:]) - 1
            y = globals.lettrs[cell[0]]
            self._arr[x][y].change_status('boat')

    def clear(self):
        for i in range(self._size):
            for j in range(self._size):
                self._arr[i][j].change_status('empty')

    def set_boat(self, new_boat):
        for i in range(new_boat.get_size()):
            x = new_boat.get_coordinates(i)[0]
            y = new_boat.get_coordinates(i)[1]
            if self._arr[x][y].get_status() != 'reserved':
                return False
        for i in range(self._size):
            for j in range(self._size):
                if self._arr[i][j].get_status() == 'reserved':
                    self.upd_cell_status(i, j, 'boat')
                    if i > 0:
                        if self._arr[i - 1][j].get_status() != 'boat' and \
                                self._arr[i - 1][j].get_status() != 'reserved':
                            self._arr[i - 1][j].change_status('border')
                        if j > 0:
                            self._arr[i - 1][j - 1].change_status('border')
                        if j < self._size - 1:
                            self._arr[i - 1][j + 1].change_status('border')
                    if i < self._size - 1:
                        if self._arr[i + 1][j].get_status() != 'boat' and \
                                self._arr[i + 1][j].get_status() != 'reserved':
                            self._arr[i + 1][j].change_status('border')
                        if j > 0:
                            self._arr[i + 1][j - 1].change_status('border')
                        if j < self._size - 1:
                            self._arr[i + 1][j + 1].change_status('border')
                    if j > 0:
                        if self._arr[i][j - 1].get_status() != 'boat' and \
                                self._arr[i][j - 1].get_status() != 'reserved':
                            self._arr[i][j - 1].change_status('border')
                    if j < self._size - 1:
                        if self._arr[i][j + 1].get_status() != 'boat' and \
                                self._arr[i][j + 1].get_status() != 'reserved':
                            self._arr[i][j + 1].change_status('border')
        return True

    def get_cell_status(self, x, y):
        return self._arr[x][y].get_status()

    def upd_cell_status(self, x, y, new_status):
        self._arr[x][y].change_status(new_status)

    def get_size(self):
        return self._size

    def draw_cell(self, i, j, screen, x, y):
        self._arr[i][j].draw_cell(screen, x, y)

    def draw_close_cell(self, i, j, screen, x, y):
        self._arr[i][j].draw_close_cell(screen, x, y)
