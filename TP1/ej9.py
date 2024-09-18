import random as rn

def naranjas_cosechadas(naranjas: int):
    '''Carga una lista con números enteros random para determinar el peso deseado.
    Pre: naranjas va a ser la cantidad de naranjsa ingresadas.
    Post: devuelve datos tales como:  
    la cantidad de naranjas jugo, las restantes, la cantidad de cajones que llenan, los camiones que viajan.
    
    '''

        # Constantes
    PESO_MINIMO = 200  # gramos
    PESO_MAXIMO = 300  # gramos
    CAJON = 100
    CAPACIDAD_CAMION_KG = 500  # kg
    OCUPACION_MINIMA_CAMION = 80  # 80%

    # Variables
    naranjas_jugo = 0
    naranjas_validas = 0
    peso_total_kg = 0
    
    pesos = [rn.randint(150,350) for x in range (naranjas)]
    print(pesos)

    for peso in pesos:
        if peso < PESO_MINIMO or peso > PESO_MAXIMO:
            naranjas_jugo += 1
        else:
            naranjas_validas += 1
            peso_total_kg += peso / 1000 #convertir de gramos a kg

    cajones_llenos = naranjas_validas // CAJON
    naranjas_resto = naranjas_validas % CAJON

    peso_total_kg += naranjas_resto * (peso / 1000)
    peso_minimo_camion = (OCUPACION_MINIMA_CAMION * CAPACIDAD_CAMION_KG) / 100
    cantidad_camiones = 0

    if peso_total_kg >= peso_minimo_camion:
        cantidad_camiones += peso_total_kg // CAPACIDAD_CAMION_KG
        if peso_total_kg % CAPACIDAD_CAMION_KG > 0:
            cantidad_camiones += 1
    else:
        cantidad_camiones = 0
        print("El camión no viaja")

    
    print(f"Los cajones que se pueden llevar son: {cajones_llenos}")
    print(f"La cantidad de naranjas jugo es: {naranjas_jugo}")
    print(f"Las naranjas que restaron son {naranjas_resto}")
    print(f"La cantidad de camiones que viajaran son: {cantidad_camiones}")
    
    return None

# Solicitar entrada al usuario
naranjas = int(input("Ingrese la cantidad de naranjas: "))

naranjas_cosechadas(naranjas)