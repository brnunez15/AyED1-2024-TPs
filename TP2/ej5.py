def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
def verificar():

    pruebas = [
        ([1, 2, 3], True),
        ([3, 2, 1], False),
        ([15, 16, 17, 18], True),
        ([22, 21, 20, 19], False),
        (['a', 'b', 'c'], True),
        (['c', 'b', 'a'], False)
    ]

    for lista, resultado_esperado in pruebas:
        resultado = ordenada(lista)
        print(f"normalizar({lista}) = {resultado}. Esperado = {resultado_esperado}")

verificar()
