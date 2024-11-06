from DAL.conexion import crear_conexion, cerrar_conexion
from modelos.departamento import Departamento
from mysql.connector import Error

def insertar_departamento(departamento):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
            INSERT INTO Departamento (nombre, telefono, gerente_id)
            VALUES (%s, %s, %s)
            """
            datos = (departamento.nombre, departamento.telefono, departamento.gerente_id)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Departamento insertado correctamente")
        except Error as e:
            print(f"Error al insertar departamento: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def obtener_departamentos():
    conexion = crear_conexion()
    departamentos = []
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Departamento")
            registros = cursor.fetchall()
            for registro in registros:
                departamentos.append(Departamento(*registro))
            return departamentos
        except Error as e:
            print(f"Error al obtener departamentos: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
    return departamentos

def actualizar_departamento(id_departamento, nuevo_telefono):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Departamento SET telefono = %s WHERE id_departamento = %s"
            datos = (nuevo_telefono, id_departamento)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Departamento actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar departamento: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

def eliminar_departamento(id_departamento):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Departamento WHERE id_departamento = %s"
            cursor.execute(consulta, (id_departamento,))
            conexion.commit()
            print("Departamento eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar departamento: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)