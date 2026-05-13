def suma():
    num1 = 3
    num2 = 5
    return(num1 + num2)
#LLamando a la función, ejecuta todo el contenido de la función.
print("La suma es: ",suma())

def suma(a,b):
    sumar = a + b
    print(f"La suma de los argumentos es: {sumar}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma(num1,num2)