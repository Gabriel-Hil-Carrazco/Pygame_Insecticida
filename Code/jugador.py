import pygame
import variables
import balas

def disparar(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_SPACE:
            variables.balas.append({'x': float(variables.x), 'y': float(variables.y), 'dir': variables.direccion})

def movimientoJugador():
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        variables.x -= variables.vel
        variables.direccion = 'izquierda'
    if teclas[pygame.K_RIGHT]:
        variables.x += variables.vel
        variables.direccion = 'derecha'
    if teclas[pygame.K_UP]:
        variables.y -= variables.vel
        variables.direccion = 'arriba'
    if teclas[pygame.K_DOWN]:
        variables.y += variables.vel
        variables.direccion = 'abajo'