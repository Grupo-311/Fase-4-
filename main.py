from cliente import registrar_cliente, mostrar_clientes

def main():
    # Registrar 10 clientes válidos
    registrar_cliente("Noemi", "noemi@correo.com", "3101234567")
    registrar_cliente("Oneida", "oneida@correo.com", "3112345678")
    registrar_cliente("Jesús", "jesus@correo.com", "3123456789")
    registrar_cliente("Sandra", "sandra@correo.com", "3134567890")
    registrar_cliente("Sneyder", "sneyder@correo.com", "3145678901")
    registrar_cliente("Kenner", "kenner@correo.com", "3156789012")
    registrar_cliente("Eliam", "eliam@correo.com", "3167890123")
    registrar_cliente("Zoe", "zoe@correo.com", "3178901234")
    registrar_cliente("Elisa", "elisa@correo.com", "3189012345")
    registrar_cliente("Carolina", "carolina@correo.com", "3190123456")

    # Registrar cliente inválido (se guarda en logs.txt)
    registrar_cliente("", "correo_invalido", "abc123")

    # Mostrar clientes registrados
    mostrar_clientes()

if __name__ == "__main__":
    main()
