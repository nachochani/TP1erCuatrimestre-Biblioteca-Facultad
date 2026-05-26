class Curso:
    def __init__(self, codigo, nombre, profesor, capacidad):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = profesor
        self.__capacidad = capacidad
        self.__estudiantesInscriptos = []

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre

    def getProfesor(self):
        return self.__profesor
    
    def getCapacidad(self):
        return self.__capacidad

    def getCuposDisponibles(self):
        return self.__capacidad - len(self.__estudiantesInscriptos)

    def agregarEstudiante(self, codigo):
        self.__estudiantesInscriptos.append(codigo)

    def quitarEstudiante(self, codigo):
        self.__estudiantesInscriptos.remove(codigo)

    def getInscriptos(self):
        return self.__estudiantesInscriptos

    def __str__(self):
        if self.__estudiantesInscriptos:
            nombres = ", ".join(
                f"'{e.getNombre()}'" for e in self.__estudiantesInscriptos)
        else:
            nombres = "Ninguno"
        return (
            f"[{self.__codigo}] '{self.__nombre}' " 
            f"| Profesor: {self.__profesor} "
            f"| Cupos: {self.__capacidad - len(self.__estudiantesInscriptos)} "
            f"| Estudiantes: {nombres}"
        )