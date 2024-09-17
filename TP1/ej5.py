es_oblongo = lambda x: any(z * (z+1) == x for z in range (1, x)) #z en cada iteracion prueba multiplicar por su numero siguiente hasta encontrar el resultado de x.
''' Esta funcion lambda imprime si es o no oblongo.
pre : recibe un numero entero, para probar si es oblongo o no.
post : Si es oblongo devuelve True, por su contrario, False.
'''
x = int(input("Ingrese un numero oblongo: "))
print(es_oblongo(x))

es_triangulo = lambda a: any(a == n * (n + 1) // 2 for n in range(1, a)) #n en cada iteracion se va a multiplicar por su numero siguiengte y al resultado lo divide * 2siguiendo esta funcion n(n + 1) todo sobre 2
"""Esta funcion lambda devuelve si es un numero triangulo o no. Sumando numeros consecutivos hasta llegar al resultado del numero ingresado.
pre : recibe un numero entero, para probar si es triangulo.
post : devuelve True si es triangulo o False en su contrario."""
a = int(input("Ingrese un numero triangular: "))
print(es_triangulo(a))
