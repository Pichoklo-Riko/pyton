opcion = 0
while opcion != 2:
    print("--- MENÚ TIENDA RETAIL ---")
    print("1. Registrar compra")
    print("2. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))
    except:
        print("Error: Debe ingresar un número entero.")
        opcion = 0
        
    if opcion == 1:
        print("Registro de compra")
        monto_valido = False

        while monto_valido == False:
            try:
                monto = int(input("Ingrese monto de compra: $"))

                if monto > 0:
                    monto_valido = True
                else:
                    print("Error: El monto debe ser mayor a cero.")

            except:
                print("Error: Debe ingresar un número entero.")

        tipo_cliente = input("Ingrese el tipo de cliente (Premium/Socio/Normal:): ")
        tipo_cliente = tipo_cliente.lower().strip()  

        if tipo_cliente == "Premium":
            porcentaje = 0.20
        elif tipo_cliente == "Socio":
            porcentaje = 0.10
        elif tipo_cliente == "Nomral":
            porcentaje = 0
        else:
            porcentaje = 0
            print("Tipo de cliente no reconocido. No se aplicará descuento.")

        descuento = monto * porcentaje
        total = monto - descuento    


    elif opcion == 2:
        print("Gracias por usar nuestro sistema.")
    else:
        print("Opción no valida.")