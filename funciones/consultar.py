def consultar(inv, color_m):
    cod = int(input(color_m + 'Ingrese el Codigo....................:'))
    for prenda in inv:
        if cod == prenda['codigo']:
            print(prenda)
        break