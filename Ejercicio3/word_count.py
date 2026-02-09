"""
Docstring for Word Count
"""
from pathlib import Path
import os
import sys
import time

def revisar_palabra(palabra):
    """metodo que revisa que las palabras son validas"""
    resultado = ""
    for caracter in palabra:
        #Obtener el valor ASCII
        codigo = ord(caracter)
        #mayúsculas a minúsculas (65-90 -> 97-122)
        if 65 <= codigo <= 90:
            resultado += chr(codigo + 32)
        #Mantener letras minúsculas (97-122)
        elif 97 <= codigo <= 122:
            resultado += caracter
        else:
            print(f"Dato no válido ignorado: '{caracter}'")
            continue
    return resultado

def registrar_resultado(lista_resultados, frecuencia_palabra, tiempo):
    """Metodo para registrar los resultados en un archivo"""
    # Definir la ruta del archivo dentro del contenedor
    # Nota: /app/datos es el volumen que mapearemos
    output_dir = "/app/datos"
    filename = os.path.join(output_dir, "WordCountResults.txt")

    # Crear el directorio si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Escribir valores
    with open(filename, "w", encoding="utf-8") as archivo_resultado:
        for indice, palabra in enumerate(lista_resultados):
            line = f"Palabra: {palabra} | Frecuencia: {frecuencia_palabra[indice]}"
            archivo_resultado.write(line + "\n")
        line = f"Tiempo de ejecución: {tiempo:.6f} segundos"
        archivo_resultado.write(line + "\n")

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

words = []
frequencies = []
start_time = time.time()
CURRENT_WORD = ""

for CURRENT_WORD in lines:
    if CURRENT_WORD.strip() != "":
        word = revisar_palabra(CURRENT_WORD.strip())
        #print(word)
        if len(words) == 0:
            words.append(word)
            frequencies.append(1)
            CURRENT_WORD = ""
        else:
            for i, elemento in enumerate(words):
                #print(f"Comparando : '{words[i]}' con '{word}'")
                #if words[i] == word:
                if word == elemento:
                    frequencies[i] += 1
                    #print(f"Se aumenta la frecuencia de la palabra: '{word}'")
                    break

                if word not in words:
                    #print(f"Se agrega la palabra: '{word}'")
                    words.append(word)
                    frequencies.append(1)

                CURRENT_WORD = ""
    else:
        print(f"Dato no válido ignorado: '{CURRENT_WORD.strip()}'")
        CURRENT_WORD = ""

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")

registrar_resultado(words, frequencies, elapsed_time)
