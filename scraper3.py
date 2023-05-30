import requests
import json

json_lst =[]
for i in range(1, 2):
    url = f"https://s3.landingfolio.com/inspiration?page={i}&sortBy=free-first"
    response = requests.get(url)
    data = json.loads(response.text)

    for item in data:
        dct = {
            "title": item["title"],
            "url": item["url"]
        }

        lst_images = []
        for images in item["screenshots"]:
            lst = images["images"].values()
            for j in lst:
                url_for_img = "https://landingfoliocom.imgix.net/"
                lst_images.append(f"{url_for_img}{j}")

        dct["images"] = lst_images
        json_lst.append(dct)

with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper3\\items.json", "w", encoding="utf-8") as file:
    json.dump(json_lst, file, ensure_ascii=False, indent=4)




