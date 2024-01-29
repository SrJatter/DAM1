# Importar la biblioteca necesaria
import requests

# Definir la URL de una página HTML
htmlUrl = "https://www.eltiempo.es/gava.html"

# Realizar una solicitud GET a la página HTML y almacenar la respuesta en 'respostaHtml'
respostaHtml = requests.get(htmlUrl)

# Imprimir la respuesta HTML
print("------- RESPOSTA HTML ---------")
print(respostaHtml.text)
print()

# Definir la URL de una API REST para obtener datos meteorológicos de un municipio específico
restUrl = "https://www.el-tiempo.net/api/json/v1/provincias/08/municipios/08089/weather"

# Realizar una solicitud GET a la API REST y almacenar la respuesta en 'respostaREST'
respostaREST = requests.get(restUrl)

# Imprimir la respuesta JSON de la API REST
print("------- RESPOSTA REST ---------")
print(respostaREST.text)
print()
