def definir_capicua(cadena):
    inicio = 0
    fin = len(cadena) -1
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    return True

def ingresar_cadena(): 
    cadena = input("Ingrese una cadena de caracteres: ")
    if definir_capicua(cadena):
        print("La cadena es capicua.")
    else:
        print("La cadena no es capicua.")

ingresar_cadena()