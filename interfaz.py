import tkinter as tk
from tkinter import messagebox, ttk
from DAL.empleado_dao import insertar_empleado, obtener_empleados, actualizar_empleado, eliminar_empleado
from modelos.empleado import Empleado

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Empleados")
ventana.geometry("600x400")

# Función para cargar empleados en el Combobox
def cargar_empleados():
    empleados = obtener_empleados()
    return [f"{empleado.id_empleado} - {empleado.nombre}" for empleado in empleados]

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

# Uso de Combobox para Rol, Tipo de Empleado, y Departamento
tk.Label(ventana, text="Rol").grid(row=6, column=0)
rol_combobox = ttk.Combobox(ventana, values=["Gerente", "Empleado", "Asistente"])
rol_combobox.grid(row=6, column=1)

tk.Label(ventana, text="Tipo de Empleado").grid(row=7, column=0)
tipo_combobox = ttk.Combobox(ventana, values=["Contratado", "Permanente", "Temporal"])
tipo_combobox.grid(row=7, column=1)

tk.Label(ventana, text="Departamento").grid(row=8, column=0)
departamento_combobox = ttk.Combobox(ventana, values=["Recursos Humanos", "Ventas", "Desarrollo"])
departamento_combobox.grid(row=8, column=1)

# ComboBox para seleccionar empleado a actualizar o eliminar
tk.Label(ventana, text="Seleccione Empleado").grid(row=9, column=0)
empleado_combobox = ttk.Combobox(ventana, values=cargar_empleados())
empleado_combobox.grid(row=9, column=1)

# Función para extraer el ID del empleado seleccionado en el Combobox
def obtener_id_empleado_seleccionado():
    seleccionado = empleado_combobox.get()
    return int(seleccionado.split(" - ")[0]) if seleccionado else None

# Función para agregar un empleado
def agregar_empleado():
    try:
        nombre = entrada_nombre.get()
        rut = entrada_rut.get()
        direccion = entrada_direccion.get()
        telefono = entrada_telefono.get()
        correo = entrada_correo.get()
        salario = float(entrada_salario.get())
        rol_id = rol_combobox.current() + 1  # ID basado en el índice del ComboBox
        tipo_empleado_id = tipo_combobox.current() + 1
        departamento_id = departamento_combobox.current() + 1

        nuevo_empleado = Empleado(None, nombre, rut, direccion, telefono, correo, "2024-11-01", rol_id, salario, "contraseña_segura", tipo_empleado_id, departamento_id)
        insertar_empleado(nuevo_empleado)
        messagebox.showinfo("Inserción", "Empleado insertado correctamente")
        empleado_combobox['values'] = cargar_empleados()  # Actualizar ComboBox con nuevo empleado
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar empleado: {e}")

# Función para ver empleados
def ver_empleados():
    empleados = obtener_empleados()
    ventana_empleados = tk.Toplevel(ventana)
    ventana_empleados.title("Lista de Empleados")

    if not empleados:
        tk.Label(ventana_empleados, text="NO HAY DATOS").pack()
    else:
        for i, empleado in enumerate(empleados):
            tk.Label(ventana_empleados, text=f"{empleado.id_empleado} - {empleado.nombre} - {empleado.rut}").grid(row=i, column=0)

# Función para actualizar el salario de un empleado
def actualizar_salario():
    try:
        id_empleado = obtener_id_empleado_seleccionado()
        if not id_empleado:
            messagebox.showwarning("Advertencia", "Seleccione un empleado")
            return
        nuevo_salario = float(entrada_salario.get())
        if actualizar_empleado(id_empleado, nuevo_salario):
            messagebox.showinfo("Actualización", "Salario actualizado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el salario: ID no encontrado o error en la base de datos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar salario: {e}")

# Función para eliminar un empleado
def eliminar_empleado_ui():
    try:
        id_empleado = obtener_id_empleado_seleccionado()
        if not id_empleado:
            messagebox.showwarning("Advertencia", "Seleccione un empleado")
            return
        if eliminar_empleado(id_empleado):
            messagebox.showinfo("Eliminación", "Empleado eliminado correctamente")
            empleado_combobox['values'] = cargar_empleados()  # Actualizar ComboBox después de eliminar
        else:
            messagebox.showerror("Error", "No se pudo eliminar: ID no encontrado o error en la base de datos.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar empleado: {e}")

# Botones para las operaciones CRUD
tk.Button(ventana, text="Agregar Empleado", command=agregar_empleado).grid(row=10, column=0)
tk.Button(ventana, text="Ver Empleados", command=ver_empleados).grid(row=10, column=1)
tk.Button(ventana, text="Actualizar Salario", command=actualizar_salario).grid(row=11, column=0)
tk.Button(ventana, text="Eliminar Empleado", command=eliminar_empleado_ui).grid(row=11, column=1)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()