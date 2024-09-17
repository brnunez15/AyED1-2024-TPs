def concatenar_numeros (n1: int, n2: int) -> int:
    """ Esta funcion concatena dos numeros enteros.
        pre: Recibe dos numeros enteros positivos
        post: Devuelve la concatenacion entre esos numeros.
    """
    resultado = n1 + n2
    return resultado

n1 = input("Ingrese un numero entero: ")
n2 = input("Ingrese un numero entero: ")
print(concatenar_numeros(n1, n2))