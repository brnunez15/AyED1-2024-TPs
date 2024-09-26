def centrar_cadena(string: str, ancho: int) -> str:
    espacios = (ancho - len(string)) // 2 #calculo el largo de la cadena - el ancho para generar espaciados tanto a la derecha como a la izquierda. Y lo divido por dos para que el resultado sea la cantidad de espaciados de cada lado.
    cadena_centrada = ' ' * espacios + string #los espacios van a ser: ' ' por la cantidad de espacios de cada lado + la cadena.
    return cadena_centrada

def main() -> None:
    cadena= input("Ingrese una cadena de caracteres: ")
    ancho_cadena = int(input("Ingrese el ancho para el espaciado: "))
    cadena_centrada = centrar_cadena(cadena, ancho_cadena)
    print(cadena_centrada)

if __name__ == "__main__":
    main()