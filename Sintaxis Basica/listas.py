#Creamos una lista y posteriormente la mostramos.
#El ":" en miLista[:] es para mostrar todo
miLista=["Juan","Pepe","Martha"]
print(miLista[:])

# .append es para agregar un nuevo elemento a la lista
miLista.append("Carlos")
print(miLista[:])

# .insert es para agregar un nuevo elemento a la lista pero en una posición especifica.
miLista.insert(2,"Fernando")
print(miLista[:])

# .extend sirve para agregar varios elementos a la lista.
miLista.extend(["Maria","Joaquina","Camilia"])
print(miLista[:])

# .remove elimina un elemento en especifico.
miLista.remove("Fernando")
print(miLista[:])

# [elemento] in [Vector] es para comprobar si existe dicho elemento en la lista.
print("Maria" in miLista)

# .pop elimina el ultimo elemento de la lista.
miLista.pop()
print(miLista[:])
