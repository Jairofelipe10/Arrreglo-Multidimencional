print("Hola soy Jairo Huatatoca")

# 1. Diccionario inicial
informacion_personal = {
    "nombre": "Jairo Huatatoca",
    "edad": 30,
    "ciudad": "Archidona",
    "profesion": "Cantante"
}

# 2. Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Baeza"

# Nota: Ya existe una profesión en el diccionario inicial,
# Nueva clave-valor que representa la profesión
informacion_personal["desempeño"]= "psicólogo clínico papá"

# 3. Verifique y no existe "telefono" y lo agrego
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985487970 al infinito y más allá"

# 4. Eliminación total de "edad" ya que no es necesaria
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)