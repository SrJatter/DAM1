import requests
import json
import matplotlib.pyplot as plt

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365
def show():
    syear = 1970
    eyear = 2020
    api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={syear}-01-01&end_date={eyear}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
    response = requests.get(api_url)
    dades = json.loads(response.text)
    precipitation = dades["daily"]["precipitation_sum"]
    preclist = []
    day = 0

    for i in range(syear, eyear + 1):
        total_precipitation = 0
        for j in range(es_bisiesto(i)):
            total_precipitation += precipitation[day]
            day += 1
        preclist.append(total_precipitation)

    fig, ax = plt.subplots()
    ax.bar(range(len(preclist)), preclist, label='Precipitación')
    ax.set_xticks(range(len(preclist)))
    ax.set_xticklabels(range(syear, eyear + 1))
    plt.xlabel('Año')
    plt.ylabel('Precipitación')
    plt.title('Precipitación anual en Gavà')
    plt.legend()
    plt.xticks(rotation=45, ha='right')

    plt.show()
