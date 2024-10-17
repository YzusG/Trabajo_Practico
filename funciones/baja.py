import json
from funciones.validar import validar
from funciones.separar import separar

def baja(inv, color_m, color_o, color_e, color_p):
    while True:
     try:
        cod =input(color_o + 'Ingrese el codigo del producto.................:')
        cod = int(cod)
        if validar(cod, inv)== False:
             print(color_e + 'El producto no esta en inventario.................')
        else:
             break
        separar(color_m)
     except Exception as e:
          print(color_e + 'El codigo es incorrecto..............................')
    for articulo in inv:
        if cod == articulo['codigo']:
            print(color_p + f"Descripcion...........................: {articulo['descripcion']:<10}|")
            print(color_p + f"Tamaño................................: {articulo['tam']:<10}|")
            print(color_p + f"Cantidad..............................: {articulo['cant']:>10.0f}|")
            print(color_p + f"Precio................................: {articulo['precio']:>10.2f}|")
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
                         print(color_e + 'Articulo eliminado..............')
    else:
         print(color_p + 'Volviendo al menu principal..............................')