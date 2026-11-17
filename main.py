# main.py
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada, Reserva
from excepciones import ClienteInvalidoError, ReservaInvalidaError
from logger import registrar_evento, registrar_error

def ejecutar_simulaciones():
    registrar_evento("=== INICIO DE LAS SIMULACIONES DE SOFTWARE FJ ===")
    print("--- INICIANDO SIMULACIONES DEL SISTEMA ---\n")
    
    # 1. Simulación 1: Registro válido de un cliente
    try:
        registrar_evento("Simulación 1: Creación de cliente válido.")
        cli1 = Cliente("1098", "Carlos Pérez", "carlos@mail.com", "3001234567")
        print("[ÉXITO] 1. Cliente creado:", cli1.obtener_detalle())
    except Exception as e:
        registrar_error("Error en Simulación 1", e)

    # 2. Simulación 2: Registro inválido de un cliente (Prueba try/except/else/finally)
    try:
        registrar_evento("Simulación 2: Creación de cliente con datos inválidos.")
        cli_malo = Cliente("1099", "Lu", "correo_mal", "123")
    except ValueError as ve:
        registrar_error("Validación fallida atrapada correctamente.", ve)
        print("[CONTROLADO] 2. Error de cliente detectado y manejado con éxito.")
    else:
        print("Esto no debería imprimirse si falla.")
    finally:
        registrar_evento("Finalizó el bloque de prueba del cliente inválido.")

    # 3. Simulación 3: Cálculo de costo de Reserva de Sala (Sobrecarga e IVA)
    try:
        registrar_evento("Simulación 3: Cálculo de costo de Reserva de Sala.")
        sala = ReservaSala("SALA-01", 50000.0, 10)
        costo = sala.calcular_costo(horas=3, descuento_porcentaje=10.0, incluye_impuesto=True)
        print(f"[ÉXITO] 3. Costo calculado para {sala.descripcion_servicio()}: ${costo}")
    except Exception as e:
        registrar_error("Error en Simulación 3", e)

    # 4. Simulación 4: Alquiler de equipo tecnológico
    try:
        registrar_evento("Simulación 4: Alquiler de equipo.")
        equipo = AlquilerEquipo("EQ-05", 30000.0, "Laptop Core i7")
        costo_eq = equipo.calcular_costo(dias=4, seguro_adicional=15000.0)
        print(f"[ÉXITO] 4. Costo equipo ({equipo.tipo_equipo}): ${costo_eq}")
    except Exception as e:
        registrar_error("Error en Simulación 4", e)

    # 5. Simulación 5: Asesoría especializada
    try:
        registrar_evento("Simulación 5: Asesoría especializada.")
        asesoria = AsesoriaEspecializada("ASES-02", 80000.0, "Desarrollo Python")
        costo_as = asesoria.calcular_costo(sesiones=2, tarifa_preferencial=True)
        print(f"[ÉXITO] 5. Costo asesoría: ${costo_as}")
    except Exception as e:
        registrar_error("Error en Simulación 5", e)

    # 6. Simulación 6: Creación y confirmación exitosa de una Reserva
    try:
        registrar_evento("Simulación 6: Creación de reserva exitosa.")
        reserva1 = Reserva("RES-001", cli1, sala, 3)
        reserva1.confirmar_reserva(horas=3, descuento_porcentaje=5.0)
        print(f"[ÉXITO] 6. {reserva1.obtener_resumen()}")
    except Exception as e:
        registrar_error("Error en Simulación 6", e)

    # 7. Simulación 7: Cancelación de una reserva
    try:
        registrar_evento("Simulación 7: Cancelación de reserva.")
        reserva1.cancelar_reserva()
        print(f"[ÉXITO] 7. Reserva cancelada exitosamente. Estado actual: {reserva1.estado}")
    except Exception as e:
        registrar_error("Error en Simulación 7", e)

    # 8. Simulación 8: Error controlado por parámetros de servicio incorrectos
    try:
        registrar_evento("Simulación 8: Prueba de parámetros de costo inválidos.")
        # Intentamos calcular con un tipo de dato erróneo o forzando un fallo
        sala.calcular_costo(horas="tres_horas") # Esto generará un TypeError
    except TypeError as te:
        registrar_error("Error de tipos controlado en cálculo de costos.", te)
        print("[CONTROLADO] 8. Excepción por tipo de dato incorrecto atrapada correctamente.")

    # 9. Simulación 9: Intento de crear un segundo cliente con correo inválido
    try:
        registrar_evento("Simulación 9: Segundo intento de cliente inválido.")
        cli_error = Cliente("1100", "Ana Gómez", "correo_sin_arroba", "3111234567")
    except ValueError as ve:
        registrar_error("Validación de correo atrapada.", ve)
        print("[CONTROLADO] 9. Validación estricta de correo electrónico funcionando.")

    # 10. Simulación 10: Reserva con servicio de asesoría y encadenamiento de excepciones
    try:
        registrar_evento("Simulación 10: Reserva avanzada con asesoría.")
        reserva2 = Reserva("RES-002", cli1, asesoria, 2)
        reserva2.confirmar_reserva(sesiones=2, tarifa_preferencial=False)
        print(f"[ÉXITO] 10. {reserva2.obtener_resumen()}")
    except Exception as e:
        registrar_error("Error crítico en reserva avanzada", e)

    registrar_evento("=== FIN DE LAS SIMULACIONES DE SOFTWARE FJ ===")
    print("\n--- ¡TODAS LAS SIMULACIONES FINALIZARON CON ÉXITO! ---")
    print("Revisa el archivo 'sistema_software_fj.log' generado en tu carpeta.")

if __name__ == "__main__":
    ejecutar_simulaciones()