a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
lista = [ i  for i in range (a, b) if i % 7 == 0 and i % 5 != 0 ]
print(lista)