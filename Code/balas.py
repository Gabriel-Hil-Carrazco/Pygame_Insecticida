import pygame
import variables

def balas(balas, ventana, enemigos, sonidoDano, spawnEnemigo):
    for bala in balas[:]:
            if bala['dir'] == 'derecha':   
                bala['x'] += 10
            if bala['dir'] == 'izquierda': 
                bala['x'] -= 10
            if bala['dir'] == 'arriba':    
                bala['y'] -= 10
            if bala['dir'] == 'abajo':     
                bala['y'] += 10

            pygame.draw.circle(ventana, variables.negro, (int(bala['x']), int(bala['y'])), 6)

            if not (0 <= bala['x'] <= variables.ancho and 0 <= bala['y'] <= variables.alto):
                balas.remove(bala)
                continue

            for bicho in enemigos[:]:
                hitbox = pygame.Rect(bicho['x'], bicho['y'], 50, 50)
                if hitbox.collidepoint(bala['x'], bala['y']):
                    sonidoDano.play()
                    enemigos.remove(bicho)
                    balas.remove(bala)
                    variables.enemigosEliminados += 1
                    spawnEnemigo()
                    spawnEnemigo()
                    break