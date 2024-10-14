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
    for indice, articulo in enumerate(inv):
        if cod == articulo['codigo']:
            print(color_p + f"Descripcion...........................: {articulo['descripcion']:<20} |")
            print(color_p + f"Tamaño................................: {articulo['tam']:<10}\t|")
            print(color_p + f"Cantidad..............................: {articulo['cant']:>10.0f}\t |")
            print(color_p + f"Precio................................: {articulo['precio']:>10.2f}\t |")
            separar(color_m)

            descripcion_vieja=articulo['descripcion']
            tamaño_viejo=articulo['tam']
            cantidad_vieja=articulo['cant']
            precio_viejo=articulo['precio']

            descripcion_nueva = input(color_o + 'Descripcion...............................: ')
            tamaño_nuevo = input(color_o + 'Tamaño...................................: ')
            cantidad_nueva = (input(color_o + 'Cantidad..................................: '))
            precio_nuevo = input(color_o + 'Precio............................: ')

            if len(descripcion_nueva) ==0:
                descripcion= descripcion_vieja
            else:
                descripcion = descripcion_nueva
            if len(tamaño_nuevo) == 0:
                tam = tamaño_viejo
            else:
                tam = tamaño_nuevo
            if len(cantidad_nueva) == 0:
                cantidad_vieja = int(cantidad_vieja)
                cant = cantidad_vieja
            else:
                cantidad_nueva = int(cantidad_nueva)
                cant = cantidad_nueva
            if len(precio_nuevo) == 0:
                precio_viejo = int(precio_viejo)
                precio = precio_viejo
            else:
                precio_nuevo = float(precio_nuevo)
                precio = precio_nuevo

            articulo_nuevo = {
                'codigo' :cod,
                'descripcion': descripcion,
                'tam': tam,
                'cant': cant,
                'precio': precio
            }
            del inv[indice]
            inv.append(articulo_nuevo)
            stock_nuevo = open('inventario.json','w')
            json.dump(inv,stock_nuevo)
            stock_nuevo.close()