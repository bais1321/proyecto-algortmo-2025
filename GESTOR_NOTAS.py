from math import factorial


historialcursos = {}
historialgeneral = []
busquedalineal = {}

# 1. Registro de notas de cursos
def registronotacurso():
    nombre = input("ingrese el nombre del curso: ").strip()
    if not nombre:
        print("el nombre del curso no puede estar vacío.")
        return
    try:
        nota = float(input("ingrese la nota obtenida (0-100): "))
        if nota < 0 or nota > 100:
            print("la nota debe estar entre 0 y 100.")
            return
    except ValueError:
        print("la nota debe ser un numero.")
        return

    historialcursos[nombre] = nota
    print(f"curso {nombre} registrado correctamente con nota {nota}.")

# 2. Mostrar cursos
def mostrarcursos(historialcursos):
    if not historialcursos:
        print("no hay cursos registrados.")
    else:
        print("listado de cursos registrados:")
        for nombre, nota in historialcursos.items():
            print(f"{nombre} → nota: {nota}")

# 3. Promedio general
def promediogeneral(historialcursos):
    if not historialcursos:
        print("no hay cursos registrados para calcular el promedio.")
        return

    total = sum(historialcursos.values())
    promedio = total / len(historialcursos)
    print(f"promedio general calculado: {promedio:.2f}")

# 4. Conteo de cursos aprobados y reprobados
def reproapro(historialcursos):
    aprobados = 0
    reprobados = 0
    for nota in historialcursos.values():
        if nota >= 60:
            aprobados += 1
        else:
            reprobados += 1
    print(f"total de cursos aprobados: {aprobados}")
    print(f"total de cursos reprobados: {reprobados}")

# 5. Búsqueda lineal
def busquedalineal_func(historialcursos, busquedalineal, historialgeneral):
    nombre = input("ingrese el nombre del curso a buscar: ").strip()
    if not nombre:
        print("este campo no puede estar vacio")
        return

    encontrado = False
    for curso in historialcursos:
        if curso.lower() == nombre.lower():
            print(f"curso encontrado: {curso} // nota: {historialcursos[curso]}")
            busquedalineal[curso] = busquedalineal.get(curso, 0) + 1
            print(f"este curso ha sido consultado {busquedalineal[curso]} veces.")
            historialgeneral.append(f"Se busco el curso {curso} - total de busquedas: {busquedalineal[curso]}")
            encontrado = True
            break
    if not encontrado:
        print("curso no encontrado.")
        historialgeneral.append(f"busqueda fallida: curso {nombre} no encontrado.")

# 6. Actualizar o editar nombre del curso/nota
def editarcursonota(historialcursos, historialgeneral):
    nombre = input("ingrese el nombre del curso que desea actualizar: ").strip()
    if not nombre:
        print("este campo no puede estar vacío.")
        return
    if nombre not in historialcursos:
        print(f"el curso '{nombre}' no esta registrado.")
        historialgeneral.append(f"intento fallido de actualizacion: curso {nombre} no encontrado.")
        return
    cursoactual = nombre
    notaactual = historialcursos[cursoactual]
    while True:
        print(f"curso seleccionado: {cursoactual}  nota actual: {notaactual}")
        print("1. editar nombre del curso")
        print("2. editar nota del curso")
        print("3. confirmar cambios")
        try:
            opcion = int(input("seleccione una opcion: "))
        except ValueError:
            print("ingrese una opción valida.")
            continue
        if opcion == 1:
            nuevonombre = input("ingrese el nuevo nombre del curso: ").strip()
            if not nuevonombre:
                print("este campo no puede estar vacio.")
                continue
            if nuevonombre in historialcursos:
                print("ya existe un curso con ese nombre.")
                continue
            historialcursos[nuevonombre] = historialcursos.pop(cursoactual)
            historialgeneral.append(f"nombre actualizado: '{cursoactual}' → '{nuevonombre}'")
            cursoactual = nuevonombre
            print(f"nombre cambiado a {nuevonombre}.")
        elif opcion == 2:
            try:
                nuevanota = float(input("ingrese la nueva nota (0-100): "))
                if nuevanota < 0 or nuevanota > 100:
                    print("la nota debe estar entre 0 y 100.")
                    continue
            except ValueError:
                print("la nota debe ser un numero.")
                continue
            historialcursos[cursoactual] = nuevanota
            notaactual = nuevanota
            historialgeneral.append(f"nota actualizada para {cursoactual}: {nuevanota}")
            print(f"nota cambiada a {nuevanota}.")
        elif opcion == 3:
            print("actualizado... regresando al menu principal...")
            break
        else:
            print("opción no valida.")

# 7. Eliminar curso
def eliminarcurso(historialcursos, historialgeneral):
    if not historialcursos:
        print("no hay cursos registrados para eliminar.")
        return
    nombre = input("ingrese el nombre del curso que desea eliminar: ").strip()
    if not nombre:
        print("este campo no puede estar vacio.")
        return
    curso_encontrado = None
    for curso in historialcursos:
        if curso.lower() == nombre.lower():
            curso_encontrado = curso
            break
    if curso_encontrado:
        confirmacion = input(f"seguro que desea eliminar {curso_encontrado} (s/n): ").lower()
        if confirmacion == 's':
            historialcursos.pop(curso_encontrado)
            historialgeneral.append(f"curso eliminado: {curso_encontrado}")
            print(f"Curso '{curso_encontrado}' eliminado correctamente")
        else:
            print("la eliminacion fue cancelada")
    else:
        print(f"el curso {nombre} no fue encontrado.")
        historialgeneral.append(f"intento fallido de eliminación: curso {nombre} no existe.")

# 8. Ordenar por nota


#9. Ordenar por nombre
def ordenar_por_nombre(cursos, historial):
  




#10. Búsqueda binaria
def busqueda_binaria(cursos, historial):
    if not cursos:
        print("No hay cursos registrados.")
        return

    nombre = input("Ingrese el nombre del curso a buscar (binaria): ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    nombres_ordenados = sorted(cursos.keys(), key=lambda x: x.lower())
    izquierda = 0
    derecha = len(nombres_ordenados) - 1
    encontrado = False

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        curso_medio = nombres_ordenados[medio]

        if curso_medio.lower() == nombre.lower():
            nota = cursos[curso_medio]
            print(f"Curso encontrado: {curso_medio} / Nota: {nota}")
            historial.append(f"Búsqueda binaria exitosa: '{curso_medio}' con nota {nota}")
            encontrado = True
            break
        elif nombre.lower() < curso_medio.lower():
            derecha = medio - 1
        else:
            izquierda = medio + 1

    if not encontrado:
        print("Curso no encontrado.")
        historial.append(f"Búsqueda binaria fallida: curso '{nombre}' no existe.")

#11. Simular cola de revisión
def simular_cola_revision(historialcursos):
    if not historialcursos:
        print("No hay cursos en el historial.")
        return

    print("Simulando cola de revisión...")
    for curso, nota in historialcursos.items():
        print(f"Revisando curso: {curso} / Nota: {nota}")

# 12. Mostrar historial de cambios
def mostrarhistorial(historialgeneral):
    if not historialgeneral:
        print("no hay historial de acciones.")
    else:
        print("historial de acciones realizadas:")
        for evento in historialgeneral:
            print(f"- {evento}")

# Menú principal
print("bienvenido al sistema de registro de notas")
nom_pers = input("Ingrese su nombre para empezar: ")
print("Nombre registrado, ¡empecemos!")

while True:
    print("\nMenú principal:")
    print("1. Agregar curso")
    print("2. Mostrar cursos")
    print("3. Calcular promedio")
    print("4. Conteo de cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (lineal)")
    print("6. Actualizar o editar nombre del curso/nota")
    print("7. Eliminar curso")
    print("8. Ordenar por nota")
    print("9. Ordenar por nombre")
    print("10. Buscar curso por nombre (binaria)")
    print("11. Simular cola de revisión")
    print("12. Mostrar historial de cambios")
    print("13. Salir")

    try:
        opcion = int(input("Ingrese el número de la opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        registronotacurso()
    elif opcion == 2:
        mostrarcursos(historialcursos)
    elif opcion == 3:
        promediogeneral(historialcursos)
    elif opcion == 4:
        reproapro(historialcursos)
    elif opcion == 5:
        busquedalineal_func(historialcursos, busquedalineal, historialgeneral)
    elif opcion == 6:
        editarcursonota(historialcursos, historialgeneral)
    elif opcion == 7:
        eliminarcurso(historialcursos, historialgeneral)
    elif opcion == 8:
        ordenar_por_nota(cursos=historialcursos, historial=historialgeneral)
    elif opcion == 9:
        ordenar_por_nombre(cursos=historialcursos, historial=historialgeneral)
    elif opcion == 10:
        busqueda_binaria(cursos=historialcursos, historial=historialgeneral)
    elif opcion == 11:
        simular_cola_revision(historialcursos)
    elif opcion == 12:
        mostrarhistorial(historialgeneral)
    elif opcion == 13:
        print(f"Gracias por usar el sistema, {nom_pers}, adiosito")
        break
    else:
        print("ingrese una opcion valida")