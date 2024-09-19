from typing import List

def normalizar (lista: List[int]) -> List[float]:
    total = sum(lista)
    lista_normalizada = [x / total for x in lista]
    return lista_normalizada
    
def verificar():
    pruebas = [
        ([1, 1, 2], [0.25, 0.25, 0.50]),
        ([2, 4 ,5], [0.1818182, 0.363636, 0.454545]),
        ([2, 2, 2], [0.333333, 0.333333, 0.333333])
    ]

    for lista, normalizado in pruebas:
        resultado = normalizar(lista)
        print(f"normalizar({lista}) = {resultado}, esperado = {normalizado}")

verificar()