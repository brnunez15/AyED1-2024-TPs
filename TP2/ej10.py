import random as rn
rn.seed(1)

def generar_lista():
    lista = [rn.randint(1,100) for i in range(10)]
    return lista

def lista_impares(lista):
    lista1 = list(filter(lambda x: x % 2 != 0, lista))
    return lista1

lista_1 = generar_lista()
print(f"Lista generada: {lista_1}")

# Obtener los números impares
impares = lista_impares(lista_1)
print(f"Números impares: {impares}")