# Escritura del archivo de texto utilizando métodos como write y readline
# Definimos el nombre del archivo
file_name = 'my_notes.txt'

# Abrimos el archivo en modo escritura ('w')
archivo_escritura = open(file_name, 'w')

# Escribimos tres líneas de notas personales usando write()
archivo_escritura.write("Linea 1: Terminar el proyecto de tecnologia de programación.\n")
archivo_escritura.write("Linea 2: Llorar la próxima semana si no termino el proyecto.\n")
archivo_escritura.write("Linea 3: Amanecer para culminar dechi proyecto.\n")

# Cerramos el archivo después de escribir
archivo_escritura.close()

# Lectura del archivo de texto
# Abrimos el archivo en modo lectura ('r')
archivo_jairo = open(file_name, 'r')

# Leemos el contenido e imprimimos en la consola
line = archivo_jairo.readline()  # Leemos la primera línea
while line:  # Continuamos mientras haya líneas por leer
    print(line.strip())  # Mostramos la línea sin saltos adicionales
    line = archivo_jairo.readline()  # Leemos la siguiente línea

# Cerramos el archivo después de leer
archivo_jairo.close()
