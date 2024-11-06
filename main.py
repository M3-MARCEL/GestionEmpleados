from DAL.empleado_dao import insertar_empleado, obtener_empleados, actualizar_empleado, eliminar_empleado
from modelos.empleado import Empleado

# Insertar un nuevo empleado
nuevo_empleado = Empleado(
    id_empleado=None,  # Se generará automáticamente en la base de datos
    nombre="John Wick",
    rut="12345678-9",
    direccion="Racine 1634",
    telefono="123456789",
    correo="johnwick@gmail.com",
    fecha_inicio="2024-11-01",
    rol_empleado_id=1,
    salario=500000,
    contraseña="safe_password",
    tipo_empleado_id=1,
    departamento_id=1
)
insertar_empleado(nuevo_empleado)

# Obtener todos los empleados
empleados = obtener_empleados()
print("Lista de empleados:")
for empleado in empleados:
    print(empleado.__dict__)  # Imprime los atributos de cada empleado

# Actualizar el salario de un empleado
actualizar_empleado(id_empleado=1, nuevo_salario=600000)

# Eliminar un empleado
eliminar_empleado(id_empleado=1)