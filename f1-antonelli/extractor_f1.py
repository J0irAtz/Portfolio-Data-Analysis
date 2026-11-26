import fastf1
import pandas as pd
import os

#Habilitar la carpeta de cach� para no descargar mis datos pesados cada vez
if not os.path.exists("cache"):
    os.makedirs("cache")
fastf1.Cache.enable_cache("cache")

#Definir la carrera a analizar
a�o = 2026
gran_premio = "Canada"

sesion_tipo = "R" # 'R' es de Race (Carrera)

print(f"Conectando a los servidores de F1 para el GP de {gran_premio} {a�o}...")
session = fastf1.get_session(a�o, gran_premio, sesion_tipo)
session.load()

# Extraer resultados
resultados = session.results

# Limpieza b�sica para Tableau (Son dos l�neas separadas)
columnas_clave = ["Abbreviation", "DriverNumber", "FullName", "TeamName", "GridPosition", "Position", "Points"]
df_limpio = resultados[columnas_clave]

# Exportar a CSV
nombre_archivo = f"resultados_{gran_premio}_{a�o}.csv"
df_limpio.to_csv(nombre_archivo, index=False)