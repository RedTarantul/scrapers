import requests 
import csv
from bs4 import BeautifulSoup
import re

#Open csv
with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper4\\items.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "Название организации",
            "Адрес",
            "Почта",
            "Номер телефона",
            "Информация об организации"
        )
    )

#Checking page count
response = requests.get("https://www.ricsfirms.com/umbraco/api/surveyorSearchApi/results?location=&firmName=Scotland&lon=&lat=&boxId=&showAllOffices=true")
dct = response.json()
page_count = dct["pageCount"]

#Get json
for i in range(1, page_count+1):
    url = f'https://www.ricsfirms.com/umbraco/api/surveyorSearchApi/results?location=&firmName=Scotland&lon=&lat=&boxId=&page={i}&showAllOffices=true'
    response = requests.get(url)
    data = response.json()["resultOffices"]

    #Get items
    for item in data:
        with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper4\\items.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    item["firmName"],
                    item["address"],
                    item["email"],
                    item["telephone"],
                    item["aboutUsInformation"]
                )
            )









