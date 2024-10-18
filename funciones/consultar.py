from funciones.separar import separar
from funciones.validar import validar
def consultar(inv, color_m, color_o, color_e,color_p):
    try:
        while True:
            cod = int(input(color_o + 'Ingrese el Codigo....................: '))
            if validar(cod,inv) == False:
                print(color_e + 'El producto no existe.......................')
                print(color_e + 'Ingrese nuevo codigo........................')
                separar(color_m)
            else:
                break
    except ValueError:
        print(color_e +'El codigo debe ser un numero.................')
    separar(color_m)
    for articulo in inv:
        if cod == articulo['codigo']:
                print(color_p + f"Descripcion...........................: {articulo['descripcion']:<10}|")
                print(color_p + f"Tamaño................................: {articulo['tam']:<10}|")
                print(color_p + f"Cantidad..............................: {articulo['cant']:>10.0f}|")
                print(color_p + f"Precio................................: {articulo['precio']:>10.2f}|")
        print(color_m + '='*51)