import fastf1
import pandas as pd
import os

# Habilitar cach�
if not os.path.exists("cache"):
    os.makedirs("cache")
fastf1.Cache.enable_cache("cache")

a�o = 2026
# Lista de las carreras de la temporada
carreras = ["Bahrain", "Saudi Arabia", "Australia", "Japan", "China", "Miami", "Emilia Romagna", "Monaco", "Canada", "Spain"]
sesion_tipo = "R"

# Tabla vac�a maestra
df_temporada = pd.DataFrame() 

print("Iniciando descarga masiva de la temporada...")

# El ciclo que automatiza la extracci�n carrera por carrera
for gran_premio in carreras:
    print(f"Descargando datos del GP de {gran_premio}...")
    try:
        session = fastf1.get_session(a�o, gran_premio, sesion_tipo)
        session.load()
        resultados = session.results
        
        columnas_clave = ["Abbreviation", "DriverNumber", "FullName", "TeamName", "Position", "Points"]
        df_limpio = resultados[columnas_clave].copy() 
        
        # Etiqueta vital para no revolver los datos en Tableau
        df_limpio["Race"] = gran_premio
        
        # Unir a la tabla maestra
        df_temporada = pd.concat([df_temporada, df_limpio])
        
    except Exception as e:
        print(f"Error al descargar {gran_premio}: {e}")

# Exportar el Mega CSV
nombre_archivo = f"resultados_temporada_completa_{a�o}.csv"
df_temporada.to_csv(nombre_archivo, index=False)

print(f"\n��xito total! Archivo maestro creado: {nombre_archivo}")