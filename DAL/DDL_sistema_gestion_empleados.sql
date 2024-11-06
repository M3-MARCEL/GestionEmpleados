CREATE DATABASE IF NOT EXISTS sistema_gestion_empleados;
USE sistema_gestion_empleados;

CREATE TABLE Rol (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    permisos TEXT
);

CREATE TABLE TipoEmpleado (
    id_tipo_empleado INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(20) NOT NULL,
    detalle VARCHAR(100)
);

CREATE TABLE Departamento (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    telefono VARCHAR(15),
    gerente_id INT
);

CREATE TABLE Proyecto (
    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE
);

CREATE TABLE Modulo (
    id_modulo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Empleado (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    rut VARCHAR(12) UNIQUE NOT NULL,
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    correo VARCHAR(50),
    fecha_inicio DATE,
    rol_empleado_id INT,
    salario DECIMAL(10, 2),
    contraseña VARCHAR(256),
    tipo_empleado_id INT,
    departamento_id INT,
    FOREIGN KEY (rol_empleado_id) REFERENCES Rol(id_rol),
    FOREIGN KEY (tipo_empleado_id) REFERENCES TipoEmpleado(id_tipo_empleado),
    FOREIGN KEY (departamento_id) REFERENCES Departamento(id_departamento)
);

CREATE TABLE ProyectoEmpleado (
    id_proyecto_empleado INT PRIMARY KEY AUTO_INCREMENT,
    proyecto_id INT,
    empleado_id INT,
    FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id_proyecto),
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id_empleado)
);

CREATE TABLE RegistroTiempo (
    id_registro_tiempo INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE,
    horas INT CHECK (horas > 0 AND horas <= 24),
    tareas TEXT,
    observacion TEXT,
    empleado_id INT,
    proyecto_id INT,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id_empleado),
    FOREIGN KEY (proyecto_id) REFERENCES Proyecto(id_proyecto)
);

CREATE TABLE Accesos (
    id_acceso INT PRIMARY KEY AUTO_INCREMENT,
    empleado_id INT,
    modulo_id INT,
    FOREIGN KEY (empleado_id) REFERENCES Empleado(id_empleado),
    FOREIGN KEY (modulo_id) REFERENCES Modulo(id_modulo)
);

CREATE TABLE Informe (
    id_informe INT PRIMARY KEY AUTO_INCREMENT,
    nombre_informe VARCHAR(50) NOT NULL,
    fecha_creacion DATE,
    creador_id INT,
    ubicacion VARCHAR(100),
    FOREIGN KEY (creador_id) REFERENCES Empleado(id_empleado)
);