import pygame

from pygame.locals import *

pygame.init()

display_surface = pygame.display.set_mode((500,500))

pygame.display.set_caption('Hand Game')

while True:

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()
            exit()

    pygame.display.update()