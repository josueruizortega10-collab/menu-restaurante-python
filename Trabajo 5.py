# ==========================================
# PROBLEMA 2 - MENU DE RESTAURANTE
# ==========================================

# Matriz:
# [Nombre del Producto, Categoria, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rapida", 25],
    ["Pizza Familiar", "Comida Rapida", 45],
    ["Ensalada Cesar", "Saludable", 18],
    ["Sushi", "Japonesa", 50],
    ["Pasta Alfredo", "Italiana", 35],
    ["Tacos Mexicanos", "Mexicana", 28]
]

# ==========================================
# FUNCION PARA CALCULAR PRECIO FINAL
# ==========================================

def calcular_precio_final(categoria_producto, precio_base,
                           categoria_objetivo, umbral):

    # Verificar condiciones
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral:
        
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    else:
        precio_final = precio_base

    return precio_final


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

print("====================================")
print("   MENU DE PROMOCIONES RESTAURANTE")
print("====================================")

# Categoria para aplicar descuento
categoria_objetivo = input("Ingrese la categoria objetivo: ")

# Umbral minimo
umbral = float(input("Ingrese el precio minimo para aplicar descuento: "))

print("\nRESULTADOS DE LA PROMOCION")
print("====================================")

# Recorrer matriz
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamar funcion
    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    # Mostrar resultados
    print("\nProducto:", nombre)
    print("Categoria:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", round(precio_final, 2))

print("\n====================================")
print("      FIN DEL PROGRAMA")
print("====================================")