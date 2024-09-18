def consultar(inv, color_m, color_o):
    print(color_o + '*'*50)
    cod = int(input(color_o + 'Ingrese el Codigo....................: '))
    print(color_o + '*'*50)
    print(color_m + '='*50)
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_m + f"Descripcion...........................: {articulo['descripcion']} |")
            print(color_m + f"Tamaño................................: {articulo['tam']}\t|")
            print(color_m + f"Tematica..............................: {articulo['deco']}|")
            print(color_m + f"Cantidad..............................: {articulo['cant']}\t |")
            print(color_m + f"Precio................................: {articulo['precio']}\t |")
        break
    print(color_m + '='*50)