# -*- coding: utf-8 -*-
import dbf

ARCHIVO_DBF = r"C:\Users\Anibal\Sistema\Encabeza.dbf"

tabla = dbf.Table(ARCHIVO_DBF)
tabla.open(mode=dbf.READ_ONLY)

print("=== ESTRUCTURA DE CAMPOS (%s) ===" % ARCHIVO_DBF)
for nombre in tabla.field_names:
    info = tabla.field_info(nombre)
    print(" - %-12s | Tipo: %s | Longitud: %s | Decimales: %s" % (
        nombre, info.field_type, info.length, info.decimal
    ))

print("\n=== REGISTROS (%d en total) ===" % len(tabla))
for idx, reg in enumerate(tabla):
    estado = "BORRADO" if dbf.is_deleted(reg) else "ACTIVO"
    print("\n--- Registro #%d [%s] ---" % (idx + 1, estado))
    for nombre in tabla.field_names:
        valor = reg[nombre]
        if isinstance(valor, str):
            valor = valor.decode("latin1", "replace").strip()
        print("  %-12s : %r" % (nombre, valor))

tabla.close()