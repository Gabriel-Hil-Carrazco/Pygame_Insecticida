import pygame
import variables

pygame.font.init()

def textoBichosMuertos():
    contadorLetra = pygame.font.SysFont("Calibri", 30, bold=True)
    return contadorLetra

def gameOver():
    fuenteGameOver = pygame.font.SysFont("Calibri", 100, bold=True)
    textoMuerte = fuenteGameOver.render("GAME OVER", True, variables.rojo)
    fuenteSegundos = pygame.font.SysFont("Calibri", 50, bold=False)
    return textoMuerte, fuenteSegundos