def validarCodigo(codigo):
    codigo_str = str(codigo)
    if len(codigo_str) != 6 or not codigo_str.isdigit():
        return 0
    tipo = int(codigo_str[0])
    area = int(codigo_str[1:4])
    if tipo not in [1, 2, 3]:
        return 0
    if area < 101 or area > 108:
        return 0
    return 1

def prestamo(codigo):
    if validarCodigo(codigo) == 0:
        return 0
    tipo = int(str(codigo)[0])
    if tipo == 1:
        return 8
    elif tipo == 2:
        return 3
    elif tipo == 3:
        return 1

def recoleccion(codigo):
    if validarCodigo(codigo) == 0:
        return 0
    tipo = int(str(codigo)[0])
    if tipo == 1:
        return 500
    elif tipo == 2:
        return 1000
    elif tipo == 3:
        return 5000

def menu():
    total_libros_prestados = 0
    total_dinero_recolectado = 0

    while True:
        print("\nBiblioteca LEXUS")
        print("Opción 1. Préstamos.")
        print("Opción 2. Recolección.")
        print("Opción 3. Salir.")
        opcion = input("¿Cuál es su opción? ")

        if opcion == '1':
            codigo = input("Ingrese el código del libro para préstamo: ")
            dias = prestamo(codigo)
            if dias > 0:
                print(f"El libro puede ser prestado por {dias} días.")
                total_libros_prestados += 1
            else:
                print("Código inválido. No se puede prestar el libro.")

        elif opcion == '2':
            codigo = input("Ingrese el código del libro para recolección: ")
            valor = recoleccion(codigo)
            if valor > 0:
                print(f"El valor a pagar por este libro es ${valor}.")
                total_dinero_recolectado += valor
            else:
                print("Código inválido. No se puede registrar la recolección.")

        elif opcion == '3':
            print(f"\nAl final del día:")
            print(f"Total de libros prestados: {total_libros_prestados}")
            print(f"Total de dinero recolectado: ${total_dinero_recolectado}")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
