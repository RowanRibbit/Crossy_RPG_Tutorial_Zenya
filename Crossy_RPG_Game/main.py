# import any libraries for the project
import pygame
# import the class from the game.py file
from game import Game

# initialize libraries
pygame.init()

game = Game()

game.run_game_loop()

# close libraries and quit
pygame.quit()
quit()