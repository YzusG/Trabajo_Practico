from funciones.separar import separar
def listado(inv, color_m, color_p):
    separar(color_m)
    titulo = ("Codigo","Descripcion ","Tamaño","Cantidad","Precio")
    for i in titulo:
        print(color_m + f"{i:<10}", end="")
    print();separar(color_m)
    for articulo in inv:
        print(color_p + f"{articulo['codigo']:<10}", end="")
        print(color_p + f"{articulo['descripcion']:<13}", end="")
        print(color_p + f"{articulo['tam']:<10}", end='')
        print(color_p + f"{articulo['cant']:>4.0f}", end='')
        print(color_p + f"{articulo['precio']:>11.2f}")
    separar(color_m)