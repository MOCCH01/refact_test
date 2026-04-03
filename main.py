from analizador_poblacion import AnalizadorPoblacion

analizador = AnalizadorPoblacion("poblacion_colombia.csv")

total = analizador.calcular_poblacion_total()
dpto, poblacion = analizador.obtener_dpto_mas_poblado()

print(f"Población total: {total}")
print(f"Departamento más poblado: {dpto} ({poblacion})")
