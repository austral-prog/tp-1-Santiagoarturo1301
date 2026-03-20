from math import pi


def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5
    area_circulo=pi * radio**2
    circuferencia_circulo=2 * pi * radio
    print(area_circulo)
    print(circuferencia_circulo)

circle()
