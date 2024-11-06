import tkinter as tk
from tkinter import messagebox
from DAL.empleado_dao import insertar_empleado, obtener_empleados, actualizar_empleado, eliminar_empleado
from modelos.empleado import Empleado

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Empleados")
ventana.geometry("600x400")

# Etiquetas y campos de entrada para la información del empleado
tk.Label(ventana, text="Nombre").grid(row=0, column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

tk.Label(ventana, text="RUT").grid(row=1, column=0)
entrada_rut = tk.Entry(ventana)
entrada_rut.grid(row=1, column=1)

tk.Label(ventana, text="Dirección").grid(row=2, column=0)
entrada_direccion = tk.Entry(ventana)
entrada_direccion.grid(row=2, column=1)

tk.Label(ventana, text="Teléfono").grid(row=3, column=0)
entrada_telefono = tk.Entry(ventana)
entrada_telefono.grid(row=3, column=1)

tk.Label(ventana, text="Correo").grid(row=4, column=0)
entrada_correo = tk.Entry(ventana)
entrada_correo.grid(row=4, column=1)

tk.Label(ventana, text="Salario").grid(row=5, column=0)
entrada_salario = tk.Entry(ventana)
entrada_salario.grid(row=5, column=1)

tk.Label(ventana, text="Rol ID").grid(row=6, column=0)
entrada_rol = tk.Entry(ventana)
entrada_rol.grid(row=6, column=1)

tk.Label(ventana, text="Tipo Empleado ID").grid(row=7, column=0)
entrada_tipo_empleado = tk.Entry(ventana)
entrada_tipo_empleado.grid(row=7, column=1)

tk.Label(ventana, text="Departamento ID").grid(row=8, column=0)
entrada_departamento = tk.Entry(ventana)
entrada_departamento.grid(row=8, column=1)

# Campo de entrada para ID de empleado (usado en actualizar/eliminar)
tk.Label(ventana, text="ID Empleado").grid(row=9, column=0)
entrada_id_empleado = tk.Entry(ventana)
entrada_id_empleado.grid(row=9, column=1)

# Función para agregar un empleado
def agregar_empleado():
    try:
        nombre = entrada_nombre.get()
        rut = entrada_rut.get()
        direccion = entrada_direccion.get()
        telefono = entrada_telefono.get()
        correo = entrada_correo.get()
        salario = float(entrada_salario.get())
        rol_id = int(entrada_rol.get())
        tipo_empleado_id = int(entrada_tipo_empleado.get())
        departamento_id = int(entrada_departamento.get())
        
        nuevo_empleado = Empleado(None, nombre, rut, direccion, telefono, correo, "2024-11-01", rol_id, salario, "contraseña_segura", tipo_empleado_id, departamento_id)
        insertar_empleado(nuevo_empleado)
        messagebox.showinfo("Inserción", "Empleado insertado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar empleado: {e}")

# Función para ver empleados
def ver_empleados():
    empleados = obtener_empleados()
    ventana_empleados = tk.Toplevel(ventana)
    ventana_empleados.title("Lista de Empleados")

    for i, empleado in enumerate(empleados):
        tk.Label(ventana_empleados, text=f"{empleado.id_empleado} - {empleado.nombre} - {empleado.rut}").grid(row=i, column=0)

# Función para actualizar el salario de un empleado
def actualizar_salario():
    try:
        id_empleado = int(entrada_id_empleado.get())
        nuevo_salario = float(entrada_salario.get())
        actualizar_empleado(id_empleado, nuevo_salario)
        messagebox.showinfo("Actualización", "Salario actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar salario: {e}")

# Función para eliminar un empleado
def eliminar_empleado_ui():
    try:
        id_empleado = int(entrada_id_empleado.get())
        eliminar_empleado(id_empleado)
        messagebox.showinfo("Eliminación", "Empleado eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar empleado: {e}")

# Botones para las operaciones CRUD
tk.Button(ventana, text="Agregar Empleado", command=agregar_empleado).grid(row=10, column=0)
tk.Button(ventana, text="Ver Empleados", command=ver_empleados).grid(row=10, column=1)
tk.Button(ventana, text="Actualizar Salario", command=actualizar_salario).grid(row=11, column=0)
tk.Button(ventana, text="Eliminar Empleado", command=eliminar_empleado_ui).grid(row=11, column=1)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()