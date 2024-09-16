def cambio_cliente (total_compra: int, dinero_recibido: int) -> int:
    """Esta funcion va a mostrar el vuelto por cada billete correspondiente.
    pre: ingresar dos numeros enteros refiriendose a el total de la compra y al dinero que sera recibido.
    post: Va a devolver la cantidad de billetes restantes al dinero recibido."""
    billetes = [5000, 1000, 500, 200, 100, 50, 10]   #creo una lista con los billetes 
    cantidad_billetes = {billete: 0 for billete in billetes} #primero recorro la lista billetes y pongo como variable del elemento: "billete" que la pongo como clave del diccionario. Y su valor es 0 que luego sera utilizado como contador.

    cambio = dinero_recibido - total_compra #inicializo la variable "cambio"

    if cambio < 0: #Valido si el cambio no alcanza para el dinero recibido
        print("El cambio no puede entregarse debido a falta de billetes.")
    else:
        if cambio == 0: #Aca valido si coincide el dinero recibido con el total de la compra, por ende el cambio sera 0.
            print("El dinero recibido es justo. No requiere de cambio.")

    for billete in billetes: #recorremos la lista de billetes
        while cambio >= billete: #En cada iteracion va a representar el valor del billete. Si el cambio es mayor o igual al billete, entra al while.
            cambio -= billete #Si entro, el cambio se restara de acuerdo al valor del billete y a su vez cambiara su valor por el resultado de este.
            cantidad_billetes[billete] += 1 #Aca es donde uso el contador del valor del diccionario creado anteriormente. Cada vez que se reste el cambio y el billete, el valor de la clave billete va a sumarse de acuerdo a la cantidad de iteraciones que pasa por ese billete.
    print(cantidad_billetes)
            


total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero a pagar: "))

cambio_cliente(total_compra, dinero_recibido)