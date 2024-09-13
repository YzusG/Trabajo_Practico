import json
def agregar(inv, color_o):
    cod = int(input(color_o + 'Ingrese Codigo.........................: '))
    desc = input(color_o + 'Tipo de Prenda............................: ')
    talla = input(color_o + 'Ingrese Talla............................: ')
    deco = input(color_o + 'Ingrese Tematica..........................: ')
    precio = float(input(color_o + 'Precio............................: '))

    prenda = {
        'codigo':cod,
        'descripcion':desc,
        'talla':talla,
        'deco':deco,
        'precio':precio
    }
    inv.append(prenda)
    stock = open('inventario.json','w')
    json.dump(inv,stock)
    stock.close()