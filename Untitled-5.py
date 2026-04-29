print("Bienvenido a nuestra tienda")
precio = int(input("Ingrese cuanto quiere gastar: "))
if precio >= 50000:
    total = precio * 0.90
else:
    total = precio
print("Total a pagar: " , int(total))