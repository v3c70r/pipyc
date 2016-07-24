import pygame
from motor import Motor

pygame.init()
_motor = Motor()
quit = False
while not quit:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                _motor.forward_start()
            if event.key == pygame.K_s:
                _motor.backward_start()
            if event.key == pygame.K_a:
                _motor.turn_left_start()
            if event.key == pygame.K_d:
                _motor.turn_right_start()
            if event.key == pygame.K_q:
                quit=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                _motor.forward_stop()
            if event.key == pygame.K_s:
                _motor.backward_stop()
            if event.key == pygame.K_a:
                _motor.turn_left_end()
            if event.key == pygame.K_d:
                _motor.turn_right_end()
_motor.dispose()
