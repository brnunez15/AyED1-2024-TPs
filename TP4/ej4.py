def gen_romanos(num : int) -> str:
    if num < 0 or num > 3999:
        return "El numero debe estar entre 0 y 3999."
    romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    resultado =""

    for valor, romano in romanos:
        while num >= valor:
            resultado += romano
            num -= valor

    return resultado

def main():
    numero = int(input("Ingrese un numero: "))
    simbolo = gen_romanos(numero)
    print(f"El número en romano es: {simbolo}")

if __name__ == "__main__":
    main()