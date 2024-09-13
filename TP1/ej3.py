def viajes (cant_viajes: int) -> int:
    '''Devuelve un entero, correspondiente al total de gastos de viajes.
    pre: Los numeros que corresponden a la cantidad de viajes, deben respetar los rangos.
    post: Esto tiene que devolver un numero entero, es drecir, el total de los gastos.'''
    tarifa_maxima = 650
    if cant_viajes >= 1 or cant_viajes <= 20:
        total = cant_viajes * tarifa_maxima
    elif cant_viajes >= 21 or cant_viajes <=30:
        total = (tarifa_maxima * 20) / 100
    elif cant_viajes >= 31 or cant_viajes <= 40:
        total = (tarifa_maxima * 30) / 100
    elif cant_viajes >= 40:
        total = (tarifa_maxima * 40) / 100
    return total

cant_viajes = int(input("Ingrese la cantidad ded viajes realizados en un mes: "))

total = viajes(cant_viajes)

if cant_viajes > 0:
    print(f"El costo total de los viajes realizados en un mes es: ${total}")
else:
    print("Debe ser al menos un viaje")

