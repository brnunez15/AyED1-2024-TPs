def maximo(a,b,c) -> int:
    '''Devuelve el número máximo de los ingresado siempre que sea único.
    Precondicion: deben ingresarse números enteros positivos.
    Postcondicion: Devuelve el maximo estricto. De no ser asi, devuelve -1.
    '''
    if c < b:
        if b < a:
            max = a
        else:
            if b == a:
                max = -1
            else:
                max = b
    elif a < b:
        if b < c:
            max = c
        else:
            if b == c:
                max = -1
            else:
                max = b
    else:
        if a == c:
            max = -1
    return max


a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

maximo_estricto = maximo(a,b,c)

if maximo_estricto == -1:
    print ("No existe un maximo unico")
else:
    if maximo_estricto > 0:
        print (f"El numero maximo es:  {maximo_estricto}")
    else:
        print("El numero debe ser positivo")