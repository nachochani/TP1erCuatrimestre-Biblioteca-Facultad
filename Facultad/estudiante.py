class Estudiante:
    def __init__(self, matricula, nombre, apellido, carrera):
        self.__matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__cursosInscriptos = []
    
    def getMatricula(self):
        return self.__matricula

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getCarrera(self):
        return self.__carrera

    def agregarCurso(self, matricula):
        self.__cursosInscriptos.append(matricula)

    def quitarCurso(self, matricula):
        self.__cursosInscriptos.remove(matricula)

    def getInscriptos(self):
        return self.__cursosInscriptos
    
    def __str__(self):
        if self.__cursosInscriptos:
            nombres = ", ".join(
                f"'{c.getNombre()}'" for c in self.__cursosInscriptos)
        else:
            nombres = "Ninguno"
        return f"[{self.__matricula}] {self.__nombre} {self.__apellido} | Cursos: {nombres}"