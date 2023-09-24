nota_parcial1 = float(input("Ingresa la nota del primer parcial: "))
nota_parcial2 = float(input("Ingresa la nota del segundo parcial: "))
nota_parcial3 = float(input("Ingresa la nota del tercer parcial: "))
# Calcular el total de las notas
total_notas = nota_parcial1 + nota_parcial2 + nota_parcial3


# Verificar si el estudiante aprobó
if total_notas > 14:
        print("El estudiante está aprobado con un total de", total_notas, "puntos.")
else:
            print("El estudiante está reprobado con un total de", total_notas, "puntos.")
