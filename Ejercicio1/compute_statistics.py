"""
Docstring for Compute_Statistics
"""
from pathlib import Path
import os
import sys
import time

def numero_valido(numero):
    """Metodo para validar si es un numero"""
    try:
        float(numero)
        return True
    except ValueError:
        print(f"El valor '{numero}' no es un número válido.")
        return False

def registrar_resultado(lista_resultados):
    """Metodo para registrar los resultados en un archivo"""
    # Definir la ruta del archivo dentro del contenedor
    # Nota: /app/datos es el volumen que mapearemos
    output_dir = "/app/datos"
    filename = os.path.join(output_dir, "StatisticsResults.txt")

    # Crear el directorio si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Escribir valores
    with open(filename, "w", encoding="utf-8") as archivo_resultado:
        for resultado in lista_resultados:
            archivo_resultado.write(f"{resultado}\n")

script_location = Path(__file__).parent
ARCHIVO = 'FileWithData.txt'

file_location = script_location / ARCHIVO
print(file_location)

datos = []
try:
    with open(file_location, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Limpiar saltos de línea y convertir a número
            if numero_valido(linea.strip()):
                datos.append(float(linea.strip()))
except FileNotFoundError:
    print("El archivo datos.txt no fue encontrado.")
    sys.exit(1)

N = len(datos)
if N == 0:
    print("El archivo está vacío.")
    sys.exit(1)

#print(f"Datos: {datos}")

START_TIME = time.time()
# --- Algoritmos Básicos ---
# Calculo Media (Promedio)
SUMA = 0
for x in datos:
    SUMA += x
MEDIA = SUMA / N

# Calculo Medianan

# Calculo Mediana
# Primero necesitamos ordenar la lista (algoritmo burbuja simple)
DATOS_ORDENADOS = sorted(datos)
if N % 2 == 0:
    # Si es par, promedio de los dos centrales
    MEDIANA = (DATOS_ORDENADOS[N//2 - 1] + DATOS_ORDENADOS[N//2]) / 2
else:
    # Si es impar, el valor central
    MEDIANA = DATOS_ORDENADOS[N//2]

# Calculo Moda
frecuencias = {}
for x in datos:
    if x in frecuencias:
        frecuencias[x] += 1
    else:
        frecuencias[x] = 1

MAX_FRECUENCIA = 0
MODA = None
for x, frecuencia in frecuencias.items():
    if frecuencia > MAX_FRECUENCIA:
        MAX_FRECUENCIA = frecuencia
        MODA = x

# Calculo Varianza (Muestral n-1)
SUMA_CUADRADOS = 0
for x in datos:
    SUMA_CUADRADOS += (x - MEDIANA) ** 2
varianza = SUMA_CUADRADOS / (N - 1)

# Calculo Desviación Estándar
desviacion_estandar = varianza ** 0.5  # Raíz cuadrada

END_TIME = time.time()
EXECUTION_TIME = END_TIME - START_TIME

print("-" * 30)
print("Resultados Estadísticos:")
print(f"Media: {MEDIA:.2f}")
print(f"Mediana: {MEDIANA:.2f}")
print(f"Moda: {MODA} (se repite {MAX_FRECUENCIA} veces)")
print(f"Varianza: {varianza:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
print(f"Tiempo de ejecución: {EXECUTION_TIME:.5f} segundos")
print("-" * 30)

MEDIA_STR = f"Media: {MEDIA:.2f}"
MEDIANA_STR = f"Mediana: {MEDIANA:.2f}"
MODA_STR = f"Moda: {MODA} (se repite {MAX_FRECUENCIA} veces)"
MAX_FRECUENCIA_STR = f"Máxima frecuencia: {MAX_FRECUENCIA:.2f}"
VARIANZA_STR = f"Varianza: {varianza:.2f}"
DE_STR = f"Desviación Estándar: {desviacion_estandar:.2f}"
EXECUTION_TIME_STR = f"Tiempo de ejecución: {EXECUTION_TIME:.5f} segundos"

resultados = [
    MEDIA_STR, MEDIANA_STR,
    MODA_STR, MAX_FRECUENCIA_STR,
    VARIANZA_STR, DE_STR, EXECUTION_TIME_STR
]
registrar_resultado(resultados)
