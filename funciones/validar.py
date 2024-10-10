def validar(cod, inv):
    resultado = False
    for articulo in inv:
        if cod == articulo['codigo']:
            resultado = True
    return resultado
    