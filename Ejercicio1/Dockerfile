# Usar una imagen oficial ligera de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

VOLUME /app/datos

# Instalar pylint
RUN pip install --no-cache-dir pandas pylint

# Copiar el script al contenedor
#COPY computeStatistics.py .
COPY . .

# Comando para ejecutar el script
#CMD ["python", "compute_statistics.py"]
# Comando para ejecutar pylint al iniciar
CMD ["pylint", "compute_statistics.py"]