import random as rn
rn.seed(1)

def generar_lista1():
    lista = lista = [rn.randint(1,100) for x in range(10)]
    return lista

def generar_lista2():
    lista = [rn.randint(1,100) for x in range(10)]
    return lista

def eliminar_elementos(lista_uno, lista_dos):
    for elemento in lista_dos:
        while elemento in lista_uno:  # Elimina todas las ocurrencias
            lista_uno.remove(elemento)
    
lista_1 = generar_lista1()
print(f"Lista original: {lista_1}")

lista_2 = generar_lista2()
print(f"Lista de valores a eliminar: {lista_2}")

eliminar_elementos(lista_1, lista_2)
print(f"Lista resultante: {lista_1}")