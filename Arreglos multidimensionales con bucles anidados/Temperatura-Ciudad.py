# Definir la matriz 3D de temperaturas
# Primera dimensión: Ciudades (Archidona, Tena, Chaco)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (Lunes,Martes, Miercoles, Jueves, Viernes, Sabado, domingo)

temperaturas = [
    [   # Archidona
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 91}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 90}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 77},
            {"day": "Viernes", "temp": 83},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 89}
        ]
    ],
    [   # Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 79},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 88}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 76},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 81},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 87}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 77},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 86}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 71},
            {"day": "Martes", "temp": 74},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 85}
        ]
    ],
    [   # Chaco
        [   # Semana 1
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 73},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 81},
            {"day": "Domingo", "temp": 84}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 69},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 74},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 71},
            {"day": "Miércoles", "temp": 73},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 67},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 81}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Archidona", "Tena", "Chaco"]
for ciudad, nombre_ciudad in zip(temperaturas, ciudades):
    for semana in ciudad:
        suma_temperaturas = sum(dia['temp'] for dia in semana)
        promedio = suma_temperaturas / len(semana)
        print(f"{nombre_ciudad}, Semana {ciudad.index(semana) + 1}: Promedio de temperatura = {promedio:.2f}°F")