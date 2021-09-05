import pygame
from pygame import locals as const
from PIL import ImageGrab
from time import sleep

def main():

    path = "screenshot.png"
    screenshot = ImageGrab.grab()  # Take the screenshot
    screenshot.save(path, 'PNG')

    sleep(2)

    pygame.init()
    pygame.display.set_caption("Calibrateur3000")
    ecran = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    bg = pygame.image.load(path)

    while 1 :

        for event in pygame.event.get():
            stop = process_event(event)
            update(ecran,bg)


def update(ecran,bg):
    pos = pygame.mouse.get_pos()
    font = pygame.font.SysFont(None, 48)  
    text = font.render(str(pos), True, (255,255,255))
    rect = text.get_rect()
    rect.bottomright = pos

    ecran.blit(bg, (0, 0))
    ecran.blit(text, rect)
    pygame.display.flip() 

def process_event(event: pygame.event):

    # Click Gauche
    if event.type == const.MOUSEBUTTONUP and event.button == 1:
        print(event.pos)

    # Echap
    if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
        quit()

if __name__ == '__main__':
    main()