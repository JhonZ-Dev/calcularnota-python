nota_parcial1 = None
nota_parcial2 = None
nota_parcial3 = None


# Solicitar las notas hasta que no sean nulas
while nota_parcial1 is None:
    nota_parcial1_str = input("Ingresa la nota del primer parcial: ")
    if nota_parcial1_str.strip():  # Verificar que no sea una cadena vacía
        try:
            nota_parcial1 = float(nota_parcial1_str)
        except ValueError:
            print("Error: Ingresa un número válido para la nota del primer parcial.")


while nota_parcial2 is None:
    nota_parcial2_str = input("Ingresa la nota del segundo parcial: ")
    if nota_parcial2_str.strip():
        try:
            nota_parcial2 = float(nota_parcial2_str)
        except ValueError:
            print("Error: Ingresa un número válido para la nota del segundo parcial.")


while nota_parcial3 is None:
    nota_parcial3_str = input("Ingresa la nota del tercer parcial: ")
    if nota_parcial3_str.strip():
        try:
            nota_parcial3 = float(nota_parcial3_str)
        except ValueError:
            print("Error: Ingresa un número válido para la nota del tercer parcial.")

# Calcular el total de las notas
total_notas = nota_parcial1 + nota_parcial2 + nota_parcial3

# Verificar si el estudiante aprobó
if total_notas > 14:
    print("El estudiante está aprobado con un total de", total_notas, "puntos.")
else:
    print("El estudiante está reprobado con un total de", total_notas, "puntos.")

