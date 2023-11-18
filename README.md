Programa de Gestión de Equipos de Fórmula 1
Este programa permite la gestión de empleados, autos y equipos para el entorno de una competencia de Fórmula 1.

##Funcionalidades Principales##
    •Alta de Empleado: Registra nuevos empleados en el sistema. Permite agregar pilotos, pilotos de reserva, mecánicos y directores de equipo.
    •Alta de Auto: Registra nuevos autos para su utilización en las carreras. Permite especificar el modelo, puntaje y color.
    •Alta de Equipo: Crea nuevos equipos, asignando autos y empleados. Los empleados se asignan según su rol (piloto titular, piloto de reserva, mecánico, director de equipo).
    •Simular Carrera: Ejecuta una simulación de carrera, considerando posibles imprevistos como lesiones, abandonos, errores en pits y penalizaciones.
    •Realizar Consultas: Proporciona opciones para consultar información relevante sobre pilotos y equipos.

##Uso del Programa##
Para ejecutar el programa, se puede utilizar la clase ProgramaF1. Al iniciar el programa, se despliega un menú con diversas opciones. El usuario puede seleccionar una opción numerada para realizar la operación correspondiente.
--- Menú Principal ---
1. Alta de empleado
2. Alta de auto
3. Alta de equipo
4. Simular carrera
5. Realizar consultas
6. Finalizar programa

##Requisitos##
Este programa está diseñado para trabajar con los siguientes módulos:
•entities: Contiene las entidades necesarias para el programa (Empleado, Auto, Equipo, etc.).
Para obtener un funcionamiento adecuado, asegúrate de tener acceso a las clases y módulos importados al principio del código.

############Relaciones entre las clases expresadas en el Diagrama de Clases############
1. Herencia:
•Entre Empleado, Mecanico, DirectorEquipo, PilotoReserva, y Piloto: Las clases Mecanico, DirectorEquipo y Piloto heredan los atributos y métodos de la clase Empleado, constituyendo entonces subclases de la misma. De esta misma forma, la clase PilotoReserva hereda de la clase Piloto.
2. Composición:
•Entre Equipo y subclases de empleados (Piloto, Mecanico, DirectorEquipo, PilotoReserva):La clase Equipo contiene directamente instancias de las subclases específicas de empleados como parte integral de su estructura. Cada instancia de Equipo contiene instancias de Piloto, Mecanico, DirectorEquipo y PilotoReserva.
3. Asociación:
•Entre Equipo y Auto:La clase Equipo tiene una asociación con la clase Auto al asignar un modelo de auto a un equipo específico.
•Entre ProgramaF1, Equipo, Auto y subclases de empleados (Piloto, Mecanico, DirectorEquipo, PilotoReserva):La clase ProgramaF1 coordina las interacciones entre Equipo, Auto y las subclases de empleados, permitiendo realizar operaciones como altas de empleados, autos, equipos, simulaciones de carrera y consultas.
Estas relaciones modelan cómo las clases interactúan entre sí en el contexto del programa de Fórmula 1, donde la clase ProgramaF1 actúa como un coordinador principal, manipulando instancias de Equipo, Auto y las diferentes subclases de empleados.

