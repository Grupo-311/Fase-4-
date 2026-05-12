# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio, fecha):

        # Validación del cliente
        if cliente == "":
            raise ValueError("El nombre del cliente no puede estar vacío")

        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.estado = "Pendiente"

    # Confirmar reserva
    def confirmar(self):

        self.estado = "Confirmada"
        print("Reserva confirmada")

    # Cancelar reserva
    def cancelar(self):

        self.estado = "Cancelada"
        print("Reserva cancelada")

    # Mostrar información
    def mostrar_reserva(self):

        print("-------------------")
        print("Cliente:", self.cliente)
        print("Servicio:", self.servicio)
        print("Fecha:", self.fecha)
        print("Estado:", self.estado)


# Manejo de excepciones
try:

    # Crear reservas
    reserva1 = Reserva(
        "Katerin Gonzalez",
        "Reserva Sala VIP",
        "2026-05-20"
    )

    reserva2 = Reserva(
        "Carlos Perez",
        "Alquiler de VideoBeam",
        "2026-05-21"
    )

    reserva3 = Reserva(
        "Maria Lopez",
        "Asesoría Especializada",
        "2026-05-22"
    )

    # Confirmar reservas
    reserva1.confirmar()
    reserva2.confirmar()

    # Cancelar reserva
    reserva3.cancelar()

    # Mostrar información
    reserva1.mostrar_reserva()
    reserva2.mostrar_reserva()
    reserva3.mostrar_reserva()

except Exception as e:

    print("Error:", e)
    