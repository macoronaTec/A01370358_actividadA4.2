"""
Docstring for Converter
"""
from pathlib import Path
import os
import sys
import time

def convertir_decimal_a_binario(n):
    """Metodo para convertir un numero decimal a binario"""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

def convertir_decimal_a_hexadecimal(n):
    """Metodo para convertir un numero decimal a hexadecimal"""
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        n = n // 16
    return hexadecimal

def registrar_resultado(lista_resultados):
    """Metodo para registrar los resultados en un archivo"""
    # Definir la ruta del archivo dentro del contenedor
    # Nota: /app/datos es el volumen que mapearemos
    output_dir = "/app/datos"
    filename = os.path.join(output_dir, "ConvertionResults.txt")

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

resultados = []
TOTAL_ERRORES = 0

try:
    with open(file_location, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Error: No se pudo abrir el archivo {file_location}")
    sys.exit(1)

start_time = time.time()

for line_number, line in enumerate(lines, start=1):
    line = line.strip()

    if line == "":
        print(f"Advertencia (línea {line_number}): línea vacía")
        TOTAL_ERRORES += 1
        continue

    try:
        number = int(line)
        if number < 0:
            raise ValueError("Número negativo")

        BINARY = convertir_decimal_a_binario(number)
        HEXADECIMAL = convertir_decimal_a_hexadecimal(number)

        RESULTADO = f"Decimal: {number} | Binario: {BINARY} | Hexadecimal: {HEXADECIMAL}"
        print(RESULTADO)
        resultados.append(RESULTADO)

    except ValueError:
        print(f"Error (línea {line_number}): dato no válido -> '{line}'")
        TOTAL_ERRORES += 1
        continue

end_time = time.time()
elapsed_time = end_time - start_time

time_info = f"\nTiempo total de ejecución: {elapsed_time:.6f} segundos"
ERROR_INFO = f"Total de errores detectados: {TOTAL_ERRORES}"

print(time_info)
print(ERROR_INFO)

resultados.append(time_info)
resultados.append(ERROR_INFO)

registrar_resultado(resultados)
