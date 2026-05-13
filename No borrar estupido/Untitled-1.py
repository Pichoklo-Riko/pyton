try:

   resultado = 10/0
   print(f"el resultado es: {resultado}")
except ZeroDivisionError as error:
   print("División por zero")