# Pedir los números al usuario
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

# Realizar los cálculos
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Manejar la división para evitar el error de división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir entre cero"

# Mostrar todos los resultados
print("\n--- Resultados del Cálculo ---")
print(f"Suma:          {numero1} + {numero2} = {suma}")
print(f"Resta:         {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División:       {division}")
