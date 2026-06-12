import pygame
import variables

def muerteGO(ventana, fuenteSegundos, textoMuerte):
    pygame.mixer.music.stop()
    ventana.fill(variables.negro)
    ventana.blit(textoMuerte, (500, 390))
    segundosSobrevividos = int(pygame.time.get_ticks() / 1000)
    textoTiempo = fuenteSegundos.render(f"Sobreviviste: {segundosSobrevividos} segundos :D", True, variables.grisHueso)
    textoBichos = fuenteSegundos.render(f"Bichos eliminados: {variables.enemigosEliminados} (¬_¬)", True, variables.grisHueso)
    ventana.blit(textoTiempo, (500, 500))
    ventana.blit(textoBichos, (500, 560))
    pygame.display.flip()
    pygame.time.delay(2000)
    return False