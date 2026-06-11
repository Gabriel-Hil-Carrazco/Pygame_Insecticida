import variables

# bordes de pantalla
def bordesPantalla():
    variables.x = max(0, min(variables.x, variables.ancho - variables.tamano))
    variables.y = max(0, min(variables.y, variables.alto - variables.tamano))