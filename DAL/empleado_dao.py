from DAL.conexion import crear_conexion, cerrar_conexion
from modelos.empleado import Empleado
from mysql.connector import Error

# Función para insertar un empleado
def insertar_empleado(empleado):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Empleado (nombre, rut, direccion, telefono, correo, fecha_inicio, rol_empleado_id, salario, contraseña, tipo_empleado_id, departamento_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            datos = (empleado.nombre, empleado.rut, empleado.direccion, empleado.telefono, empleado.correo, empleado.fecha_inicio, empleado.rol_empleado_id, empleado.salario, empleado.contraseña, empleado.tipo_empleado_id, empleado.departamento_id)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Empleado insertado correctamente")
        except Error as e:
            print(f"Error al insertar empleado: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

# Función para obtener todos los empleados
def obtener_empleados():
    conexion = crear_conexion()
    empleados = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Empleado")
            registros = cursor.fetchall()
            for registro in registros:
                empleados.append(Empleado(*registro))
            return empleados
        except Error as e:
            print(f"Error al obtener empleados: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return empleados

# Función para actualizar el salario de un empleado
def actualizar_empleado(id_empleado, nuevo_salario):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Empleado SET salario = %s WHERE id_empleado = %s"
            datos = (nuevo_salario, id_empleado)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Empleado actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar empleado: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

# Función para eliminar un empleado
def eliminar_empleado(id_empleado):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Empleado WHERE id_empleado = %s"
            cursor.execute(consulta, (id_empleado,))
            conexion.commit()
            print("Empleado eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar empleado: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)