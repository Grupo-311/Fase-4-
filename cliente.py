"""
Gestor de Reservas de Alquiler de Equipos para la empresa Software FJ.
Este sistema permite a los clientes apartar computadores, cámaras y proyectores.
Todo se gestionará mediante objetos y listas, sin base de datos, garantizando
robustez, modularidad y aplicación completa de los principios de POO y manejo
avanzado de excepciones.
"""

import logging

# Configuración de logs centralizada
logging.basicConfig(filename="logs.txt", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class Cliente:
    """
    Clase Cliente: representa a un usuario del sistema.
    Aplica encapsulación y validaciones de datos personales.
    """

    def __init__(self, nombre: str, correo: str, telefono: str):
        try:
            if not nombre or len(nombre.strip()) == 0:
                raise ValueError("El nombre no puede estar vacío.")
            if "@" not in correo or "." not in correo:
                raise ValueError("Correo inválido. Debe contener '@' y '.'")
            if not telefono.isdigit():
                raise ValueError("Teléfono inválido. Debe contener solo números.")

            self._nombre = nombre
            self._correo = correo
            self._telefono = telefono

        except ValueError as e:
            logging.error(f"Error al crear cliente: {e}")
            raise

    # Getters y setters (encapsulación)
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre: str):
        if not nuevo_nombre or len(nuevo_nombre.strip()) == 0:
            logging.error("Intento de asignar nombre vacío.")
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    def get_correo(self):
        return self._correo

    def set_correo(self, nuevo_correo: str):
        if "@" not in nuevo_correo or "." not in nuevo_correo:
            logging.error("Intento de asignar correo inválido.")
            raise ValueError("Correo inválido.")
        self._correo = nuevo_correo

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, nuevo_telefono: str):
        if not nuevo_telefono.isdigit():
            logging.error("Intento de asignar teléfono inválido.")
            raise ValueError("Teléfono inválido.")
        self._telefono = nuevo_telefono

    def __str__(self):
        return f"Cliente: {self._nombre}, Correo: {self._correo}, Teléfono: {self._telefono}"


# Lista global de clientes
lista_clientes = []

def registrar_cliente(nombre, correo, telefono):
    try:
        cliente = Cliente(nombre, correo, telefono)
        lista_clientes.append(cliente)
        return cliente
    except Exception as e:
        print("Error al registrar cliente:", e)
        return None

def mostrar_clientes():
    if len(lista_clientes) == 0:
        print("No hay clientes registrados.")
    else:
        for c in lista_clientes:
            print(c)
