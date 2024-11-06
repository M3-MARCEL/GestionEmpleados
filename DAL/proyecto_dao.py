from DAL.conexion import crear_conexion, cerrar_conexion
from modelos.proyecto import Proyecto
from mysql.connector import Error

def insertar_proyecto(proyecto):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Proyecto (nombre, descripcion, fecha_inicio, fecha_fin)
            VALUES (%s, %s, %s, %s)
            """
            datos = (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.fecha_fin)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Proyecto insertado correctamente")
        except Error as e:
            print(f"Error al insertar proyecto: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_proyectos():
    conexion = crear_conexion()
    proyectos = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Proyecto")
            registros = cursor.fetchall()
            for registro in registros:
                proyectos.append(Proyecto(*registro))
            return proyectos
        except Error as e:
            print(f"Error al obtener proyectos: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return proyectos

def actualizar_proyecto(id_proyecto, nueva_descripcion):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Proyecto SET descripcion = %s WHERE id_proyecto = %s"
            datos = (nueva_descripcion, id_proyecto)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Proyecto actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar proyecto: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_proyecto(id_proyecto):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Proyecto WHERE id_proyecto = %s"
            cursor.execute(consulta, (id_proyecto,))
            conexion.commit()
            print("Proyecto eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar proyecto: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)