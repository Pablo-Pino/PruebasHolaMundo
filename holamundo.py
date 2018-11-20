import sys

def holamundo():
    cadena = None
    try:
        name = sys.argv[1]
        cadena = "Hola " + name
        print(cadena)
    except IndexError:
        cadena = "No se han pasado suficientes parametros al programa"
        print(cadena)
    return cadena

holamundo()