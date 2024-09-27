def gen_matriz(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return matriz

def gen_matriz_a(matriz):
    for _ in matriz:
        matriz[0][0] = 1
        matriz[1][1] = 3
        matriz[2][2] = 5
        matriz[3][3] = 7
    return matriz


def main():
    numero = int(input("Ingrese un numero para las filas y columnas: "))
    matriz_gral = gen_matriz(numero)
    print(matriz_gral)
    matriz_a = gen_matriz_a(matriz_gral)
    print(matriz_a)


if __name__ == "__main__":
    main()