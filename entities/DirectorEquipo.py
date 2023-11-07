from Empleado import Empleado

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, nacionalidad, fecha_nacimiento, salario):
        super().__init__(id, nombre, nacionalidad, fecha_nacimiento, salario)