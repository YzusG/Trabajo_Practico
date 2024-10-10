from funciones.separar import separar
from funciones.validar import validar
def consultar(inv, color_m, color_o, color_e):
    while True:
        cod = int(input(color_o + 'Ingrese el Codigo....................: '))
        if validar(cod,inv,color_e) == False:
            print(color_e + 'El producto no existe.......................')
            print(color_e + 'Ingrese nuevo codigo........................')
        else:
            break
    separar(color_m)
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_m + f"Descripcion...........................: {articulo['descripcion']:<20} |")
            print(color_m + f"Tamaño................................: {articulo['tam']:<10}\t|")
            print(color_m + f"Tematica..............................: {articulo['deco']:<15}|")
            print(color_m + f"Cantidad..............................: {articulo['cant']:>10.0f}\t |")
            print(color_m + f"Precio................................: {articulo['precio']:>10.2f}\t |")
    print(color_m + '='*50)
