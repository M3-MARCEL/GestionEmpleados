from DAL.conexion import crear_conexion, cerrar_conexion
from modelos.registrotiempo import RegistroTiempo
from mysql.connector import Error

def insertar_registro_tiempo(registro):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO RegistroTiempo (fecha, horas, tareas, observacion, empleado_id, proyecto_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            datos = (registro.fecha, registro.horas, registro.tareas, registro.observacion, registro.empleado_id, registro.proyecto_id)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Registro de tiempo insertado correctamente")
        except Error as e:
            print(f"Error al insertar registro de tiempo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_registros_tiempo():
    conexion = crear_conexion()
    registros_tiempo = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM RegistroTiempo")
            registros = cursor.fetchall()
            for registro in registros:
                registros_tiempo.append(RegistroTiempo(*registro))
            return registros_tiempo
        except Error as e:
            print(f"Error al obtener registros de tiempo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return registros_tiempo

def actualizar_registro_tiempo(id_registro, nuevas_horas):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE RegistroTiempo SET horas = %s WHERE id_registro_tiempo = %s"
            datos = (nuevas_horas, id_registro)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Registro de tiempo actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar registro de tiempo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_registro_tiempo(id_registro):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM RegistroTiempo WHERE id_registro_tiempo = %s"
            cursor.execute(consulta, (id_registro,))
            conexion.commit()
            print("Registro de tiempo eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar registro de tiempo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)