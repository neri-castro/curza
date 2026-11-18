def clasificar_archivos_var_log(archivos, tamano_max_mb):
    comprimir = []
    espacio_recuperable = 0

    for nombre, tamano_mb in archivos:
        if nombre.endswith(".log") and tamano_mb >= tamano_max_mb:
            comprimir.append(nombre + ".gz")
            espacio_recuperable += int(tamano_mb * 0.7)

    return comprimir, espacio_recuperable


directorio_log = [
    ("syslog.log", 50),
    ("auth.log", 12),
    ("kern.log.gz", 80),
    ("apache_access.log", 100),
    (" notas.txt", 40),
]

nuevos_gz, ahorro_mb = clasificar_archivos_var_log(directorio_log, 30)
print("Archivos a comprimir:", nuevos_gz)
print("Ahorro estimado (MB):", ahorro_mb)