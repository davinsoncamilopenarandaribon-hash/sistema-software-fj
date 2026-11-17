# logger.py
import logging

# Configuración básica del sistema de logging
logging.basicConfig(
    filename='sistema_software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    encoding='utf-8'
)

def registrar_evento(mensaje: str):
    """Registra un evento exitoso o informativo en el log."""
    logging.info(mensaje)

def registrar_error(mensaje: str, excepcion: Exception = None):
    """Registra un error detallado en el log, capturando opcionalmente la excepción."""
    if excepcion:
        logging.error(f"{mensaje} | Detalle técnico: {type(excepcion).__name__}: {excepcion}")
    else:
        logging.error(mensaje)