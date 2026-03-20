def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio_notas=(8+7+9)/3
    nota_maxima=9
    nota_minima=7
    promedio_10=(10-promedio_notas)

    print(promedio_notas)
    print(nota_maxima)
    print(nota_minima)
    print(promedio_10)
grades()
