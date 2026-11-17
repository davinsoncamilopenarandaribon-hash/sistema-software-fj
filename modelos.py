from abc import ABC, abstractmethod
from datetime import datetime

# 1. CLASE ABSTRACTA BASE (Entidad general del sistema)
class EntidadBase(ABC):
    def __init__(self, identificador: str):
        self._identificador = identificador

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def obtener_detalle(self) -> str:
        pass


# 2. CLASE CLIENTE (Con encapsulación y validaciones)
class Cliente(EntidadBase):
    def __init__(self, identificador: str, nombre: str, correo: str, telefono: str):
        super().__init__(identificador)
        self.nombre = nombre        # Usa el setter para validar
        self.correo = correo        # Usa el setter para validar
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre del cliente no es válido (mínimo 3 caracteres).")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            raise ValueError("El formato del correo electrónico no es válido.")
        self._correo = valor.strip()

    def obtener_detalle(self) -> str:
        return f"Cliente: {self._nombre} | Correo: {self._correo} | ID: {self.identificador}"


# 3. CLASE ABSTRACTA SERVICIO (Aplica polimorfismo)
class Servicio(ABC):
    def __init__(self, codigo: str, nombre_servicio: str, costo_base: float):
        self.codigo = codigo
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs) -> float:
        """Método abstracto para calcular el costo con posibles sobrecargas."""
        pass

    @abstractmethod
    def descripcion_servicio(self) -> str:
        pass


# 4. TRES SERVICIOS ESPECIALIZADOS (Herencia y Sobrecarga)
class ReservaSala(Servicio):
    def __init__(self, codigo: str, costo_base: float, capacidad: int):
        super().__init__(codigo, "Reserva de Sala", costo_base)
        self.capacidad = capacidad

    # Sobrecarga simulada mediante parámetros opcionales (impuesto y descuento)
    def calcular_costo(self, horas: int = 1, descuento_porcentaje: float = 0.0, incluye_impuesto: bool = True) -> float:
        subtotal = self.costo_base * horas
        if descuento_porcentaje > 0:
            subtotal -= subtotal * (descuento_porcentaje / 100)
        if incluye_impuesto:
            subtotal *= 1.19  # IVA del 19%
        return round(subtotal, 2)

    def descripcion_servicio(self) -> str:
        return f"Sala de reuniones (Capacidad: {self.capacidad} personas)"


class AlquilerEquipo(Servicio):
    def __init__(self, codigo: str, costo_base: float, tipo_equipo: str):
        super().__init__(codigo, "Alquiler de Equipo", costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias: int = 1, seguro_adicional: float = 0.0) -> float:
        total = (self.costo_base * dias) + seguro_adicional
        return round(total, 2)

    def descripcion_servicio(self) -> str:
        return f"Alquiler de equipo tecnológico: {self.tipo_equipo}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, codigo: str, costo_base: float, area: str):
        super().__init__(codigo, "Asesoría Especializada", costo_base)
        self.area = area

    def calcular_costo(self, sesiones: int = 1, tarifa_preferencial: bool = False) -> float:
        factor = 0.85 if tarifa_preferencial else 1.0
        total = self.costo_base * sesiones * factor
        return round(total, 2)

    def descripcion_servicio(self) -> str:
        return f"Asesoría técnica en área: {self.area}"


# 5. CLASE RESERVA (Integra cliente, servicio, duración y estado)
class Reserva:
    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion_unidades: int):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_unidades = duracion_unidades
        self.estado = "Pendiente"  # Estados: Pendiente, Confirmada, Cancelada
        self.costo_total = 0.0

    def confirmar_reserva(self, **kwargs):
        """Confirma la reserva calculando su costo final."""
        try:
            self.costo_total = self.servicio.calcular_costo(**kwargs)
            self.estado = "Confirmada"
            return True
        except Exception as e:
            self.estado = "Error en Confirmación"
            raise RuntimeError(f"No se pudo confirmar la reserva {self.id_reserva}") from e

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        self.costo_total = 0.0

    def obtener_resumen(self) -> str:
        return (f"Reserva [{self.id_reserva}] - Estado: {self.estado}\n"
                f"   -> {self.cliente.obtener_detalle()}\n"
                f"   -> Servicio: {self.servicio.nombre_servicio} ({self.servicio.descripcion_servicio()})\n"
                f"   -> Costo Total: ${self.costo_total}")