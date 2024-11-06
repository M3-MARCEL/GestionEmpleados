from DAL.conexion import crear_conexion, cerrar_conexion
from modelos.informe import Informe
from mysql.connector import Error

def insertar_informe(informe):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Informe (nombre_informe, fecha_creacion, creador_id, ubicacion)
            VALUES (%s, %s, %s, %s)
            """
            datos = (informe.nombre_informe, informe.fecha_creacion, informe.creador_id, informe.ubicacion)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Informe insertado correctamente")
        except Error as e:
            print(f"Error al insertar informe: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_informes():
    conexion = crear_conexion()
    informes = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Informe")
            registros = cursor.fetchall()
            for registro in registros:
                informes.append(Informe(*registro))
            return informes
        except Error as e:
            print(f"Error al obtener informes: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return informes

def actualizar_informe(id_informe, nueva_ubicacion):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Informe SET ubicacion = %s WHERE id_informe = %s"
            datos = (nueva_ubicacion, id_informe)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Informe actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar informe: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_informe(id_informe):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Informe WHERE id_informe = %s"
            cursor.execute(consulta, (id_informe,))
            conexion.commit()
            print("Informe eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar informe: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)