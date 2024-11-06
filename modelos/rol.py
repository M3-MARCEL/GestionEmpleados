class Rol:
    def __init__(self, id_rol, nombre, permisos=None):
        self.id_rol = id_rol
        self.nombre = nombre
        self.permisos = permisos if permisos else []

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)