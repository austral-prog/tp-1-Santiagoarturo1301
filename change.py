def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto= float(input())
    print(gasto)
    print("Dinero recibido")
    recibido=int(input())
    print(recibido)

    vuelto= recibido - gasto

    print("\n" + "Vuelto" + "\n")

    pesos= int(vuelto)
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    centavos= int(round((vuelto-pesos)* 100))
    print(centavos)

