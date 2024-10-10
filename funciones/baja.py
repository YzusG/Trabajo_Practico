import json
from funciones.validar import validar

def baja(inv, color_m, color_o, color_e):
    while True:
        cod = int(input(color_o + 'Ingrese el codigo del producto.............:'))
        if validar(cod, inv)== False:
             print(color_e + 'El producto no esta en inventario.................')
        else:
             break
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_m + '|', end="")
            print(color_m + f"Descripcion...........................: {articulo['descripcion']:<10} |")
            print(color_m + f"Tamaño................................: {articulo['tam']:<8}\t|")
            print(color_m + f"Tematica..............................: {articulo['deco']:<10}|")
            print(color_m + f"Cantidad..............................: {articulo['cant']:>10.0f}\t |")
            print(color_m + f"Precio................................: {articulo['precio']:>10.2f}\t |")
            break
    op = input(color_o + '¿Desea darle de baja al producto....?(S/N):').capitalize()
    if op == 'S':
            '''
            Se borra al darle un S, creamos un bucle for con dos variables.
            1- la que va a tomar los valores del articulo
            2- el indice que dara la posicion de cada articulo
            usamos un codicional que coincida con el cod que pedimos
            usamos la palabra DEL con la lista y la posicion del articulo a borrar

            op_1: Montar todo en un bucle while externo y alli dentro usamos todo lo que establecimos ya
            '''
            for indice, articulo in enumerate(inv):
                 if cod == articulo['codigo']:
                         del inv[indice]
                         stock_nuevo = open('inventario.json', 'w')
                         json.dump(inv, stock_nuevo)
                         stock_nuevo.close()
    else:
         print(color_m + 'Volviendo al menu principal..............................')