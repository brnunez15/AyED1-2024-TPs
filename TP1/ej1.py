def mayor_de_tres (num1: int, num2: int, num3: int) -> int:
    lista = [num1, num2, num3]
    mayor = max(lista)
    return mayor

num1 = 4
num2 = 90
num3 = 9


mayores = mayor_de_tres(num1, num2, num3)
print(mayores)
