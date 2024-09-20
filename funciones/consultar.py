def consultar(inv, color_m, color_o):
    print(color_o + '*'*50)
    cod = int(input(color_o + 'Ingrese el Codigo....................: '))
    print(color_o + '*'*50)
    print(color_m + '='*50)
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_m + f"Descripcion...........................: {articulo['descripcion']:<20} |")
            print(color_m + f"Tamaño................................: {articulo['tam']:<10}\t|")
            print(color_m + f"Tematica..............................: {articulo['deco']:<15}|")
            print(color_m + f"Cantidad..............................: {articulo['cant']:>10.0f}\t |")
            print(color_m + f"Precio................................: {articulo['precio']:>10.2f}\t |")
        break
    print(color_m + '='*50)