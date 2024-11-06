class Departamento:
    def __init__(self, id_departamento, nombre, telefono, gerente=None):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.telefono = telefono
        self.gerente = gerente
        self.empleados = []

    def asignar_gerente(self, empleado):
        self.gerente = empleado

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)