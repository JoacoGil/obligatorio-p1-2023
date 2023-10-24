from Empleado import Empleado

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, edad, nacionalidad, fecha_nacimiento, salario):
        super().__init__(id, nombre, edad, nacionalidad, fecha_nacimiento, salario)