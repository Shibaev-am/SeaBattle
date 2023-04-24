class Boat:

    def __init__(self, size, coords):
        self._size = size
        self._coordinates = coords
        self._cells = 0

    def get_size(self):
        return self._size

    def get_coordinates(self, i):
        return self._coordinates[i]

    def get_all_coordinates(self):
        return self._coordinates

    def check_boat(self):
        self._coordinates.sort()
        if len(self._coordinates) != self._size:
            return False
        f1 = True
        for i in range(1, self._size):
            diff_x = self._coordinates[0][0] - self._coordinates[i][0]
            diff_y = self._coordinates[i][1] - self._coordinates[i - 1][1]
            if not (diff_x == 0 and diff_y == 1):
                f1 = False
        f2 = True
        for i in range(1, self._size):
            diff_y = self._coordinates[0][1] - self._coordinates[i][1]
            diff_x = self._coordinates[i][0] - self._coordinates[i - 1][0]
            if not (diff_y == 0 and diff_x == 1):
                f2 = False
        return f1 or f2
        
