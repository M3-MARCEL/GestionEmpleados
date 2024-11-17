import hashlib

class Empleado:
    def __init__(self, id_empleado=None, nombre="", rut="", direccion="", telefono="", correo="", fecha_inicio="", rol_empleado_id=None, salario=0.0, contraseña="", tipo_empleado_id=None, departamento_id=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.rol_empleado_id = rol_empleado_id
        self.salario = salario
        self.contraseña = self.encriptar_contraseña(contraseña)
        self.tipo_empleado_id = tipo_empleado_id
        self.departamento_id = departamento_id

    def validar_contraseña(self, contraseña):
        """Compara la contraseña cifrada almacenada con la ingresada por el usuario."""
        return self.contraseña == self.encriptar_contraseña(contraseña)

    def encriptar_contraseña(self, contraseña):
        """Encripta la contraseña para almacenarla de manera segura."""
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def asignar_departamento(self, departamento):
        """Asigna un departamento al empleado."""
        if departamento and departamento.id_departamento:
            self.departamento_id = departamento.id_departamento