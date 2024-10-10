from funciones.validar import validar
import json
def agregar(inv, color_o, color_e):
    while True:
        cod = int(input(color_o + 'Ingrese Codigo.........................: '))
        if validar(cod, inv, color_e):
            print(color_e + 'El codigo ya existe..........')
        else:
            break
    desc = input(color_o + 'Descripcion...............................: ')
    tam = input(color_o + 'Tamaño...................................: ')
    deco = input(color_o + 'Tematica..................................: ')
    cant = int(input(color_o + 'Cantidad..................................: '))
    precio = float(input(color_o + 'Precio............................: '))

    articulo = {
        'codigo': cod,
        'descripcion': desc,
        'tam': tam,
        'deco': deco,
        'cant': cant,
        'precio': precio
    }
    inv.append(articulo)
    stock = open('inventario.json','w')
    json.dump(inv,stock)
    stock.close()