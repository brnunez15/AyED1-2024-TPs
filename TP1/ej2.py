
def es_bisiesto (anio: int) -> bool:
    '''Deevuelve True or False segun la condicion
    pre: Debe ser bisiesto teniendo en cuenta que sea divisible por 4 y a su vez que no sea divisible por 100 o que sea divisible por 400.
    post: Devuelve True si se cumple la condicion, o False si no es asi.'''
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def fecha(dia: int, mes: int, anio: int) -> bool:
    """Devuelve la validez de la fecha ingresada.
    pre: Deben ser tres numeros enteros positivos, teniendo en cuenta la canidad de dias correspondientes de cada mes, incluyendo los de los años bisiestos.
    post: Devuelve True o False dependiendo de la validez de la fecha."""
    if mes >= 1 or mes <= 12:
        return True
    if mes == 2:
        if es_bisiesto(anio):
            return dia >= 1 or dia <= 29
        else:
            dia >= 1 or dia <= 28
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return dia >= 1 or dia <= 31
        else:
            return dia >=1 or dia <= 30

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

if fecha(dia, mes, anio):
    if es_bisiesto(anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida y fue un año bisiesto.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
else:
    print(f"La fecha {dia}/{mes}/{anio} no es válida.")