def Menu_principal():
    print("========== MENu PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    Menu_principal()
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opcion invalida debe ser un numero entre 1 y 6.")
        except ValueError:
            print("Entrada invalida por favor, ingrese un numero entero.")

def agregar_libro(lista_libros):
    titulo = input("Ingrese el titulo del libro: ").strip()
    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio ni ser solo espacios en blanco.")
        return
    try:
        copias = int(input("Ingrese la cantidad de copias disponibles: "))
        if not validar_copias(copias):
            print("Error la cantidad de copias debe ser un numero entero mayor o igual que cero.")
            return
    except ValueError:
        print("Error la cantidad de copias debe ser un numero entero.")
        return
    try:
        prestamo = int(input("Ingrese el periodo de prestamo en dias: "))
        if not validar_prestamo(prestamo):
            print("Error el periodo de prestamo debe ser un numero entero mayor que cero")
            return
    except ValueError:
        print("Error el periodo de prestamo debe ser un numero entero")
        return
    libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": copias > 0
    }
    lista_libros.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente")

def validar_titulo(titulo):
    return bool(titulo and titulo.strip())

def validar_copias(copias):
    return isinstance(copias, int) and copias >= 0

def validar_prestamo(prestamo):
    return isinstance(prestamo, int) and prestamo > 0

def buscar_libro(lista_libros, titulo):
    for index, libro in enumerate(lista_libros):
        if libro["titulo"] == titulo:
            return index
    return -1

def eliminar_libro(lista_libros):
    titulo = input("Ingrese el titulo que desea eliminar: ").strip()
    index = buscar_libro(lista_libros, titulo)
    if index != -1:
        del lista_libros[index]
        print(f"Libro '{titulo}' eliminado exitosamente")
    else:
        print(f"Libro '{titulo}' no encontrado")

def actualizar_disponibilidad(lista_libros):
    for libro in lista_libros:
        libro['disponible'] = libro['copias'] > 0
    print("Disponibilidad de libros actualizada exitosamente")

def mostrar_libros(lista_libros):
    actualizar_disponibilidad(lista_libros)
    print("===LISTA DE LIBROS===")
    for libro in lista_libros:
        estado = "DISPONIBLE" if libro['disponible'] else "SIN COPIAS"
        print(f"Titulo: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Prestamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("********************************************")
