import pygame
from src import globals
from src.System import System


pygame.init()
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("SeaBattle")
system = System(screen, globals.WIDTH, globals.HEIGHT)
pygame.display.update()

cmd = system.get_interface().get_start_command()
while cmd != "start":
    if cmd == "change1" or cmd == "change2":
        if cmd == "change1":
            new_name = system.get_interface().get_name(globals.get_pl1_name)
            system.get_first_player().update_name(new_name)
        else:
            new_name = system.get_interface().get_name(globals.get_pl2_name)
            system.get_second_player().update_name(new_name)
    cmd = system.get_interface().get_start_command()
if cmd != "auto":
    system.prepare_for_game()
ready = system.get_interface().get_ready_command()
while ready != "ready":
    ready = system.get_interface().get_ready_command()
system.game_process()
is_game = True
while is_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            is_game = False
pygame.quit()
