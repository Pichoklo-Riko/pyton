import utils as u

personas = []
while True:
    u.mostrar_menu()

    try:
        opcion = int(input("Ingrese una opcion: "))
    except:
        print("La opción debe ser númerica")
        opcion = 0

    if opcion == 1:
        print("Esra es la opción 1")
    elif opcion == 2:
        print("Esta es la opción 2")
    elif opcion == 3:
        print("Gracias por usar el sistema")
        break
    else:
        print("La opción no es válida")      