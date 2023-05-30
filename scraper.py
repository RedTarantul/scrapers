import requests
from bs4 import BeautifulSoup
import json 

#url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#response = requests.get(url)

#with open(r"C:\Users\REnATIK\Desktop\Hack\python proj\scraper\index.html", "w", encoding="utf-8") as file:
#    file.write(response.text)

with open(r"C:\Users\REnATIK\Desktop\Hack\python proj\scraper\index.html", "r", encoding="utf-8") as file:
    html = BeautifulSoup(file.read(), "lxml")

url = "https://health-diet.ru"

#Все ссылки на продукты
elements = html.find_all(class_ = "mzr-tc-group-item-href")
dct = {}
for i in elements:
    href = i["href"]
    dct[i.string] = f"{url}{href}"

#Создание словаря
for title, url in dct.items():
    json_dict = {}
    if url == dct["Danone"]:
        continue
    else:   
        response = requests.get(url)
        html = BeautifulSoup(response.text, "lxml")

        table = html.tbody
        elements = table.find_all("tr")

        lst = []
        for i in elements:
            lst2 = []
            cells = i.find_all("td")
            for j in cells:
                if j.string: lst2.append(j.string)
                else: lst2.append(j.a.string)
            lst.append(lst2)
            print(lst2)
            
        for i in lst:
            json_dict[i[0]] = {
                "калории": i[1],
                "белки": i[2],
                "жиры": i[3],
                "углеводы": i[4]
            }
        
    with open(f"C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper\\table\\{title}.json", "w", encoding="utf-8") as file:
        json.dump(json_dict, file, ensure_ascii=False, indent=4)



