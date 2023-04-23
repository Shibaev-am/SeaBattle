from src.Boat import Boat
import pygame
from src import globals


class Interface:

    def __init__(self, screen, sc_w, sc_h):
        print("Welcome to the game)")
        self.screen = screen
        self.screen_w = sc_w
        self.screen_h = sc_h
        self.back_color = (175, 238, 238)
        self.text_color = (0, 0, 0)
        self.start_displey()
        clock = pygame.time.Clock()
        is_run = True
        while is_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_run = False
            clock.tick(globals.FPS)

    def start_displey(self, is_begin=True):
        self.screen.fill(self.back_color)
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        msg = globals.welcome_msg
        if not is_begin:
            msg = globals.all_is_ready_msg
        text = font.render(msg, True, self.text_color)
        self.screen.blit(text, (self.screen_w / 2 - text.get_size()[0] // 2,
                                self.screen_h / 2 - text.get_size()[1] // 2))
        pygame.display.update()

    def get_name(self, msg):
        self.screen.fill(self.back_color)
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, globals.black_color)
        self.screen.blit(text, (globals.padding, self.screen_h // 2))
        pygame.display.update()
        input_rect = pygame.Rect(
            text.get_size()[0] + globals.padding, self.screen_h // 2, 100, 35)
        clock = pygame.time.Clock()
        user_text = ''
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return user_text
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_SPACE:
                        user_text += ' '
                    else:
                        user_text += event.unicode
            pygame.draw.rect(self.screen, (self.back_color[0] + 10,
                             self.back_color[1] + 10,
                             self.back_color[2] + 10),
                             input_rect)
            text_surface = font.render(user_text, True, globals.black_color)
            self.screen.blit(
                text_surface, (input_rect.x, input_rect.y))
            input_rect.w = max(100, text_surface.get_width() + 10)
            pygame.display.update()
            clock.tick(globals.FPS)

    def get_boat(self, size, player, text_msg):
        msg = text_msg
        self.screen.fill(self.back_color)
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        self.screen.blit(text, (self.screen_w // 2 -
                         text.get_size()[0] // 2, 20))
        pygame.display.update()
        cell_w = globals.cell_width
        cell_h = globals.cell_height
        curr_x = self.screen_w // 2 - cell_w * globals.field_size // 2
        curr_y = self.screen_h // 2 - cell_h * globals.field_size // 2
        coords = []
        for i in range(player.get_field_size()):
            for j in range(player.get_field_size()):
                player.draw_cell(
                    i, j, self.screen,
                    curr_x + cell_h / 2 + j * cell_h,
                    curr_y + cell_w / 2 + i * cell_w)
        pygame.display.update()
        clock = pygame.time.Clock()
        while True:
            mouse = pygame.mouse.get_pos()
            sz = player.get_field_size()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                        and curr_x <= mouse[0] <= curr_x + sz * cell_h \
                        and curr_y <= mouse[1] <= curr_y + sz * cell_w:
                    cell_j = (mouse[0] - curr_x) // cell_h
                    cell_i = (mouse[1] - curr_y) // cell_w
                    if player.get_cell_status(
                            cell_i, cell_j) == 'empty':
                        coords.append([cell_i, cell_j])
                        player.upd_cell_status(
                            cell_i, cell_j, 'reserved')
                        player.draw_cell(cell_i, cell_j, self.screen,
                                         curr_x + cell_h /
                                         2 + cell_j * cell_h,
                                         curr_y + cell_w / 2 + cell_i * cell_w)
                        pygame.display.update()

            if len(coords) == size:
                break
            clock.tick(globals.FPS)
        new_boat = Boat(size, coords)
        return new_boat

    def print_result_attack(self, msg):
        pass

    def print_close_field(self, player):
        msg = globals.opponent_field_msg
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        cell_w = globals.cell_width
        cell_h = globals.cell_height
        curr_x = self.screen_w // 4 - cell_w * globals.field_size // 2
        curr_y = self.screen_h // 2 - cell_h * globals.field_size // 2
        self.screen.blit(text, ((curr_x + cell_w * globals.field_size //
                         2) - text.get_size()[0] // 2, curr_y - 100))
        for i in range(player.get_field_size()):
            for j in range(player.get_field_size()):
                player.draw_close_cell(i, j, self.screen,
                                       curr_x + cell_h / 2 + j * cell_h,
                                       curr_y + cell_w / 2 + i * cell_w)
        pygame.display.update()

    def print_open_field(self, player, is_shift=True, is_end=False):
        msg = globals.our_field_msg
        if is_end:
            msg = globals.player_field_msg.format(player.get_name())
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        cell_w = globals.cell_width
        cell_h = globals.cell_height
        curr_x = 0
        curr_y = 0
        if is_shift:
            curr_x = 3 * (self.screen_w // 4) - \
                cell_w * globals.field_size // 2
            curr_y = self.screen_h // 2 - cell_h * globals.field_size // 2
        else:
            curr_x = self.screen_w // 4 - cell_w * globals.field_size // 2
            curr_y = self.screen_h // 2 - cell_h * globals.field_size // 2

        self.screen.blit(text, ((curr_x + cell_w * globals.field_size //
                         2) - text.get_size()[0] // 2, curr_y - 100))
        pygame.display.update()
        for i in range(player.get_field_size()):
            for j in range(player.get_field_size()):
                player.draw_cell(i, j, self.screen,
                                 curr_x + cell_h / 2 + j * cell_h,
                                 curr_y + cell_w / 2 + i * cell_w)
        pygame.display.update()

    def get_target(self, shooter, defender):
        self.screen.fill(self.back_color)
        msg = globals.get_trgt_msg.format(shooter.get_name())
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        self.screen.blit(text, (self.screen_w // 2 -
                         text.get_size()[0] // 2, 30))
        pygame.display.update()
        self.print_open_field(shooter)
        self.print_close_field(defender)
        cell_w = globals.cell_width
        cell_h = globals.cell_height
        curr_x = self.screen_w // 4 - cell_w * globals.field_size // 2
        curr_y = self.screen_h // 2 - cell_h * globals.field_size // 2
        for i in range(defender.get_field_size()):
            for j in range(defender.get_field_size()):
                defender.draw_close_cell(
                    i, j, self.screen,
                    curr_x + cell_h / 2 + j * cell_h,
                    curr_y + cell_w / 2 + i * cell_w)
        pygame.display.update()
        clock = pygame.time.Clock()
        while True:
            mouse = pygame.mouse.get_pos()
            sz = defender.get_field_size()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
                        and curr_x <= mouse[0] <= curr_x + sz * cell_h \
                        and curr_y <= mouse[1] <= curr_y + sz * cell_w:
                    cell_j = (mouse[0] - curr_x) // cell_h
                    cell_i = (mouse[1] - curr_y) // cell_w
                    if defender.get_cell_status(
                            cell_i, cell_j) != 'past' and \
                            defender.get_cell_status(
                            cell_i, cell_j) != 'wound':
                        cell_x = curr_x + cell_h / 2 + cell_j * cell_h
                        cell_y = curr_y + cell_w / 2 + cell_i * cell_w
                        defender.draw_cell(cell_i, cell_j, self.screen,
                                           cell_x, cell_y)
                        trgt = str(chr(ord('A') + cell_j)) + \
                            str(cell_i + 1)
                        return trgt

            clock.tick(globals.FPS)

    def end_game(self, winner, loser):
        self.screen.fill(self.back_color)
        msg = globals.winner_name_msg.format(winner.get_name())
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        self.screen.blit(text, (self.screen_w // 2 -
                         text.get_size()[0] // 2, globals.padding))
        pygame.display.update()
        print("Игра окончена, победил игрок {}!".format(winner.get_name()))
        self.print_open_field(winner, is_shift=False, is_end=True)
        self.print_open_field(loser, is_end=True)

    def get_start_command(self):
        msg1 = globals.ready_to_set_flds_msg
        msg2 = globals.change_name_pl1_msg
        msg3 = globals.change_name_pl2_msg
        self.screen.fill(self.back_color)
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text1 = font.render(msg1, True, self.text_color)
        text2 = font.render(msg2, True, self.text_color)
        text3 = font.render(msg3, True, self.text_color)
        self.screen.blit(text1, (self.screen_w // 2 - text1.get_size()[0] // 2,
                                 self.screen_h // 2 - 5 * text2.get_size()[1]))
        self.screen.blit(text2, (self.screen_w // 2 - text2.get_size()[0] // 2,
                                 self.screen_h // 2))
        self.screen.blit(text3, (self.screen_w // 2 - text3.get_size()[0] // 2,
                                 self.screen_h // 2 + 5 * text2.get_size()[1]))
        pygame.display.update()
        is_start = False
        clock = pygame.time.Clock()
        while not is_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'start'
                    elif event.key == pygame.K_1:
                        return 'change1'
                    elif event.key == pygame.K_2:
                        return 'change2'
            clock.tick(globals.FPS)

    def get_ready_command(self):
        self.start_displey(is_begin=False)
        is_start = False
        clock = pygame.time.Clock()
        while not is_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'ready'
            clock.tick(globals.FPS)

    def get_next_command(self, player):
        self.screen.fill(self.back_color)
        msg = globals.ready_next_step_msg.format(player.get_name())
        font = pygame.font.SysFont(
            'TimesNewRoman', globals.text_size, bold=False, italic=False)
        text = font.render(msg, True, self.text_color)
        self.screen.blit(text, (self.screen_w // 2 -
                         text.get_size()[0] // 2, self.screen_h // 2))
        pygame.display.update()
        is_start = False
        clock = pygame.time.Clock()
        while not is_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 'next'
            clock.tick(globals.FPS)
