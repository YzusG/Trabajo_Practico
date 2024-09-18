def baja(inv, color_m, color_o):
    cod = int(input(color_o + 'Ingrese el codigo del producto.............:'))
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_m + '|', end="")
            print(color_m + f"Descripcion...........................: {articulo['descripcion']} |")
            print(color_m + '|', end="")
            print(color_m + f"Talla.................................: {articulo['talla']}\t|")
            print(color_m + '|', end="")
            print(color_m + f"Tematica..............................: {articulo['deco']}|")
            print(color_m + '|', end="")
            print(color_m + f"Precio................................: {articulo['precio']}\t |")
            break
    op = input(color_o + '¿Desea darle de baja al producto....?(S/N):').capitalize()
    if op == 'S':
        ...