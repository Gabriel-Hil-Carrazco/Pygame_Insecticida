import pygame
import random
import variables

def spawnEnemigo():
    tipos = ['arana', 'escarabajo', 'mosquito', 'cucaracha']
    tipo = random.choice(tipos)

    if tipo == 'arana':
        velocidadBicho = variables.velocidadArana
    elif tipo == 'escarabajo':
        velocidadBicho = variables.velocidadEscarabajo
    elif tipo == 'mosquito':
        velocidadBicho = variables.velocidadMosquito
    else:
        velocidadBicho = variables.velocidadCucaracha

    borde = random.choice(['izquierda', 'derecha', 'arriba', 'abajo'])
    if borde == 'izquierda':
        ex = -100
        ey = random.randint(0, variables.alto)
    elif borde == 'derecha':
        ex = variables.ancho + 100
        ey = random.randint(0, variables.alto)
    elif borde == 'arriba':
        ex = random.randint(0, variables.ancho)
        ey = -100
    else:
        ex = random.randint(0, variables.ancho)
        ey = variables.alto + 100

    variables.enemigos.append({
        'tipo': tipo,
        'x': ex,
        'y': ey,
        'vel': velocidadBicho
    })

def movimientoEnemigos(ventana):
    for bicho in variables.enemigos:
        if bicho['x'] < variables.x:
            bicho['x'] += bicho['vel']
        elif bicho['x'] > variables.x:
            bicho['x'] -= bicho['vel']

        if bicho['y'] < variables.y:
            bicho['y'] += bicho['vel']
        elif bicho['y'] > variables.y:
            bicho['y'] -= bicho['vel']

        if bicho['tipo'] == 'arana':
            ventana.blit(variables.arana, (bicho['x'], bicho['y']))
            hitboxBicho = pygame.Rect(bicho['x'], bicho['y'], 52, 52)
            dano = variables.danoArana
        elif bicho['tipo'] == 'escarabajo':
            ventana.blit(variables.escarabajo, (bicho['x'], bicho['y']))
            hitboxBicho = pygame.Rect(bicho['x'], bicho['y'], 55, 55)
            dano = variables.danoEscarabajo
        elif bicho['tipo'] == 'mosquito':
            ventana.blit(variables.mosquito, (bicho['x'], bicho['y']))
            hitboxBicho = pygame.Rect(bicho['x'], bicho['y'], 25, 25)
            dano = variables.danoMosquito
        else:
            ventana.blit(variables.cucaracha, (bicho['x'], bicho['y']))
            hitboxBicho = pygame.Rect(bicho['x'], bicho['y'], 40, 40)
            dano = variables.danoCucaracha

        ventana.blit(variables.insecticida, (variables.x, variables.y))
        hitboxJugador = pygame.Rect(variables.x, variables.y, 60, 60)
        if hitboxJugador.colliderect(hitboxBicho):
            variables.saludInstante -= dano