import random as rn
rn.seed(1)

def generar_numeros():
    return rn.randint(1000, 9999)

def generar_elementos():
    return rn.randint(10,99)

def generar_lista():
    cantidad = generar_elementos()
    lista = [generar_numeros() for x in range (cantidad)]
    return lista

def calcular_producto(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

def eliminar_valor(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista

def definir_capicua(lista):
    inicio = 0
    fin = len(lista) -1
    while inicio < fin:
        if lista[inicio] != lista[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

lista_numeros = generar_lista()
print(lista_numeros)

valor_eliminar = int(input("Ingresa el elemento que desea eliminar de la lista: "))
print(eliminar_valor(lista_numeros, valor_eliminar)) 


print(f"El producto de todos los elementos de la lista es: {calcular_producto(lista_numeros)}")

if definir_capicua(lista_numeros):
    print("La lista es capicua.")
else:
    print("La lista no es capicua.")