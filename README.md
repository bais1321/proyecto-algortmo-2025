GESTOR DE NOTAS ACADEMICAS:
este proyecto esta dirigido a aquellas personas a las cuales les interés el uso de
aplicaciones fáciles  y eficaces al momento de tener un registro de notas ya que 
permite almacenar, modificar, mostrar y calcular un promedio general. puede ser 
utilizado para maestros que quieran  almacenar las notas de diferentes cursos de 
sus estudiantes.

 
Su funcionamiento es recaudar una variedad de dato (nombre de cursos y notas de cada curso)
cada curso tendrá que tener una ponderación entre 0 - 100 para almacenarlos y luego mostrarlos 
si asi lo desee el usuario, calcular el promedio general del usuario 
(nota del curso 1 + curso2 + curso3 + ... / cantidad de cursos ingresados ), 
evaluar si los datos ingresados son aprobados o reprobados por medio de la nota si es < a 60 estará 
reprobado si es >= que 60 esta aprobado al evaluarlo nos mostrara la cantidad de cursos aprobados 
y de igual forma los reprobados, contara con dos formas de busqueda: 1. de forma lineal osea que 
evaluara el nombre que uno ingrese con cada nombre registrado uno a la vez y si posee concidencia 
lo estara mostrando en pantalla y repitira la evaluacion con cada nombre hasta no encontrar mas 
concidencias 2. busqueda binaria esta es diferente a la busqueda anterior, hasta donde he comprendido 
este tipo de busqueda se base en la cantidad de caracteres que posee un nombre de curso y evalua si 
sus caracteres conciden ya que lo que hace esta evaluacion es dividir y avaluar por dos secciones, 
izquierda y derecha y si ambas conciden lo va mostrando de lo contrario lo descarta y pasa al siquiente, 
permitira modificar la nota de cualquier curso, si a registrado un curso el cual ya no desea tener el 
usuario este podra ser borrado, al momento de querer ver los cursos y sus notas podra ordenarlos de 
dos formas: 1. ordenamiento en base las notas de mayor a menor y 2.por el nombre del curso de A-Z, 
mostrara el historial que se a tenido el programa es decir si a habido alguna modificacion o se agregado 
algo nuevo habra un historial que respalde al usuario y por ultimo se ara una cimulacion que permita 
obtener todos los datos (nombre del curso y la nota) para luego enviarlos aprobando que ya se a realizado 
la revision correspondiente por el usuario.

la forma de implementar estoas funciones sera en base a un menu inicial que mostrara las opciones 
disponibles para que el usuario lo realice de forma facil y eficiente, cada valor ingresado tendra 
que ser de forma correcta para que la ejecucion de dicha opcion a requerir sea correcta. no se 
implementaran librerias externas a python.









pseudocodigo

Algoritmo gestor_notas
	total = 0
	Repetir
		Escribir "bienvenido, este es el menu de las opciones disponibles que tiene"
		Escribir "1. Registrar nuevo curso"
		Escribir "2. Mostrar todos los cursos"
		Escribir "3. Calcular promedio general"
		Escribir "4. Contar cursos aprobados y reprobados"
		Escribir "5. en espera"
		Escribir "6 simulacion"
		Escribir "7 salir"
		Escribir "Seleccione una opción:"
		leer menu 
		segun menu Hacer
				//1 INGRESAR NOMBRE DE CURSO Y NOTA
			1: si total  < 6 Entonces
					total = total +1
					Escribir "Nombre del curso " total ":"
					segun total Hacer
						1: leer curso1
						2: leer curso2
						3: leer curso3
						4: leer curso4
						5: leer curso5
					FinSegun
					Escribir "ingrese la nota del " total ":"
					segun total Hacer
						1: leer nota1
						2:leer nota2
						3: leer nota3
						4: leer nota4
						5: leer nota5
					FinSegun
				sino 
					Escribir "ya no puede ingresar mas cursos y notas"
				FinSi
				suma = nota1 + nota2 + nota3 + nota4 + nota5
				//2 MOSTRAR UN LISTADO DE LOS CURSOS INGRESADOS
			2: para i = 1 Hasta total Hacer
					segun i Hacer
						1:escribir "curso" curso1 "nota de:" nota1
						2:escribir "curso" curso2 "nota de:" nota2
						3:escribir "curso" curso3 "nota de:" nota3
						4:escribir "curso" curso4 "nota de:" nota4
						5:escribir "curso" curso5 "nota de:" nota5
					FinSegun
				FinPara
				// CALCULAR EL PROMEDIO GENERAL DE TODOS LOS CURSOS
			3: si total = 0 Entonces
					Escribir "no a ingresado cursos, no ay promedio para calcular"
				SiNo
					escribir "su promedio general en base a sus registros es de: " suma/total
				FinSi
				//EVALUAR CUANTOS CURSOS APROBADOS Y REPROBADOS EXISTEN
			4: aprobado = 0 
			reprobado = 0
			para i = 1 Hasta total Hacer
			segun i Hacer
			1:Si nota1 >= 60 Entonces
		    aprobados = aprobados+1
			SiNo
			Si nota1 <= 59 Entonces
			reprobados = reprobados+1
			FinSi
			FinSi
			2:Si nota2 >= 60 Entonces
			aprobados = aprobados+1
			SiNo
			Si nota2 <= 59 Entonces
			reprobados = reprobados+1
			FinSi
			FinSi
		    3:Si nota3 >= 60 Entonces
			aprobados = aprobados+1
			SiNo
			Si nota3 <= 59 Entonces
			reprobados = reprobados+1
			FinSi
			FinSi
		    4:Si nota4 >= 60 Entonces
			aprobados = aprobados+1
			SiNo
			Si nota4  <= 60 Entonces
			reprobados = reprobados+1
			FinSi
			FinSi
		    5:Si nota5 >= 60 Entonces
			aprobados = aprobados+1
		    SiNo
			Si nota5 >= 60 Entonces
			reprobados = reprobados+1
			FinSi
		    FinSi
		    FinSegun
		    FinPara
            Escribir "cursos aprobados: " aprobados
            Escribir "cursos reprobados: " reprobados
		5: 
		6:escribir "aca esta el listado de los cursos"
		 para i = 1 Hasta total Hacer
		 segun i Hacer
		    1:escribir "curso " curso1 " nota de: " nota1
		    2:escribir "curso " curso2 " nota de: " nota2
		    3:escribir "curso " curso3 " nota de: " nota3
			4:escribir "curso " curso4 " nota de: " nota4
			5:escribir "curso " curso5 " nota de: " nota5
				FinSegun
			FinPara
		   Escribir "esta listo para enviar (s/n)"
		   Leer enviar
		   si enviar = "s" Entonces
			   Escribir "datos enviados"
		   SiNo
			   si enviar = "n" Entonces
				   Escribir "revise y corriga hasta que este segur@"
			   FinSi
		   FinSi
FinSegun
Hasta Que menu = 7
FinAlgoritmo
