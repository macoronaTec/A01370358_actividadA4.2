# Comandos a ejecutar

|---------|-------------|
| `docker build -t actividad4.2.3 .` | Construye la el contenedor con la imagen. |
| `docker run --rm -v "C:\Maestría\Quinto-trimestre\Pruebas de software\Semana4\Proyecto\Ejercicio3\datos":/app/datos actividad4.2.3` | Ejecuta el contenedor con la imagen y genera el resultado. |

|nota: utilice docker desktop para ejecutar el contenedor.|
|nota: para cambiar la ruta de cargar la información del contenedor, actualizar la ruta estática de docker run del segundo parámetro -v.|
|nota: para ejecutar el scripto con python o pylint se debe actualizar el archivo Dockerfile de acuerdo al caso|
# Comando para ejecutar python al iniciar
#CMD ["python", "word_count.py"]
# Comando para ejecutar pylint al iniciar
CMD ["pylint", "word_count.py"]

|---------|-------------|