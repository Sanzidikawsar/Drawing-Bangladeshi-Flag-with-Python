import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((600,360),0,32)

    green=(0, 106, 78)
    red=(244, 42, 65)

    DISPLAY.fill(green)

    # pygame.draw.rect(DISPLAY,red,(200,150,100,50))
    pygame.draw.circle(DISPLAY, red, [300, 180], 90)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
