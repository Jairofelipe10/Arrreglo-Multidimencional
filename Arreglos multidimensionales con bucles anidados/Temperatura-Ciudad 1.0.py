# Matriz 3D de temperaturas en grados Celsius (°C) Napo-Ecuador
temperaturas = [
    [  # Archidona
        [  # Semana 1
            {"day": "Lunes", "temp": 25}, {"day": "Martes", "temp": 26}, {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 28}, {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 24}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 25}, {"day": "Viernes", "temp": 29}, {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 23}, {"day": "Martes", "temp": 26}, {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 28}, {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 25}, {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 23}, {"day": "Viernes", "temp": 27}, {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [  # Tena
        [  # Semana 1
            {"day": "Lunes", "temp": 23}, {"day": "Martes", "temp": 25}, {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 27}, {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 24}, {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23}, {"day": "Viernes", "temp": 26}, {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 21}, {"day": "Martes", "temp": 23}, {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 25}, {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 22}, {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 24}, {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [  # Chaco
        [  # Semana 1
            {"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 22}, {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 24}, {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 23}, {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 25}
        ]
    ]
]

# Lista de nombres de ciudades
ciudades = ["Archidona", "Tena", "Chaco"]


# Función para calcular la temperatura promedio de una ciudad
def calcular_promedio_ciudad(datos_temperaturas, nombre_ciudad):
    """
    Calcula la temperatura promedio de una ciudad durante todas las semanas disponibles.

    Parámetros:
        datos_temperaturas (list): Matriz 3D con datos de temperaturas.
        nombre_ciudad (str): Nombre de la ciudad ("Archidona", "Tena" o "Chaco").

    Retorna:
        float: Promedio de temperaturas de la ciudad especificada.
    """
    # Encontrar el índice de la ciudad en la lista de ciudades
    try:
        indice_ciudad = ciudades.index(nombre_ciudad)
    except ValueError:
        return f"Error: La ciudad '{nombre_ciudad}' no está en la lista."

    # Obtener los datos de la ciudad específica
    ciudad = datos_temperaturas[indice_ciudad]

    # Sumar todas las temperaturas de la ciudad
    suma_total = 0
    total_dias = 0
    for semana in ciudad:
        for dia in semana:
            suma_total += dia["temp"]
            total_dias += 1

    # Calcular el promedio
    promedio = suma_total / total_dias
    return promedio


# Pruebas de la función
for ciudad in ciudades:
    promedio = calcular_promedio_ciudad(temperaturas, ciudad)
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f}°C")