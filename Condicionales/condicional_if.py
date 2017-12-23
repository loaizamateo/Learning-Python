###########################
# Condicional: If

#Realizamos una funcion que evalue si con la nota aprueba o reprueba
def evaluacion(nota):
    valoracion="Aprobado"
    if nota<3:
        valoracion="Reprobado"
    return valoracion

print(evaluacion(3))

###########################
#Introduccion de valor de nota por teclado
print("Evaluacion de notas de alumnos")
notaAlumno=input("Cual es su nota?: ")

print(evaluacion(int(notaAlumno)))
