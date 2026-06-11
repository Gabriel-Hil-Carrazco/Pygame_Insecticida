import pygame
import variables

from archivos import archivos
from salud import salud
from textos import textoBichosMuertos, gameOver
from jugador import disparar, movimientoJugador
from bichos import spawnEnemigo, movimientoEnemigos
from balas import balas as procesarBalas
from bordes import bordesPantalla

pygame.init()

# ventana primero
ventana = pygame.display.set_mode((variables.ancho, variables.alto))
pygame.display.set_caption("Juego estilo Brotato")
reloj = pygame.time.Clock()

# cargar archivos
archivos()

# inicializar listas y estado
variables.enemigos = []
variables.enemigosEliminados = 0
variables.balas = []
variables.direccion = 'derecha'

# textos
textoMuerte, fuenteSegundos = gameOver()
contadorLetra = textoBichosMuertos()

# spawn inicial
for i in range(4):
    spawnEnemigo()

# ------------------------------    EJECUTAR    ----------------------------------------

corriendo = True

while corriendo:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        disparar(evento)

    if variables.saludInstante <= 0:
        pygame.mixer.music.stop()
        ventana.fill((0, 0, 0))
        ventana.blit(textoMuerte, (500, 390))
        segundosSobrevividos = int(pygame.time.get_ticks() / 1000)
        textoTiempo = fuenteSegundos.render(f"Sobreviviste: {segundosSobrevividos} segundos :D", True, variables.grisHueso)
        textoBichos = fuenteSegundos.render(f"Bichos eliminados: {variables.enemigosEliminados} (¬‿¬)", True, variables.grisHueso)
        ventana.blit(textoTiempo, (500, 500))
        ventana.blit(textoBichos, (500, 560))
        pygame.display.flip()
        pygame.time.delay(3000)
        corriendo = False
        continue
    
    # jugador
    movimientoJugador()

    # bordes
    bordesPantalla()

    # fondo
    ventana.blit(variables.fondo, (0, 0))

    # enemigos
    movimientoEnemigos(ventana)

    #balas
    procesarBalas(variables.balas, ventana, variables.enemigos, variables.sonidoDano, spawnEnemigo)

    # contador bichos
    bichosAniquilados = contadorLetra.render(f"Bichos eliminados = {variables.enemigosEliminados}", True, variables.negro)
    ventana.blit(bichosAniquilados, (1180, 40))

    # craneo
    ventana.blit(variables.craneo, (1520, 28))

    # barra de salud
    salud(ventana)

    # display
    pygame.display.flip()
    reloj.tick(60)

pygame.quit() 
