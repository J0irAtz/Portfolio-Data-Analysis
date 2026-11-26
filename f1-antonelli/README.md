# Fórmula 1 · Seguimiento de Kimi Antonelli

Proyecto de Jair Alfaro. Dos extractores de Python obtienen resultados de carrera con FastF1 y pandas y generan CSV para analizarlos en Tableau.

## Corte disponible

El CSV agregado contiene 132 registros de pilotos en seis Grandes Premios de 2026: Australia, Japón, China, Miami, Mónaco y Canadá. El archivo de Canadá contiene 22 registros. En ese corte, Antonelli figura primero con 25 puntos en Canadá.

El nombre original del CSV agregado se conserva para facilitar la conexión con Tableau. Su cobertura corresponde a seis carreras. El extractor intenta consultar diez eventos y registra las excepciones en consola. La causa de cada ausencia del corte histórico quedó sin confirmar.

## Reproducir la extracción

Con Python 3, instala las dependencias con `python -m pip install fastf1 pandas`. En una carpeta de trabajo con ambos scripts, ejecuta `python extractor_f1.py` para Canadá o `python extractor_temporada.py` para los eventos configurados. Las consultas requieren acceso a Internet y los scripts escriben sus CSV en el directorio actual. Conserva una copia del corte incluido si quieres comparar futuras extracciones.

## Visualización

[Ver el dashboard interactivo en Tableau Public](https://public.tableau.com/app/profile/jair.eduardo.alfaro.ahuatzin/viz/Dashboard_F1_Antonelli/Dashboard1). Incluye una gráfica de puntos acumulados de Kimi Antonelli y una comparación de los resultados del GP de Canadá.
