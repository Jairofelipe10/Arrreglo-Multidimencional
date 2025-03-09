# Definir la matriz 3D de temperaturas
ciudades = ["Archidona", "Tena", "Chaco"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Matriz 3D: [ciudad][día][semana]
temperaturas = [
    [  # Archidona
        [15, 16, 14, 17],  # Semana 1
        [16, 15, 17, 14],  # Semana 2
        [14, 15, 16, 15],  # Semana 3
        [17, 16, 15, 14]   # Semana 4
    ],
    [  # Tena
        [22, 23, 21, 24],  # Semana 1
        [23, 22, 24, 21],  # Semana 2
        [21, 22, 23, 22],  # Semana 3
        [24, 23, 22, 21]   # Semana 4
    ],
    [  # Chaco
        [28, 29, 27, 30],  # Semana 1
        [29, 28, 30, 27],  # Semana 2
        [27, 28, 29, 28],  # Semana 3
        [30, 29, 28, 27]   # Semana 4
    ]
]
# Calcular y mostrar promedios
for i in range(len(ciudades)):  # Iterar sobre ciudades
    print(f"\nPromedios para {ciudades[i]}:")
    for j in range(semanas):  # Iterar sobre semanas
        suma_temperaturas = 0
        for k in range(len(temperaturas[i][j])):  # Iterar sobre días
            suma_temperaturas += temperaturas[i][j][k]
        promedio = suma_temperaturas / len(temperaturas[i][j])
        print(f"  Semana {j + 1}: {promedio:.2f}°C")