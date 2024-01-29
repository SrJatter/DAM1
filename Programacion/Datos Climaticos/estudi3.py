import requests
import json
import matplotlib.pyplot as plt

def es_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def show():
    mounths = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    year1 = 2012
    m_days1 = es_bisiesto(year1)
    api_url1 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={year1}-01-01&end_date={year1}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
    response1 = requests.get(api_url1)
    dades1 = json.loads(response1.text)
    day = 0
    tempdic1 = {"max": [], "min": []}
    for i in range(12):
        tempMax1 = dades1["daily"]["temperature_2m_max"][day]
        tempMin1 = dades1["daily"]["temperature_2m_min"][day]
        for j in range(m_days1[i]):
            if tempMax1 < dades1["daily"]["temperature_2m_max"][day]:
                tempMax1 = dades1["daily"]["temperature_2m_max"][day]
            if tempMin1 > dades1["daily"]["temperature_2m_min"][day]:
                tempMin1 = dades1["daily"]["temperature_2m_min"][day]
            day += 1
        tempdic1["max"].append(tempMax1)
        tempdic1["min"].append(tempMin1)

    year2 = 2023
    m_days2 = es_bisiesto(year2)
    api_url2 = f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={year2}-01-01&end_date={year2}-12-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
    response2 = requests.get(api_url2)
    dades2 = json.loads(response2.text)
    day = 0
    tempdic2 = {"max": [], "min": []}
    for i in range(12):
        tempMax2 = dades2["daily"]["temperature_2m_max"][day]
        tempMin2 = dades2["daily"]["temperature_2m_min"][day]
        for j in range(m_days2[i]):
            if tempMax2 < dades2["daily"]["temperature_2m_max"][day]:
                tempMax2 = dades2["daily"]["temperature_2m_max"][day]
            if tempMin2 > dades2["daily"]["temperature_2m_min"][day]:
                tempMin2 = dades2["daily"]["temperature_2m_min"][day]
            day += 1
        tempdic2["max"].append(tempMax2)
        tempdic2["min"].append(tempMin2)

    fig, ax = plt.subplots()
    ax.plot(tempdic1["max"], label=f'Temp. Máx. & Min. {year1}', color='red')
    ax.plot(tempdic2["max"], label=f'Temp. Máx. & Min. {year2}', color='green')
    ax.plot(tempdic1["min"], color='red')
    ax.plot(tempdic2["min"], color='green')
    ax.set_xticks(range(len(mounths)))
    ax.set_xticklabels(mounths)
    plt.xlabel('Meses')
    plt.ylabel('Temperatura')
    plt.title(f'Comparacion de temperaturas maximas y minimas de Gavá de {year1} y {year2}')
    plt.legend()
    plt.xticks(rotation=45, ha='right')
    plt.show()

