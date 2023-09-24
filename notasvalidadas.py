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

