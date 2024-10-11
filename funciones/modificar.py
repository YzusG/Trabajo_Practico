import json
from funciones.validar import validar
from funciones.separar import separar
def modificar(inv,color_m,color_o,color_e,color_p):
    while True:
        cod = int(input(color_o + 'Ingrese el codigo del articulo....................: '))
        if validar(cod,inv) == False:
            print(color_e + 'El articulo no existe................................')
        else:
            break
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_p + f"Descripcion...........................: {articulo['descripcion']:<20} |")
            print(color_p + f"Tamaño................................: {articulo['tam']:<10}\t|")
            print(color_p + f"Tematica..............................: {articulo['deco']:<15}|")
            print(color_p + f"Cantidad..............................: {articulo['cant']:>10.0f}\t |")
            print(color_p + f"Precio................................: {articulo['precio']:>10.2f}\t |")
            separar(color_m)

            descripcion_vieja=articulo['descripcion']
            tamaño_viejo=articulo['tam']
            decoracion_vieja=articulo['deco']
            cantidad_vieja=articulo['cant']
            precio_viejo=articulo['precio']

            descripcion_nueva = input(color_o + 'Descripcion...............................: ')
            tamaño_nuevo = input(color_o + 'Tamaño...................................: ')
            decoracion_nueva = input(color_o + 'Tematica..................................: ')
            cantidad_nueva = (input(color_o + 'Cantidad..................................: '))
            precio_nuevo = input(color_o + 'Precio............................: ')

            if len(descripcion_nueva) ==0:
                articulo['descripcion'] = descripcion_vieja
            if len(tamaño_nuevo) == 0:
                articulo['tam'] = tamaño_viejo
            if len(decoracion_nueva) == 0:
                articulo['deco'] = decoracion_vieja
            if len(cantidad_nueva) == 0:
                articulo['cant'] = cantidad_vieja
            else:
                cantidad_nueva = int(cantidad_nueva)
                articulo['cant'] = cantidad_nueva
            if len(precio_nuevo) == 0:
                articulo['precio'] = precio_viejo
            else:
                precio_nuevo = float(precio_nuevo)
                articulo['precio'] = precio_nuevo