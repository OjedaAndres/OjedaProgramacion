""" 1. Datos que debe manejar el sistema
El sistema trabaja con una colección de libros. Esta colección debe existir desde
que el programa inicia y estar disponible durante toda la ejecución. Cada vez que
se agrega un libro, se incorpora a esa colección como un nuevo elemento.
Cada libro se representa como un conjunto de campos asociados: título, copias,
préstamo y un indicador de si está disponible o no. La siguiente tabla resume los
campos de cada registro:
Campo Qué representa Restricciones de
validación
"titulo" Título del libro No vacío ni solo
espacios en blanco
"copias" Cantidad de copias
disponibles
Numero entero mayor
o igual que cero
"prestamo" Período de préstamo
en días
Numero entero mayor
que cero
"disponible" ¿Hay al menos una
copia disponible?
False al registrar. No
se valida ni se solicita
al usuario: el sistema
lo asigna
Cada diccionario se guarda dentro de una lista. La lista es la colección general; los
diccionarios son los libros individuales dentro de ella. El programa comienza con la
lista vacía y la va llenando a medida que se agregan registros.
2. Lo que debe hacer el sistema
El sistema se controla desde un menu que aparece en pantalla cada vez que el
usuario termina una acción. El usuario elige una opción numérica, el programa
ejecuta la tarea correspondiente y vuelve a mostrar el menu. Esto se repite hasta
que el usuario elige salir.
El menu tiene seis opciones:
========== MENu PRINCIPAL ==========
1. Agregar libro
2. Buscar libro
3. Eliminar libro
4. Actualizar disponibilidad
5. Mostrar libros
6. Salir
=====================================
Para implementar este comportamiento debes definir dos funciones separadas: una
que muestre las opciones en pantalla (sin recibir nada ni retornar nada) y otra que
lea y retorne la opción elegida por el usuario (sin recibir nada, retornando el numero
validado). Ambas funciones deben invocarse en cada vuelta del ciclo.
A continuación, se describe qué debe ocurrir al elegir cada opción:
Opción 1 - Agregar libro:
El sistema solicita al usuario el título, las copias y el período de préstamo del libro.
Antes de guardar el registro, verifica que cada dato cumpla su condición:
• El nombre no puede estar vacío ni ser solo espacios en blanco.
• Las copias deben ser un numero entero mayor o igual que cero.
• El período de préstamo debe ser un numero entero mayor que cero.
Si algun dato no cumple la condición, el sistema informa al usuario y no registra el
libro. Solo cuando todos los datos son válidos se crea el diccionario y se agrega a
la lista.
Para implementar esta opción debes definir una función que reciba la lista como
parámetro. Dentro de ella se solicitan los datos al usuario y se llama a una función
de validación distinta para cada campo. Los mensajes de error se muestran en esta
función, no dentro de las validaciones.
automáticamente. Su
valor puede cambiar a
True cuando se
ejecute la opción 4
(Actualizar
disponibilidad), segun
las copias del libro.
Opción 2 - Buscar libro:
El sistema solicita un título de libro al usuario y recorre la lista buscando un registro
cuyo campo título coincida exactamente con el ingresado. Si lo encuentra, muestra
la posición en la que está y sus datos. Si no existe ningun registro con ese título,
informa al usuario.
Para implementar esta opción debes definir una función que reciba la lista y el título
a buscar como parámetros. La función recorre la lista y retorna la posición del
registro encontrado, o -1 si no existe. Es el programa principal quien recibe ese valor
y decide qué hacer con él: si la posición es válida, muestra los datos del libro en esa
posición; si es -1, muestra el mensaje de no encontrado.
Opción 3 - Eliminar libro:
El sistema solicita el título del libro que se desea eliminar. Para localizarlo, llama a
la función de busqueda definida en la opción anterior, pasándole la lista y el título
ingresado. Si la función retorna una posición válida, el sistema elimina el registro en
esa posición. Si retorna -1, informa al usuario con el siguiente mensaje:
El libro 'titulo' no se encuentra registrado.
Opción 4 - Actualizar disponibilidad:
El sistema recorre la lista completa de libros y actualiza el campo "disponible" de
cada registro segun sus copias: si las copias son mayor o igual a 1, el campo pasa
a True; si es menor, queda en False. Esta operación afecta a todos los registros de
la lista sin excepción.
Para implementar esta opción debes definir una función que reciba la lista como
parámetro y aplique esa regla a cada elemento.
Opción 5 - Mostrar libros:
El sistema primero actualiza la disponibilidad de todos los libros haciendo el llamado
a la función anterior, luego recorre la lista mostrando los datos de cada libro. El
formato de salida es el siguiente:
=== LISTA DE LIBROS ===
Título: El Quijote
Copias: 5
Préstamo: 2
Estado: DISPONIBLE
********************************************
Título: Don Segundo Sombra
Copias: 0
Préstamo: 3
Estado: SIN COPIAS
*********************************************
Opción 6 - Salir:
El sistema termina la ejecución de forma limpia, sin errores. El ciclo del menu se
detiene y el programa finaliza con un mensaje de despedida:
“Gracias por usar el sistema. Vuelva Pronto” """



print("Bienvenido al sistema de gestión de libros")
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
    titulo = input("Ingrese el título del libro: ").strip()
    if not validar_titulo(titulo):
        print("Error: El título no puede estar vacío ni ser solo espacios en blanco.")
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
        prestamo = int(input("Ingrese el período de prestamo en dias: "))
        if not validar_prestamo(prestamo):
            print("Error el período de prestamo debe ser un numero entero mayor que cero")
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
