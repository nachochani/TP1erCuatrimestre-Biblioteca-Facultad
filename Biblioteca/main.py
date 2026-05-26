from biblioteca import Biblioteca
from libro import Libro
from miembro import Miembro

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
    print(" 1: Agregar Libro")
    print(" 2: Agregar Miembro")
    print(" 3: Mostrar Libros")
    print(" 4: Mostrar Miembros")
    print(" 5: Prestar Libro")
    print(" 6: Devolver Libro")
    print(" 7: Consultar Estado Libros")
    print(" 8: Consultar Estado Miembros")


biblioteca = Biblioteca()

mostrarMenu()


opcion = pedirEntero("\nSeleccione una opción: ")

while opcion != 0:

    if opcion == 1:
        titulo = pedirTexto("Título: ")
        autor = pedirTexto("Autor: ")
        isbn = pedirEntero("ISBN: ")
        biblioteca.agregarLibro(titulo, autor, isbn)

    elif opcion == 2:
        dni = pedirEntero("DNI: ")
        nombre = pedirTexto("Nombre: ")
        biblioteca.agregarMiembro(dni, nombre)

    elif opcion == 3:
        biblioteca.consultarEstadoLibros()

    elif opcion == 4:
        biblioteca.consultarEstadoMiembros()

    elif opcion == 5:
        dni = pedirEntero("DNI del miembro: ")
        isbn = pedirEntero("ISBN del libro: ")
        biblioteca.prestarLibro(isbn, dni)

    elif opcion == 6:
        isbn = pedirEntero("ISBN del libro: ")
        dni = pedirEntero("DNI del miembro: ")
        biblioteca.devolverLibro(isbn, dni)
    
    elif opcion == 7:
        biblioteca.consultarEstadoLibros()

    elif opcion == 8:
        biblioteca.consultarEstadoMiembros()

    else:
        print("Opción no válida.")

    mostrarMenu()
  
    opcion = pedirEntero("\n Seleccione una opción: ")


print("\n ¡Hasta luego!")
