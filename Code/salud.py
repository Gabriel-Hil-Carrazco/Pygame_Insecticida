import pygame
import variables

def salud(ventana):
    saludActual = variables.saludInstante / variables.saludMaxima
    anchoSalud = variables.barraAncho * saludActual
    pygame.draw.rect(ventana, variables.rojo, (30, 30, variables.barraAncho, variables.barraAlto))
    pygame.draw.rect(ventana, variables.verde, (30, 30, anchoSalud, variables.barraAlto))