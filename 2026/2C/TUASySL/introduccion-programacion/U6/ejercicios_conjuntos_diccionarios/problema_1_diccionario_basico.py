"""Problema 1 - Operaciones básicas con un diccionario"""

equipo = {"nombre": "PC-Lab01", "ram_gb": 8, "so": "Debian"}

print("Cantidad de datos:", len(equipo))
print("Sistema operativo:", equipo["so"])
print("Disco (get):", equipo.get("disco"))   # None: no existe

equipo["ram_gb"] = 16                          # modificar
equipo["disco_gb"] = 256                       # insertar
equipo.update({"sede": "CURZAS", "estado": "activo"})

if "sede" in equipo.keys():
    print("La clave 'sede' existe")

del equipo["estado"]

for clave, valor in equipo.items():
    print(f"{clave}: {valor}")
