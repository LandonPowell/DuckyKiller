import time
import usb.core, usb.util

# generateWords
from random import choice
from wordlist import wordlist

# detectHuman
import pygame

def generateWords():
    return " ".join([choice(wordlist) for x in range(4)])

def detectHuman():
    pygame.init()
    pygame.event.set_grab(True)
    screen = pygame.display.set_mode((700, 90))
    screen.fill((50,50,50))

    words = generateWords()
    font = pygame.font.SysFont("monospace", 25)
    label = font.render(words, 1, (255,255,255))
    screen.blit(label, (10, 10))

    newText = ""

    while True:
        pygame.display.flip()
        events = pygame.event.get()

        for event in events:
            if event.type != pygame.KEYDOWN:
                pass

            elif event.key == pygame.K_RETURN and newText == words:
                pygame.quit()
                return True

            elif event.key == pygame.K_BACKSPACE:
                newText = ""

            elif event.type == pygame.KEYDOWN and event.key < 256:
                newText += chr(event.key)
                font = pygame.font.SysFont("monospace", 25)

        if words[:len(newText)] != newText:
            color = (255,100,100)
        else:
            color = (100,255,100)

        input = font.render(newText + "|",
            1, color,
            (50,50,50))

        screen.blit(input, (10, 50))

devices = [x for x in usb.core.find(find_all=True, bDeviceClass=0)]
deviceCount = len(devices)

print("The DuckyKiller is now watching for Rubber Ducks.")

while True:
    devices = [x for x in usb.core.find(find_all=True, bDeviceClass=0)]
    time.sleep(.25)
    if len(devices) > deviceCount:
        detectHuman()
    deviceCount = len(devices)
