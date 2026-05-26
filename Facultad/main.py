from facultad import Facultad
from curso import Curso
from estudiante import Estudiante

def pedirEntero(mensaje):
  while True:
    try:
      return int(input(mensaje))
    except ValueError:
      print ("Error, ingrese un número válido")

def pedirTexto(mensaje):
  while True:
    valor = input(mensaje)
    if valor.strip() != "":
      return valor
    print ("Error, el campo no puede estar vacío")

def mostrarMenu():
    print("\n 0: Salir")
    print(" 1: Agregar Curso")
    print(" 2: Agregar Estudiante")
    print(" 3: Inscribir a Curso")
    print(" 4: Dar de baja de Curso")
    print(" 5: Consultar Estado Cursos")
    print(" 6: Consultar Estado Estudiantes")


facultad = Facultad()

mostrarMenu()


opcion = pedirEntero("\nSeleccione una opción: ")

while opcion != 0:

    if opcion == 1:
        codigo = pedirEntero("Código: ")
        nombre = pedirTexto("Nombre: ")
        profesor = pedirTexto("Profesor: ")
        capacidad = pedirEntero("Capacidad: ")
        facultad.agregarCurso(codigo, nombre, profesor, capacidad)

    elif opcion == 2:
        matricula = pedirEntero("Matrícula: ")
        nombre = pedirTexto("Nombre: ")
        apellido = pedirTexto("Apellido: ")
        carrera = pedirTexto("Carrera: ")
        facultad.agregarEstudiante(matricula, nombre, apellido, carrera)

    elif opcion == 3:
        codigo = pedirEntero("Código del curso: ")
        matricula = pedirEntero("Matrícula del estudiante: ")
        facultad.inscribirACurso(codigo, matricula)

    elif opcion == 4:
        codigo = pedirEntero("Código del curso: ")
        matricula = pedirEntero("Matrícula del estudiante: ")
        facultad.darDeBaja(codigo, matricula)

    elif opcion == 5:
        facultad.consultarEstadoCursos()

    elif opcion == 6:
        facultad.consultarEstadoEstudiantes()

    else:
        print("Opción no válida.")

    mostrarMenu()
  
    opcion = pedirEntero("\n Seleccione una opción: ")


print("\n ¡Hasta luego!")
