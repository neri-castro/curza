def analizar_procesos(tabla_procesos, limite_ram):
    por_usuario = {}
    pesados = []
    for pid, usuario, comando, ram_mb in tabla_procesos:
        por_usuario[usuario] = por_usuario.get(usuario, 0) + ram_mb
        if ram_mb > limite_ram:
            pesados.append((pid, comando))
    return por_usuario, pesados


procesos = [
    (101, "root", "systemd", 45),
    (204, "www-data", "apache2", 320),
    (205, "www-data", "apache2", 290),
    (310, "mysql", "mysqld", 850),
    (412, "root", "sshd", 25),
]

consumo_usuarios, alerta_procesos = analizar_procesos(procesos, 300)
print("RAM por usuario (MB):", consumo_usuarios)
print("Procesos que superan 300 MB:", alerta_procesos)