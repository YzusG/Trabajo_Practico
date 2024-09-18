def baja(inv, color_m, color_o):
    cod = int(input(color_o + 'Ingrese el codigo del producto.............:'))
    for prenda in inv:
        if cod == prenda['codigo']:
            print(color_m + '|', end="")
            print(color_m + f"Descripcion...........................: {prenda['descripcion']} |")
            print(color_m + '|', end="")
            print(color_m + f"Talla.................................: {prenda['talla']}\t|")
            print(color_m + '|', end="")
            print(color_m + f"Tematica..............................: {prenda['deco']}|")
            print(color_m + '|', end="")
            print(color_m + f"Precio................................: {prenda['precio']}\t |")
        break
    op = input(color_o + '¿Desea darle de baja al producto....?(S/N):').capitalize()
    if op == 'S':
        ...