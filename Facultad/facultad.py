from curso import Curso
from estudiante import Estudiante

class Facultad:
    def __init__(self):
        self.__estudiantes = []
        self.__cursos = []

    def _buscarEstudiante(self, matricula):
        for estudiante in self.__estudiantes:
            if estudiante.getMatricula() == matricula:
                return estudiante
        raise LookupError(f"No se encontró a ningún estudiante con Matrícula '{matricula}'.")

    def _buscarCurso(self, codigo):
        for curso in self.__cursos:
            if curso.getCodigo() == codigo:
                return curso
        raise LookupError(f"No se encontró ningún curso con Código '{codigo}'.")

    def agregarEstudiante(self, matricula, nombre, apellido, carrera):
        try:
            for estudiante in self.__estudiantes:
                if estudiante.getMatricula() == matricula:
                    raise ValueError(f"Ya existe un estudiante con la Matrícula '{matricula}'.")
            estudiante = Estudiante(matricula, nombre, apellido, carrera)
            self.__estudiantes.append(estudiante)
            print(f"Estudiante agregado: {nombre} {apellido} .")
        except ValueError as e:
            print(f"{e}")

    def agregarCurso(self, codigo, nombre, profesor, capacidad):
        try:
            for curso in self.__cursos:
                if curso.getCodigo() == codigo:
                    raise ValueError(f"Ya existe un curso con Código '{codigo}'.")
            curso = Curso(codigo, nombre, profesor, capacidad)
            self.__cursos.append(curso)
            print(f"Curso agregado: {nombre}.")
        except ValueError as e:
            print(f"{e}")

    def inscribirACurso(self, codigo, matricula):
        try:
            curso = self._buscarCurso(codigo)
            estudiante = self._buscarEstudiante(matricula)
            if curso.getCuposDisponibles() == 0:
                raise PermissionError(
                    f" El curso {curso.getNombre()} no tiene cupos disponibles."
                )
            curso.agregarEstudiante(estudiante)
            estudiante.agregarCurso(curso)
            print(f"Estudiante: {estudiante.getNombre()} {estudiante.getApellido()} inscripto a {curso.getNombre()}.")
        except (LookupError, PermissionError) as e:
            print(f"{e}")

    def darDeBaja(self, codigo, matricula):
        try:
            curso = self._buscarCurso(codigo)
            estudiante = self._buscarEstudiante(matricula)
            if not any(e.getMatricula() == matricula for e in curso.getInscriptos()):
                raise PermissionError(
                    f"El estudiante {estudiante.getNombre()} no está inscripto en el curso {curso.getNombre()}.")
            
            estudiante.quitarCurso(curso)
            curso.quitarEstudiante(estudiante)
            print(f"El estudiante {estudiante.getNombre()} fue eliminado del curso {curso.getNombre()}.")
        except (LookupError, PermissionError) as e:
            print(f"{e}")

    def consultarEstadoCursos(self):
        print(" ESTADO DE CURSOS")
        if not self.__cursos:
            print("  No hay cursos registrados.")
        else:
            for curso in self.__cursos:
                print(f"  {curso}")

    def consultarEstadoEstudiantes(self):
        print("  ESTADO DE ESTUDIANTES")
        if not self.__estudiantes:
            print("  No hay estudiantes registrados.")
        else:
            for estudiante in self.__estudiantes:
                print(f"  {estudiante}")