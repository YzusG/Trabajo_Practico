def consultar(inv, color_m, color_o):
    print(color_o + '*'*50)
    cod = int(input(color_o + 'Ingrese el Codigo....................: '))
    print(color_o + '*'*50)
    print()
    print(color_m + '='*50)
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
    print(color_m + '='*50)