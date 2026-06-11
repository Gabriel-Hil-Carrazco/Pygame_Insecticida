import os
import pygame
import variables

def archivos():
    DATOS = os.path.dirname(os.path.abspath(__file__))

    def ruta(archivo):
        return os.path.join(DATOS, archivo)

    # música
    pygame.mixer.init()
    pygame.mixer.music.load(ruta("../music/musica.mp3"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    # sonido daño
    variables.sonidoDano = pygame.mixer.Sound(ruta("../music/golpe.mp3"))

    # imagenes
    variables.fondo = pygame.image.load(ruta("../images/cocina.jpg"))
    variables.fondo = pygame.transform.scale(variables.fondo, (1600, 900))

    variables.arana = pygame.image.load(ruta("../images/arana.png")).convert_alpha()
    variables.arana = pygame.transform.scale(variables.arana, (70, 70))

    variables.escarabajo = pygame.image.load(ruta("../images/escarabajo-ciervo.png")).convert_alpha()
    variables.escarabajo = pygame.transform.scale(variables.escarabajo, (65, 65))

    variables.mosquito = pygame.image.load(ruta("../images/mosquito.png")).convert_alpha()
    variables.mosquito = pygame.transform.scale(variables.mosquito, (42, 42))

    variables.cucaracha = pygame.image.load(ruta("../images/cucaracha.png")).convert_alpha()
    variables.cucaracha = pygame.transform.scale(variables.cucaracha, (57, 57))

    variables.insecticida = pygame.image.load(ruta("../images/insecticida.png")).convert_alpha()
    variables.insecticida = pygame.transform.scale(variables.insecticida, (70, 70))

    variables.craneo = pygame.image.load(ruta("../images/craneo.png")).convert_alpha()
    variables.craneo = pygame.transform.scale(variables.craneo, (50, 50))
