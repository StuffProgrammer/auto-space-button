from pynput.keyboard import Key, Controller
import time
import pygame
keyboard = Controller()
pygame.init()
time.sleep(5)
running = True
while running == True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(1)
pygame.quit()