import requests
from bs4 import BeautifulSoup
import time
import json

cookies = {
    'BITRIX_SM_SALE_UID': '39632447',
    '_ga': 'GA1.2.2087058321.1685216698',
    '_gid': 'GA1.2.440518458.1685216698',
    'roistat_visit': '7399124',
    'roistat_first_visit': '7399124',
    'roistat_visit_cookie_expire': '1209600',
    '_ym_uid': '1685216699816536247',
    '_ym_d': '1685216699',
    'roistat_marker': 'seo_yandex_',
    'roistat_marker_old': 'seo_yandex_',
    '___dc': '4bc9507b-6827-4500-9521-1fce921e0994',
    'dark_mode': 'true',
    '_ym_isad': '2',
    'tmr_lvid': '7451f488d804c585b02c43db26090ce2',
    'tmr_lvidTS': '1685216703414',
    'BX_USER_ID': '1418223b581d514f35dbef172e891f4f',
    '_tt_enable_cookie': '1',
    '_ttp': 'nLVbdvNvfSOGqKeH7N62spExbyh',
    'roistat_call_tracking': '1',
    'roistat_emailtracking_email': 'null',
    'roistat_emailtracking_tracking_email': 'null',
    'roistat_emailtracking_emails': 'null',
    'cookie-modal': 'closed',
    'aa_v4_search': 'UEFHRU5fMT0zJg%3D%3D',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A4%2C%22EXPIRE%22%3A1685307540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    '_ym_visorc': 'w',
    'PHPSESSID': 'dhfvnFbPfDkuIoB0cDY15Ha48UiraabR',
    '_gat': '1',
    'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
    'tmr_detect': '0%7C1685287324338',
    'activity': '1|40',
}

headers = {
    'authority': 'shop.casio.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9,fr;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'BITRIX_SM_SALE_UID=39632447; _ga=GA1.2.2087058321.1685216698; _gid=GA1.2.440518458.1685216698; roistat_visit=7399124; roistat_first_visit=7399124; roistat_visit_cookie_expire=1209600; _ym_uid=1685216699816536247; _ym_d=1685216699; roistat_marker=seo_yandex_; roistat_marker_old=seo_yandex_; ___dc=4bc9507b-6827-4500-9521-1fce921e0994; dark_mode=true; _ym_isad=2; tmr_lvid=7451f488d804c585b02c43db26090ce2; tmr_lvidTS=1685216703414; BX_USER_ID=1418223b581d514f35dbef172e891f4f; _tt_enable_cookie=1; _ttp=nLVbdvNvfSOGqKeH7N62spExbyh; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; cookie-modal=closed; aa_v4_search=UEFHRU5fMT0zJg%3D%3D; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A4%2C%22EXPIRE%22%3A1685307540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_visorc=w; PHPSESSID=dhfvnFbPfDkuIoB0cDY15Ha48UiraabR; _gat=1; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails; tmr_detect=0%7C1685287324338; activity=1|40',
    'pragma': 'no-cache',
    'referer': 'https://shop.casio.ru/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36',
}

response = requests.get(
    'https://shop.casio.ru/catalog/filter/gender-is-male/apply/',
    cookies=cookies,
    headers=headers,
    verify=False,
)

with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper2\\index.html", "w", encoding="utf-8") as file:
    file.write(response.text)

with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper2\\index.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

page_count_block = soup.find("div", class_="bx-pagination-container").find_all("li")
page_count = int(page_count_block[-2].find("span").text)

lst = []
for i in range(1, page_count+1):
    cookies = {
    'PHPSESSID': '05RiJ2xK8vwcqpeIBzTWEK6cPv6u9qwq',
    'BITRIX_SM_SALE_UID': '39632447',
    '_ga': 'GA1.2.2087058321.1685216698',
    '_gid': 'GA1.2.440518458.1685216698',
    'roistat_visit': '7399124',
    'roistat_first_visit': '7399124',
    'roistat_visit_cookie_expire': '1209600',
    'roistat_is_need_listen_requests': '0',
    'roistat_is_save_data_in_cookie': '1',
    '_ym_uid': '1685216699816536247',
    '_ym_d': '1685216699',
    '_ym_visorc': 'w',
    'roistat_marker': 'seo_yandex_',
    'roistat_marker_old': 'seo_yandex_',
    '___dc': '4bc9507b-6827-4500-9521-1fce921e0994',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A22%2C%22EXPIRE%22%3A1685221140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    'dark_mode': 'true',
    '_ym_isad': '2',
    'tmr_lvid': '7451f488d804c585b02c43db26090ce2',
    'tmr_lvidTS': '1685216703414',
    'BX_USER_ID': '1418223b581d514f35dbef172e891f4f',
    '_tt_enable_cookie': '1',
    '_ttp': 'nLVbdvNvfSOGqKeH7N62spExbyh',
    'roistat_call_tracking': '1',
    'roistat_emailtracking_email': 'null',
    'roistat_emailtracking_tracking_email': 'null',
    'roistat_emailtracking_emails': 'null',
    'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_marker%2Croistat_marker_old%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
    'cookie-modal': 'closed',
    'aa_v4_search': 'UEFHRU5fMT0zJg%3D%3D',
    'tmr_detect': '0%7C1685218997108',
    '_gat': '1',
    'activity': '5|20',
    }

    headers = {
        'authority': 'shop.casio.ru',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9,fr;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=05RiJ2xK8vwcqpeIBzTWEK6cPv6u9qwq; BITRIX_SM_SALE_UID=39632447; _ga=GA1.2.2087058321.1685216698; _gid=GA1.2.440518458.1685216698; roistat_visit=7399124; roistat_first_visit=7399124; roistat_visit_cookie_expire=1209600; roistat_is_need_listen_requests=0; roistat_is_save_data_in_cookie=1; _ym_uid=1685216699816536247; _ym_d=1685216699; _ym_visorc=w; roistat_marker=seo_yandex_; roistat_marker_old=seo_yandex_; ___dc=4bc9507b-6827-4500-9521-1fce921e0994; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A22%2C%22EXPIRE%22%3A1685221140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; dark_mode=true; _ym_isad=2; tmr_lvid=7451f488d804c585b02c43db26090ce2; tmr_lvidTS=1685216703414; BX_USER_ID=1418223b581d514f35dbef172e891f4f; _tt_enable_cookie=1; _ttp=nLVbdvNvfSOGqKeH7N62spExbyh; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_marker%2Croistat_marker_old%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails; cookie-modal=closed; aa_v4_search=UEFHRU5fMT0zJg%3D%3D; tmr_detect=0%7C1685218997108; _gat=1; activity=5|20',
        'origin': 'https://shop.casio.ru',
        'pragma': 'no-cache',
        'referer': 'https://shop.casio.ru/catalog/filter/gender-is-male/apply/?PAGEN_1=1',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'PAGEN_1': f'{i}',
    }

    data = {
        'exclude[]': [
            '77983',
            '75431',
            '95445',
            '95448',
            '97361',
            '94576',
            '94577',
            '97862',
            '97594',
            '81349',
            '71948',
            '71949',
            '97844',
            '97845',
            '72163',
            '72166',
            '72194',
            '72358',
            '72359',
            '72413',
            '72414',
            '72460',
            '97113',
            '95960',
            '97086',
            '97846',
            '81358',
            '83116',
            '83115',
            '97848',
            '97849',
        ],
    }

    response = requests.post(
        'https://shop.casio.ru/catalog/filter/gender-is-male/apply/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    soup = BeautifulSoup(response.text, "lxml")
    blocks = soup.find_all("div", class_="product-item carousel-item")
    
    for i in blocks:
        lst.append(i.get("data-analitics"))

lst2 = []
for i in lst:
    for_json = i.replace("'", '"')
    dt = json.loads(for_json)
    lst2.append(dt)

with open("C:\\Users\\REnATIK\\Desktop\\Hack\\python proj\\scraper2\\items.json", "w", encoding="utf-8") as file:
    json.dump(lst2, file, ensure_ascii=False, indent=4)
    


