class RegistroTiempo:
    def __init__(self, id_registro_tiempo, fecha, horas, tareas, observacion, empleado, proyecto):
        self.id_registro_tiempo = id_registro_tiempo
        self.fecha = fecha
        self.horas = horas
        self.tareas = tareas
        self.observacion = observacion
        self.empleado = empleado
        self.proyecto = proyecto

    def validar_horas(self):
        return 0 < self.horas <= 24