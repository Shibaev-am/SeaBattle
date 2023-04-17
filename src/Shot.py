class Shot:
    def __init__(self, coords, attak, defend):
        self._coordinates = coords
        self._attaker = attak
        self._defender = defend

    def get_attacker(self):
        return self._attaker

    def get_defender(self):
        return self._defender

    def get_coordinates(self):
        return self._coordinates
