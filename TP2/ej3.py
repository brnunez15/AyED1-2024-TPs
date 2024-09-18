def generar_lista(n):
    cuadrados = [i ** 2 for i in range(1, n + 1)]
    return cuadrados

def ultimos_10(lista):
    for elem in lista[-10:]:
        lista.append(elem)
    return lista

numero = int(input("Ingrese un numero: "))

lista_cuadrados = generar_lista(numero)
print(lista_cuadrados)

ultimos_diez = ultimos_10(lista_cuadrados)
print(f"Los ultimos 10 valores de la lista son: {ultimos_diez}")