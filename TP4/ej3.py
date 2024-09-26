def obtener_claves(clave_maestra: str) -> tuple:
    clave1 = ""
    clave2 = ""

    for posicion, digito in enumerate(clave_maestra):
        if (posicion + 1) % 2 != 0:
            clave1 += digito
        else:
            clave2 += digito

    return clave1, clave2

def main():
    clave_maestra = input("Ingrese la clave maestra: ")
    clave1, clave2 = obtener_claves(clave_maestra)
    print(f"clave 1 (posiciones impares):  {clave1}")
    print(f"clave 2 (posiciones pares):  {clave2}")

if __name__ == "__main__":
    main()