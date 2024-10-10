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
            print(color_o + f"Descripcion...........................: {articulo['descripcion']:<10}|")
            print(color_o + f"Tamaño................................: {articulo['tam']:<10}|")
            print(color_o + f"Tematica..............................: {articulo['deco']:<10}|")
            print(color_o + f"Cantidad..............................: {articulo['cant']:>10.0f}|")
            print(color_o + f"Precio................................: {articulo['precio']:>10.2f}|")
            break
    separar(color_m)