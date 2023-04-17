from src.Player import Player
from src.Interface import Interface
from src import globals


class System:

    def __init__(self, screen, w, h):

        self._interface = Interface(screen, w, h)
        self._player1 = Player(self)
        self._player2 = Player(self)
        name1 = self._interface.get_name(globals.get_pl1_name)
        self._player1.update_name(name1)
        name2 = self._interface.get_name(globals.get_pl2_name)
        self._player2.update_name(name2)

    def get_interface(self):
        return self._interface

    def get_first_player(self):
        return self._player1

    def get_second_player(self):
        return self._player2

    def clear(self):
        self._player1.clear_field()
        self._player2.clear_field()

    def prepare_for_game(self):
        self.clear()
        self._player1.update_boats(globals.boats_size)
        self._player2.update_boats(globals.boats_size)

    @staticmethod
    def check_end(field):
        f = True
        for i in range(field.get_size()):
            for j in range(field.get_size()):
                if field.get_cell_status(i, j) == 'boat':
                    f = False
        return f

    def next_step(self, player):
        self._interface.get_next_command(player)

    @staticmethod
    def process_fire(shot):
        defend = shot.get_defender()
        coords = shot.get_coordinates()
        result = 0
        if defend.get_cell_status(coords[0], coords[1]) == 'empty' or \
                defend.get_cell_status(coords[0], coords[1]) == 'border':
            defend.upd_cell_status(coords[0], coords[1], 'past')
            result = 'past'
        elif defend.get_cell_status(coords[0], coords[1]) == 'boat':
            defend.upd_cell_status(coords[0], coords[1], 'wound')
            result = 'wound'
        else:
            result = 'doubling'

        if System.check_end(defend.get_field()):
            result = 'end'
        return result

    def game_process(self):
        is_now_first = True
        sz = self._player1.get_field_size()
        for i in range(sz):
            for j in range(sz):
                if self._player1.get_cell_status(i, j) == 'border':
                    self._player1.upd_cell_status(i, j, 'empty')
                if self._player2.get_cell_status(i, j) == 'border':
                    self._player2.upd_cell_status(i, j, 'empty')
        rs = '-'
        while True:
            shot = 0
            if rs == '-' or rs == 'past':
                if is_now_first:
                    self.next_step(self._player1)
                    shot = self._player1.fire(self._player2)
                else:
                    self.next_step(self._player2)
                    shot = self._player2.fire(self._player1)
            else:
                if is_now_first:
                    shot = self._player1.fire(self._player2)
                else:
                    shot = self._player2.fire(self._player1)
            rs = System.process_fire(shot)
            if rs == 'past':
                self._interface.print_result_attack("Мимо")
                is_now_first = not is_now_first
            elif rs == 'wound':
                self._interface.print_result_attack("Есть пробитие!")
            elif rs == 'doubling':
                self._interface.print_result_attack("Туда уже был выстрел!")
            else:
                if shot.get_attacker() == self._player1:
                    self._interface.end_game(self._player1, self._player2)
                else:
                    self._interface.end_game(self._player2, self._player1)
                break
