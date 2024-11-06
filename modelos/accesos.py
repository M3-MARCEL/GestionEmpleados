class Accesos:
    def __init__(self, id_acceso, empleado, modulo):
        self.id_acceso = id_acceso
        self.empleado = empleado
        self.modulo = modulo

    def validar_acceso(self, modulo):
        return modulo in self.empleado.permisos