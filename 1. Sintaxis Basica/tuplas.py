#--------------- UNA TUPLA ES INMUTABLE, Y NO PERMITE REPETIR VALORES -------------------

mitupla=("Juan",21,1997)
#Convertir una tupla en una lista
milista=list(mitupla)
print(milista)

milista=("Camila",3,2014)
#Convertir una lista en una tupla
mitupla=tuple(mitupla)
print(mitupla)

#Saber cuantas veces esta cualquier elemento
print(mitupla.count("Juan"))

#Saber la longitud de una tupla
print(len(mitupla))

#Tupla unitaria
otra_tupla=("Juan",)

#Empaquetado de una Tupla
tupla_tres="Angie",20,1998

#Desempaquetado de una tupla
tupla_cuatro="Angie",20,1998
nombre,agno,nacimiento=tupla_cuatro
print(nombre)
print(agno)
print(nacimiento)

print(nacimiento)
