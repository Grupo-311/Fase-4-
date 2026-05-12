"""
Gestor de Reservas de Alquiler de Equipos para la empresa Software FJ.
Este sistema permite a los clientes apartar computadores, cámaras y proyectores.
Todo se gestionará mediante objetos y listas, sin base de datos, garantizando
robustez, modularidad y aplicación completa de los principios de POO y manejo
avanzado de excepciones.
"""

import logging
from abc import ABC, abstractmethod

# Configuración de logs centralizada
logging.basicConfig(filename="logs.txt", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s", encoding='utf-8')

class SistemaFJError(Exception):
    pass

class DatosInvalidosError(SistemaFJError):
    pass

class ServicioNoDisponibleError(SistemaFJError):
    pass

class ReservaError(SistemaFJError):
    pass

# ==========================================
# CLASES ABSTRACTAS Y HERENCIA
# ==========================================
class EntidadGeneral (ABC):
    def __init__ (self, id_entidad):
        self._id_entidad= id_entidad
        
    @abstractmethod
    def mostrar_info(self):
        pass
    
class Servicio (EntidadGeneral):
    def __init__(self, id_entidad, nombre, tarifa_base):
        super().__init__(id_entidad)
        self.nombre=nombre
        self.tarifa_base=tarifa_base
        self.disponible= True
        
    @abstractmethod
    def calcular_costo(self, dias, descuento=0.0, impuesto=0.19):
        pass
    
    @abstractmethod
    def describir(self):
        pass
    
    def validar_parametros(self):
        if self.tarifa_base <=0:
            raise DatosInvalidosError( f'La tarifa base de {self.nombre} debe ser mayor a 0.')

# ==========================================
# POLIMORFISMO Y CLASES DERIVADAS
# ==========================================        
class Camara (Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, resolucion):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.resolucion=resolucion
        
    def calcular_costo(self, dias, descuento=0, impuesto=0.19):
        subtotal= self.tarifa_base*dias
        return subtotal-(subtotal*descuento)+(subtotal*impuesto)
    
    def describir(self):
        return f'Cámara: {self.nombre} (Resolución: {self.resolucion})'
    
    def mostrar_info(self):
        return self.describir()
    
class Equipos(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, potencia):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.potencia=potencia  
        
    def calcular_costo(self, dias, descuento=0, impuesto=0.19, seguro=50000):
        subtotal= (self.tarifa_base*dias)+ seguro
        return subtotal-(subtotal*descuento)+(subtotal*impuesto)
    
    def describir(self):
        return f'Equipo de sonido: {self.nombre} (Potencia: {self.potencia}W)'
    
    def mostrar_info(self):
        return self.describir()
    
class Proyector(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, lumenes):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.lumenes= lumenes
        
    def calcular_costo(self, dias, descuento=0, impuesto=0.19):
        subtotal= self.tarifa_base*dias        
        return subtotal-(subtotal*descuento)+(subtotal*impuesto)
    
    def describir(self):
        return f'Proyector: {self.nombre} (Lumenes: {self.lumenes})'
    
    def mostrar_info(self):
        return self.describir()
    
class Asesoria(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, especialidad):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.especialidad= especialidad
        
    def calcular_costo(self, descuento=0, impuesto=0.19):
        return self.tarifa_base -(self.tarifa_base*descuento)+ (self.tarifa_base*impuesto)
    
    def describir(self):
        return f'Especialidad: {self.especialidad}'
    
    def mostrar_info(self):
        return self.describir()
    
class Salas(Servicio):
    def __init__(self, id_entidad, nombre, tarifa_base, capacidad):
        super().__init__(id_entidad, nombre, tarifa_base)
        self.capacidad=capacidad
        
    def calcular_costo(self, dias, descuento=0, impuesto=0.19):
        subtotal= self.tarifa_base*dias
        return subtotal-(subtotal*descuento)+ (subtotal*impuesto)
    
    def describir(self):
        return f'Sala de reuniones {self.nombre} (Capacidad: {self.capacidad})'
    
    def mostrar_info(self):
        return self.describir()
          
            
# ==========================================
# ENCAPSULACIÓN ESTRICTA
# ==========================================
    
class Cliente(EntidadGeneral):
    #Clase Cliente: representa a un usuario del sistema.

    def __init__(self, id_entidad, nombre: str, documento, correo: str, telefono: str):
        super().__init__(id_entidad)
        self._nombre = nombre
        self.documento= documento
        self._correo = correo
        self._telefono = telefono
        try:
            if not nombre or len(nombre.strip()) == 0:
                raise ValueError("El nombre no puede estar vacío.")
            if "@" not in correo or "." not in correo:
                raise ValueError("Correo inválido. Debe contener '@' y '.'")
            if not telefono.isdigit():
                raise ValueError("Teléfono inválido. Debe contener solo números.")

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

    def mostrar_info(self):
            return self.__str__() 
# Lista global de clientes
lista_clientes = []

class Reserva:
    def __init__(self, cliente, servicio, dias):
        self.cliente= cliente
        self.servicio=servicio
        self.dias=dias
        
    def procesar(self):
        try:
            #validaciones previas
            self.servicio.validar_parametros()
            if not self.servicio.disponible:
                raise ServicioNoDisponibleError (f"El sercicio '{self.servicio.nombre}'ya está ocupado.")
            if self.dias <=0:
                raise DatosInvalidosError ('La duración de la reserva debe ser de mínimo 1 día.')
            #confirmación
            self.servicio.disponible =False
            self.estado='Confirmada'
            costo_total= self.servicio.calcular_costo(self.dias)
        except (DatosInvalidosError, ServicioNoDisponibleError) as e:
            self.estado= "Fallida"
            logging.error(f'Falló reserva de {self.cliente.get_nombre()}: {str(e)}')
            raise ReservaError ('El proceso de reserva ha fallado por reglas de negocio') from e
        else:
            logging.info (f'Reserva confirmada: {self.cliente.get_nombre()} reservó {self.servicio.nombre} por {self.dias} días. Total: ${costo_total:,.2f}')
            print (f'Reserva exitosa para {self.cliente.get_nombre()}. Total a pagar: ${costo_total:,.2f}')
            return costo_total
    
        finally:
            logging.info (f'Intento de transacción finalizado. Estado de la reserva: {self.estado}')
            
    def cancelar (self):
        if self.estado== 'Confirmada':
            self.servicio.disponible= True
            self.estado= 'Cancelada'
            logging.info(f'Reserva cancelada. El servicio {self.servicio.nombre} vuelve a estar disponible')
            print ('Reserva cancelada exitosamente.')
        else: 
            print ('La reserva no está confirmada, no hay lugar a cancelación')
    
    
def registrar_cliente(id_entidad, nombre, documento, correo, telefono):
    try:
        cliente = Cliente(id_entidad, nombre, documento, correo, telefono)
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
            
            
 #===============================
#  SIMULACIÓN DE 10 OPERACIONES 
# ===============================

def simular_10_operaciones():
    print("\n" + "="*50)
    print("INICIANDO SIMULACIÓN SISTEMA FJ (10 OPERACIONES)")
    print("="*50 + "\n")
    
    # ---------------------------------------------------------
    # OPERACIONES 1 y 2: Creación exitosa de servicios
    # ---------------------------------------------------------
    print(">> OP 1 y 2: Creación de servicios válidos")
    sala_conferencias = Salas("S01", "Sala Magna", 150000, 50)
    asesoria_legal = Asesoria("A01", "Asesoría Legal Tech", 200000, "Propiedad Intelectual")
    print(sala_conferencias.mostrar_info())
    print(asesoria_legal.mostrar_info())
    
    # ---------------------------------------------------------
    # OPERACIÓN 3: Creación de servicio con parámetros inválidos
    # ---------------------------------------------------------
    print("\n>> OP 3: Intento de creación de servicio con tarifa negativa")
    try:
        proyector_malo = Proyector("P01", "Proyector Dañado", -50000, 3000)
        proyector_malo.validar_parametros()
    except DatosInvalidosError as e:
        print(f"Error Capturado Exitosamente: {e}")

    # ---------------------------------------------------------
    # OPERACIONES 4 y 5: Registro de clientes válidos
    # ---------------------------------------------------------
    print("\n>> OP 4 y 5: Creación de clientes válidos")
    cliente_1 = Cliente("C01", "Ana Gómez", "10203040", "ana@correo.com", "3102349568")
    cliente_2 = Cliente("C02", "Luis Pérez", "50607080", "luis@correo.com", "3230980099")
    print(cliente_2.mostrar_info())

    # ---------------------------------------------------------
    # OPERACIÓN 6: Registro de cliente inválido (Validación de tu compañera)
    # ---------------------------------------------------------
    print("\n>> OP 6: Creación de cliente inválido (Falta '@' en correo y letras en teléfono)")
    try:
        cliente_malo = Cliente("C03", "Carlos", "112233", "carlos_sin_arroba.com", "ABC")
    except ValueError as e:
        print(f"Error Capturado Exitosamente: {e}")

    # ---------------------------------------------------------
    # OPERACIÓN 7: Reserva Exitosa
    # ---------------------------------------------------------
    print("\n>> OP 7: Reserva Exitosa de Sala")
    reserva_1 = Reserva(cliente_1, sala_conferencias, 3)
    reserva_1.procesar()

    # ---------------------------------------------------------
    # OPERACIÓN 8: Reserva Fallida (Servicio no disponible)
    # ---------------------------------------------------------
    print("\n>> OP 8: Intento de reservar una Sala que ya está ocupada")
    try:
        reserva_2 = Reserva(cliente_2, sala_conferencias, 2)
        reserva_2.procesar()
    except ReservaError as e:
        print(f"Error Capturado Exitosamente (Encadenamiento): {e}")
        print(f"Causa original: {e.__cause__}")

    # ---------------------------------------------------------
    # OPERACIÓN 9: Reserva Fallida (Días inválidos / negativos)
    # ---------------------------------------------------------
    print("\n>> OP 9: Intento de reserva con días negativos")
    try:
        reserva_3 = Reserva(cliente_1, asesoria_legal, -5)
        reserva_3.procesar()
    except ReservaError as e:
        print(f"Error Capturado Exitosamente (Encadenamiento): {e}")
        print(f"Causa original: {e.__cause__}")

    # ---------------------------------------------------------
    # OPERACIÓN 10: Cancelación y reasignación exitosa
    # ---------------------------------------------------------
    print("\n>> OP 10: Cancelación de reserva anterior y nueva reserva exitosa")
    reserva_1.cancelar()  # Libera la sala
    reserva_4 = Reserva(cliente_2, sala_conferencias, 1) # Ahora Luis sí puede reservarla
    reserva_4.procesar()

# Punto de entrada principal (Buenas prácticas en Python)
if __name__ == "__main__":
    simular_10_operaciones()
    print("\nSimulación finalizada. Revisa el archivo 'logs.txt' para ver la auditoría de excepciones.")