class ProyectoEmpleado:
    def __init__(self, id_proyecto_empleado, proyecto, empleado):
        self.id_proyecto_empleado = id_proyecto_empleado
        self.proyecto = proyecto
        self.empleado = empleado

    def asignar_empleado_proyecto(self):
        if self.empleado not in self.proyecto.empleados:
            self.proyecto.agregar_empleado(self.empleado)