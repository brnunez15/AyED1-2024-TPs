def informar_ingresos():

    ingresos = {}

    while True:
        n_socio = int(input("Ingrese su número de socio (o 0 para finalizar las cargas): "))
        
        if n_socio == 0:
            print("Finalizando las cargas...")
            break

        if n_socio >= 10000 and n_socio <= 99999:
            
            if n_socio in ingresos:
                ingresos[n_socio] += 1
            else:
                ingresos[n_socio] = 1
        else:
            print("Número de socio incorrecto. Deben ser 5 dígitos.")

    return ingresos

def dar_baja(entradas):

    for key, value in entradas.items():
        print(f"Número de socio: {key}, Visitas: {value}")

    while True:
        n_socio_baja = int(input("Ingrese el numero de socio dado de baja (0 para salir): "))

        if n_socio_baja == 0:
            print("Saliendo...")
            break

        if n_socio_baja >= 10000 and n_socio_baja <= 99999:
            if n_socio_baja in entradas:
                cantidad_eliminada = entradas[n_socio_baja]
                del entradas[n_socio_baja]
                print(f"Se eliminaron {cantidad_eliminada} ingresos para el socio {n_socio_baja}.")


def main():
    ingresos = informar_ingresos()
    dar_baja(ingresos)

if __name__ == "__main__":
    main()