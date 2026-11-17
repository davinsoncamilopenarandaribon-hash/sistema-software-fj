# excepciones.py

class SoftwareFJExcepcion(Exception):
    """Clase base para todas las excepciones personalizadas de Software FJ."""
    pass

class ClienteInvalidoError(SoftwareFJExcepcion):
    """Se lanza cuando los datos del cliente no cumplen con las validaciones."""
    pass

class ServicioNoDisponibleError(SoftwareFJExcepcion):
    """Se lanza cuando se intenta solicitar un servicio inactivo o inexistente."""
    pass

class ReservaInvalidaError(SoftwareFJExcepcion):
    """Se lanza cuando hay errores en los parámetros, fechas o estados de una reserva."""
    pass

class OperacionNoPermitidaError(SoftwareFJExcepcion):
    """Se lanza ante operaciones lógicas prohibidas dentro del sistema."""
    pass