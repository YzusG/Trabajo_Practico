import json
def agregar(inv, color_o):
    cod = int(input(color_o + 'Ingrese Codigo.........................: '))
    desc = input(color_o + 'Descripcion...............................: ')
    tam = input(color_o + 'Tamaño...................................: ')
    deco = input(color_o + 'Tematica..................................: ')
    cant = input(color_o + 'Cantidad..................................: ')
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