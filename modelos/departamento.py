from modelos.empleado import Empleado

class Departamento(Empleado):
    def __init__(self, nombre, gerente_id, empleados=None):
        super().__init__(id_empleado=gerente_id)  # Inicializa el gerente desde Empleado
        self.nombre = nombre
        self.empleados = empleados if empleados is not None else []  # Lista de empleados

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def quitar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)

    # Método polimórfico
    def mostrar_info(self):
        return f"Departamento: {self.nombre}, Gerente: {self.nombre}"