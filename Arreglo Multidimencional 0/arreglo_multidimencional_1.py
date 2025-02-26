# Programa para búsqueda en matriz bidimensional

def buscar_valor(matriz, valor_buscado):
    """
    Función que busca un valor en una matriz bidimensional
    Retorna True y la posición si lo encuentra, False y None si no
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor_buscado:
                return True, (i, j)  # Retorna True y la posición como tupla
    return False, None  # Retorna False y None si no se encuentra


def main():
    # Crear una matriz 3x3 con valores numéricos
    matriz = [
        [4, 7, 2],
        [9, 1, 5],
        [3, 8, 6]
    ]

    # Mostrar la matriz inicial
    print("Matriz inicial:")
    for fila in matriz:
        print(fila)

    # Definir el valor a buscar
    valor_buscado = 5

    # Realizar la búsqueda
    encontrado, posicion = buscar_valor(matriz, valor_buscado)

    # Mostrar resultado
    if encontrado:
        print(f"\n¡El valor {valor_buscado} fue encontrado!")
        print(f"Posición: fila {posicion[0]}, columna {posicion[1]}")
    else:
        print(f"\nEl valor {valor_buscado} no se encontró en la matriz")


# Ejecutar el programa
if __name__ == "__main__":
    main()