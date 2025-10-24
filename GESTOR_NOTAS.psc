Proceso SistemaRegistroNotas
    // Declaración de variables
    Definir nombre Como Cadena
    Definir opciones, n, i Como Entero
    Definir curso, buscado, nombreEditar, conf, nomConf Como Cadena
    Definir nota, suma, promedio Como Real
    Definir aprobados, reprobados, contador Como Entero
    Definir historial Como Cadena
    Definir encontrado Como Logico
	
    // Inicializar
    historial <- ""
    opciones <- 0
	
    Escribir "Bienvenido al sistema de registro de notas"
    Escribir "Ingrese su nombre:"
    Leer nombre
    Si nombre = "" Entonces
        Escribir "El nombre no puede estar vacío. Reinicie el programa."

FinSi

repetir
	Escribir ""
	Escribir "------ MENÚ PRINCIPAL ------"
	Escribir "1. Registrar cursos"
	Escribir "2. Mostrar resumen del último registro"
	Escribir "3. Calcular promedio (del último registro)"
	Escribir "4. Contar aprobados y reprobados (último registro)"
	Escribir "5. Buscar curso (no disponible sin arreglos)"
	Escribir "6. Editar curso/nota (no disponible sin arreglos)"
	Escribir "7. Eliminar curso (no disponible sin arreglos)"
	Escribir "8. Ordenar por nota (no disponible sin arreglos)"
	Escribir "9. Ordenar alfabéticamente (no disponible sin arreglos)"
	Escribir "10. Búsqueda binaria (no disponible sin arreglos)"
	Escribir "11. Simular cola de revisión"
	Escribir "12. Mostrar historial"
	Escribir "13. Salir"
	Escribir "Ingrese el número de la opción (1-13):"
	Leer opciones
	
	// Validar rango de opción
	Si opciones < 1 O opcion > 13 Entonces
		Escribir "Opción no válida. Ingrese un número entre 1 y 13."
	Sino
		Segun opciones Hacer
			
			1:
				Escribir "¿Cuántos cursos desea registrar? (número entero mayor que 0):"
				Leer n
				Si n <= 0 Entonces
					Escribir "Debe ingresar un número mayor que 0."
				Sino
					suma <- 0
					aprobados <- 0
					reprobados <- 0
					contador <- 0
					// Registramos n cursos, pero sin guardarlos en un arreglo (solo estadísticas y último curso)
					Para i <- 1 Hasta n Con Paso 1 Hacer
						Escribir "Ingrese el nombre del curso ", i, ":"
						Leer curso
						Si curso = "" Entonces
							Escribir "El nombre no puede estar vacío. Intente de nuevo."
							i <- i - 1 // repetir esta iteración
						Sino
							Escribir "Ingrese la nota de ", curso, " (0-100):"
							Leer nota
							Si nota < 0 O nota > 100 Entonces
								Escribir "Nota inválida. Debe ser entre 0 y 100. Reingrese este curso."
								i <- i - 1 // repetir esta iteración
							Sino
								suma <- suma + nota
								contador <- contador + 1
								Si nota >= 60 Entonces
									aprobados <- aprobados + 1
								Sino
									reprobados <- reprobados + 1
								FinSi
								// Guardamos en historial un resumen parcial (último curso)
								historial <- historial + "Registro curso: " + curso + " - Nota: " + ConvertirATexto(nota) + SaltoLinea
							FinSi
						FinSi
					FinPara
					
					Si contador > 0 Entonces
						promedio <- suma / contador
						Escribir "Se registraron ", contador, " cursos."
						Escribir "Promedio general del registro: ", promedio
						historial <- historial + "Resumen: " + ConvertirATexto(contador) + " cursos. Promedio: " + ConvertirATexto(promedio) + SaltoLinea
					Sino
						Escribir "No se registró ningún curso válido."
					FinSi
				FinSi
				
			2:
				Escribir "---- Resumen del último registro ----"
				Si historial = "" Entonces
					Escribir "No hay registros aún."
				Sino
					// Mostramos las últimas líneas del historial (a falta de arreglos)
					Escribir historial
				FinSi
				
			3:
				Escribir "no esta disponible esta opcion"
				
			4:
				Escribir "no esta disponible esta opcion"
				
			5:
				Escribir "no esta disponible esta opcion"
				
			6:
				Escribir "no esta disponible esta opcion"
				
			7:
				Escribir "no esta disponible esta opcion"
				
			8:
				Escribir "no esta disponible esta opcion"
				
			9:
				Escribir "no esta disponible esta opcion"
				
			10:
				Escribir "no esta disponible esta opcion"
				
			11:
				Escribir "Simulación de cola de revisión (ejemplo con 3 agentes simulados):"
				Para i <- 1 Hasta 3 Con Paso 1 Hacer
					Escribir "Atendiendo persona ", i, " en la cola de revisión..."
				FinPara
				historial <- historial + "Simulación de cola de revisión realizada." + SaltoLinea
				
			12:
				Escribir "---- Historial de acciones ----"
				Si historial = "" Entonces
					Escribir "No hay historial."
				Sino
					Escribir historial
				FinSi
				
			13:
				Escribir "Gracias por usar el sistema, ", nombre, ". Saliendo..."
				// Salida manejada por la condición del Repetir...Hasta
		FinSegun
	FinSi

Hasta Que  opciones = 13

FinProceso
