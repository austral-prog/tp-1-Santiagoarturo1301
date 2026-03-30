def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""


    price=int(input())
    descuento=float(input())
    cantidad=int(input())

    precio_descuento=(price- descuento)
    total=(precio_descuento)*cantidad

    print(f"Precio: {price}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {total}")
