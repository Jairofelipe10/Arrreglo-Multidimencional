# Búsqueda de matriz bidimensional

def buscar_valor(matriz, valor_buscado):
    """
    Función matriz bidimensional
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor_buscado:
                return True, (i, j)  # La posición
    return False, None  # Retorna False si en verdad no se encuentra


def main():
    # Valores numéricos para la matriz 3x3
    matriz = [
        [7, 2, 12],
        [9, 10, 5],
        [3, 8, 13]
    ]

    # Desarrollo de la matriz inicial
    print("Matriz principal:")
    for fila in matriz:
        print(fila)

    # Inicio del valor a registrar
    valor_registrado = 8

    # Búsqueda del valor registrado
    encontrado, posicion = buscar_valor(matriz, valor_registrado)

    # Resultados únicos
    if encontrado:
        print(f"\n¡El valor {valor_registrado} fue encontrado!")
        print(f"Posición: fila {posicion[0]}, columna {posicion[1]}")
    else:
        print(f"\nEl valor {valor_registrado} desafortunadamente no esta en la matriz")


# Ejecutar el programa
if __name__ == "__main__":
    main()