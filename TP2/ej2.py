import random as rn
rn.seed(1)

def generar_lista(numero):
    lista = [rn.randint(1,100) for x in range(numero)]
    return lista

def definir_repetido(lista):
    # esta estructura va a guardar solo los lementos unicos
    elementos_vistos = set()
    for num in lista:
        if num in elementos_vistos:
            return True  # si se encuentra un elemento repetido, no e puede agregar al set
        elementos_vistos.add(num) #se guardan solo los elementos unicos
    return False  # No hay elementos repetidos

def definir_unicos(lista):
    elementos_unicos = set()
    for num in lista:
        elementos_unicos.add(num)
    return elementos_unicos
    
n = int(input("Ingrese la cantidad de numeros de la lista: "))
lista_general = generar_lista(n)
print (lista_general)

print(definir_repetido(lista_general))

print(f"Los elementos unicos de la lista es: {definir_unicos(lista_general)}")
