# Importar las bibliotecas necesarias
import json
import requests

# Definir la URL de la API REST que se va a consultar
restUrl = "https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"

# Realizar una solicitud GET a la API REST y almacenar la respuesta en 'respostaREST'
respostaREST = requests.get(restUrl)

# Convertir el texto de la respuesta JSON en un diccionario de Python usando json.loads
dades = json.loads(respostaREST.text)

# Imprimir el JSON formateado con sangrías para una mejor legibilidad
print("------- JSON FORMATEJAT ---------")
print(json.dumps(dades, indent=3))

# Imprimir información específica obtenida del JSON
print()

# Imprimir la fecha de elaboración del informe
print("Data d'elaboració de l'informe ", dades["elaborado"])

# Imprimir el nombre del municipio y la provincia
print("Municipi ", dades["nombre"], " a la província de ", dades["provincia"])

# Obtener la fecha de la primera predicción y mostrarla
print("Predicció per data ", dades["prediccion"]["dia"][0]["@attributes"]["fecha"])

# Obtener y mostrar la temperatura máxima para la primera predicción del día
print("Predicció: temperatura màxima: ", dades["prediccion"]["dia"][0]["temperatura"]["maxima"])

# Obtener y mostrar la temperatura mínima para la primera predicción del día
print("Predicció: temperatura mínima: ", dades["prediccion"]["dia"][0]["temperatura"]["minima"])
