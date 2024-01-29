import requests
import json
import matplotlib.pyplot as plt


def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def calcular_precipitacion_anual(year):
    m_days = es_bisiesto(year)
    api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={year}-01-01&end_date={year}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
    response = requests.get(api_url)
    dades = json.loads(response.text)
    day = 0
    preclist = []
    for i in range(12):
        precsum = dades["daily"]["precipitation_sum"][day]
        for j in range(m_days[i]):
            precsum += dades["daily"]["precipitation_sum"][day]
            day += 1
        preclist.append(precsum)
    return preclist

def show():
    months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    sy = 1970
    ey = 2020
    year_prec = {}
    ty = 0
    for i in range(sy, ey+1, 10):
        year_prec[i] = calcular_precipitacion_anual(i)
        ty += 1

    bar_width = 0.9/ty
    bar_width_m = 0.9/ty
    fig, ax = plt.subplots()
    ax.bar(range(12), year_prec[sy], label=f'Precipitación {sy}', width=bar_width)
    for i in range(sy +10, ey+1, 10):
        bar_positions = []
        for j in range(12):
            position = j + bar_width_m
            bar_positions.append(position)
        ax.bar(bar_positions, year_prec[i], label=f'Precipitación {i}', width=bar_width)
        bar_width_m += 0.9/ty

    label_positions = []
    for i in range(12):
        position = i + bar_width / 2
        label_positions.append(position)
    ax.set_xticks(label_positions)
    ax.set_xticklabels(months)
    plt.xlabel('Meses')
    plt.ylabel('Precipitación')
    plt.title(f'Comparacion de precipitacion mensual en Gavà entre {sy} y {ey}')
    plt.legend()
    plt.show()
