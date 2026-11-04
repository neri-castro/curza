"""Problema 4 - Duplicados y operaciones de conjuntos"""

asistencias = ["Brisa", "Abel", "Celeste", "Brisa", "Diego", "Abel"]
presentes = set(asistencias)           # elimina repetidos
inscriptos = {"Abel", "Diego", "Erika", "Fabi"}

print("Presentes sin repetir:", sorted(presentes))
print("Cantidad:", len(presentes))
print("Presentes e inscriptos (&):", sorted(presentes & inscriptos))
print("Todos los nombres (|):", sorted(presentes | inscriptos))
print("Inscriptos que faltaron (-):", sorted(inscriptos - presentes))
print("En uno solo de los grupos (^):", sorted(presentes ^ inscriptos))
