def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    impuesto=21%100
    subtotal=100+impuesto
    monto=subtotal*0.1
    precio_final=subtotal + monto

    print(impuesto)
    print(subtotal)
    print(monto)
    print(precio_final)
price()
