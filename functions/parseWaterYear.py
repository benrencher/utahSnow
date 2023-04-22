import json
from ..common import day, month, waterYear

def parseWaterYear(year):
    newWaterYear = waterYear(year)
    dataByYear = json.load(open("../dataFiles/dataByYear.json"))
    data = dataByYear[year]
    months = dict()
    for date, swe in data:
        monthNumber = int(date[0:2])
        dayNumber = int(date[3:])
        if monthNumber not in months:
            newMonth = month(monthNumber)
            months[monthNumber] = newMonth
        months[monthNumber].parseDay(dayNumber, swe)

    newWaterYear.months = months


parseWaterYear("2021")