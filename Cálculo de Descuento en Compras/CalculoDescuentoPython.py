# Creación de la función calcular_descuento
# Parámetros: monto total y porcentaje de descuento

def calcular_descuento(monto_total, porcentaje_descuento=25):
    """
    Calcula el descuento basado en el monto total y un porcentaje de descuento.

    Args:
        monto_total (float): El monto total de la compra
        porcentaje_descuento (float): Porcentaje de descuento (25% por defecto)

    Returns:
        float: El monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# Llamada 1: monto total (25% por defecto)
compra_1 = 150
descuento_1 = calcular_descuento(compra_1)
monto_final1 = compra_1 - descuento_1

# Llamada 2: monto total y porcentaje personalizado
compra_2 = 150
descuento_2 = calcular_descuento(compra_2, 60)  # 60% de descuento
monto_final2 = compra_2 - descuento_2

# Mostrar resultados
print("Compra 1:")
print(f"Monto total: ${compra_1:.2f}")
print(f"Descuento (25%): ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

print("Compra 2 (descuento personalizado):")
print(f"Monto total: ${compra_2:.2f}")
print(f"Descuento (60%): ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")