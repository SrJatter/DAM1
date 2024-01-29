# Importar las bibliotecas necesarias
import requests
import json
import matplotlib.pyplot as plt

# Definir la URL de la API para obtener datos meteorológicos de diciembre de 2022
api_url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date=2022-12-01&end_date=2022-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"

# Realizar una solicitud GET a la API y almacenar la respuesta en 'response'
response = requests.get(api_url)

# Convertir el texto de la respuesta JSON en un diccionario de Python usando json.loads
dades = json.loads(response.text)

# Extraer las temperaturas máximas, mínimas y la cantidad de precipitación diaria
tempMax = dades["daily"]["temperature_2m_max"]
tempMin = dades["daily"]["temperature_2m_min"]
pluja = dades["daily"]["precipitation_sum"]

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Trazar la temperatura máxima
ax.plot(dades["daily"]["time"], tempMax, label='Temp. Máxima')

# Trazar la temperatura mínima
ax.plot(dades["daily"]["time"], tempMin, label='Temp. Mínima')

# Crear un gráfico de barras para la precipitación
ax.bar(dades["daily"]["time"], pluja, label='Precipitación')

# Añadir etiquetas y leyenda
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.title('Datos meteorológicos de diciembre de 2022')
plt.legend()

# Rotar las etiquetas del eje x para mayor legibilidad
plt.xticks(rotation=45, ha='right')

# Mostrar el gráfico
plt.show()
