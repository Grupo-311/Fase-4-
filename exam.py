fila_1v = input("Ingrese 4 números entre 3 y 6 separados por coma (fila 1): ")
fila_2v = input("Ingrese 4 números entre 3 y 6 separados por coma (fila 2): ")
fila_3v = input("Ingrese 4 números entre 3 y 6 separados por coma (fila 3): ")
fila_4v = input("Ingrese 4 números entre 3 y 6 separados por coma (fila 4): ")

# Convertir las filas a listas numéricas
f1 = [float(x) for x in fila_1v.split(",")]
f2 = [float(x) for x in fila_2v.split(",")]
f3 = [float(x) for x in fila_3v.split(",")]
f4 = [float(x) for x in fila_4v.split(",")]

matriz = [f1, f2, f3, f4]

# Verificar si todos los valores están en el rango
valores_validos = True
for fila in matriz:
    for elemento in fila:
        if not (3 <= elemento <= 6):
            valores_validos = False
            print(f"{elemento} está fuera del rango permitido (3 a 6).")

# Mostrar matriz solo si es válida
if valores_validos:
    print("\nMatriz válida:")
    for fila in matriz:
        print(fila)
else:
    print("\nNo se puede mostrar la matriz porque contiene valores fuera del rango (3 a 6).")

