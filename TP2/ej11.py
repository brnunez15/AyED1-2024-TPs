def registrar_listado():
    urgencia = []
    turno = []
    
    while True:
        n_afiliado = int(input("Ingrese su numero de afiliado. -1 para salir: "))
        if n_afiliado == -1:
            print("Saliendo...")
            break
        
        if n_afiliado >= 1000 and n_afiliado <= 9999:
            paciente = int(input("Ingrese 0 por urgencia o 1 por turno: "))
            if paciente == 0:
                urgencia.append(n_afiliado)
            elif paciente == 1:
                turno.append(n_afiliado)
            else:
                print("Opción no válida. Intente de nuevo.")
        else:
            print("Numero invalido. Deben ser 4 digitos")
    
    return urgencia, turno

def turno_urgencia(lista_urgencias, lista_turnos):
    while True:
        n_afiliado = int(input("Ingrese el numero de un afiliado. -1 para salir: "))
        if n_afiliado == -1:
            print("Saliendo...")
            break
        
        cant_turnos = lista_turnos.count(n_afiliado)
        cant_urgencias = lista_urgencias.count(n_afiliado)
        
        print(f"La cantidad de veces que {n_afiliado} fue atendido por turno: {cant_turnos}")
        print(f"Y por urgencias: {cant_urgencias}")


listado = registrar_listado()
urgencias, turnos = listado  #Desempaquetar las listas

turno_urgencia(urgencias, turnos)