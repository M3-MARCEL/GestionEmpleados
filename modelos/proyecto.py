class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.empleados = []

    def validar_fechas(self):
        return self.fecha_inicio <= self.fecha_fin

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)