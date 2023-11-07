class Empleado:
    def __init__(self, id, nombre, nacionalidad, fecha_nacimiento, salario):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.salario = salario

    def get_id(self):
        return self.id