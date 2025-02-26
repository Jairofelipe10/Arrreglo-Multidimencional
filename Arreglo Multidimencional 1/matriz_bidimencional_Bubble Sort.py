# Pasos para ordenar una fila específica de una matriz bidimensional

def bubble_sort(arr):

   # Bubble Sort para ordenar una lista en orden ascendente

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Elementos matriz fila
def ordenar_fila_matriz(matriz, fila):
    if fila < 0 or fila >= len(matriz):
        print("Fila no válida")
        return

    # Para no cambiar la fila original, la copiamos.
    fila_a_ordenar = matriz[fila].copy()

    # Ordenamos la fila con Bubble sort
    bubble_sort(fila_a_ordenar)

    # Hacemos una nueva matriz con la fila ordenada
    nueva_matriz = [fila_matriz.copy() for fila_matriz in matriz]
    nueva_matriz[fila] = fila_a_ordenar

    return nueva_matriz


def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


# Matriz original 3x3
matriz = [
    [9, 2, 5],
    [7, 1, 4],
    [8, 6, 3]
]

print("Matriz original:")
imprimir_matriz(matriz)

# Ordenar la fila 2
fila_a_ordenar = 2
matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
imprimir_matriz(matriz_ordenada)