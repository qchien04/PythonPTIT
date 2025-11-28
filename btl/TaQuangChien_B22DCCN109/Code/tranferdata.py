from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
from bs4 import BeautifulSoup
from object import Tranfer
import os


def changePriceToNumber(price):
    if price == "Free": 
        return 0
    if price[-1] == 'K':
        return int(float(price[1:-1]) * 1000)
    elif price[-1] == 'M':
        return int(float(price[1:-1]) * 1000000)
    return int(price[1:])

def getTranferFromWeb(page_numbers, idTable, results):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        for page in page_numbers:
            url = f"https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/{page}"
            driver.get(url)
            time.sleep(5)

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            # player
            tbody = soup.find('tbody', id=idTable)
            tr_list = tbody.find_all('tr')
            for tr in tr_list:
                tdName = tr.find('td')

                spanName = tdName.find('span')
                name = spanName.text
                price = tr.find_all('td')[-1].text

                #link
                link=''
                a=tdName.find('a', recursive=True)
                if a!=None:
                    link=a['href']
                
                    
                results.append(Tranfer(name, changePriceToNumber(price),link))
            print(f"Finish Page {page}")
    finally:
        driver.quit()

idTable = "player-table-body"
list_result = []
threads = []
PAGE_QUANTITY = 18  # Tổng số trang
PAGES_PER_THREAD = 5  # Số trang mỗi luồng xử lý

# Tạo các luồng, mỗi luồng sẽ xử lý 3 trang
for i in range(0, PAGE_QUANTITY, PAGES_PER_THREAD):
    page_numbers = range(i + 1, min(i + PAGES_PER_THREAD + 1, PAGE_QUANTITY + 1))
    thread = threading.Thread(target=getTranferFromWeb, args=(page_numbers, idTable, list_result))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

print("Get data success")
print(len(list_result))


def getStatPlayer(startIndex,endIndex,tranferList):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for i in range(startIndex,endIndex+1):
        try:
            url_raw=tranferList[i].statLink
            if url_raw=='': 
                continue
            url = url_raw + f"/stats"
            driver.get(url)
            time.sleep(2)

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')

            ETV_ul=soup.find('ul',class_='playerInfoTop-bar__list')
            averageETV=0
            ETV_li=ETV_ul.find_all('li', recursive=False)
            if len(ETV_li)==2:
                ETV_li=ETV_li[-1]
                ETV_range_raw=ETV_li.find_all('div', recursive=False)[1].text
                ETV_range_raw=ETV_range_raw.split(" – ")
                ETV_on=changePriceToNumber(ETV_range_raw[1])
                ETV_bottom=changePriceToNumber(ETV_range_raw[0])
                averageETV=(ETV_on+ETV_bottom)/2
            elif len(ETV_li)==1:
                div_text=ETV_li[0].find('div')
                if div_text.text!='Contract Until':
                    ETV_li=ETV_li[-1]
                    ETV_range_raw=ETV_li.find_all('div', recursive=False)[1].text
                    ETV_range_raw=ETV_range_raw.split(" – ")
                    ETV_on=changePriceToNumber(ETV_range_raw[1])
                    ETV_bottom=changePriceToNumber(ETV_range_raw[0])
                    averageETV=(ETV_on+ETV_bottom)/2


            skill=soup.find('div',class_='teamInfoTop-skill__skill')
            if skill!=None:
                skill=float(skill.text.strip().split()[1])
            else: skill=0
            pot=soup.find('div',class_='teamInfoTop-skill__pot')
            if pot!=None:
                pot=float(pot.text.strip().split()[1])
            else: pot=0
            matches_num=0
            minutes_play=0
            goals=0
            assists=0
            yellow_cards=0
            yellow_red_cards=0
            red_cards=0
            tbody = soup.find('tbody', id="all")
            tr_list=[]
            if tbody!=None:
                tr_list = tbody.find_all('tr',class_="total-bg bold")
            for tr in tr_list:
                td_list = tr.find_all('td')
                td_list[1].find('small').extract()

                matches_num+=int(td_list[1].text)
                minutes_play+=int(td_list[2].text)
                goals+=int(td_list[3].text)
                assists+=int(td_list[4].text)
                yellow_cards+=int(td_list[5].text)
                yellow_red_cards+=int(td_list[6].text)
                red_cards+=int(td_list[7].text)
            
            #lastTranfer
            url = url_raw + f"/transfer-history"
            driver.get(url)
            thtml_content = driver.page_source
            tsoup = BeautifulSoup(thtml_content, 'html.parser')
            time.sleep(1)
            lastTranfer=0
            table=tsoup.find('table', class_="full-width table table-striped table-hover ft-table player-transfer-history-table mb-0")
            if table!=None:
                ttbody=table.find('tbody')
                ttr=ttbody.find("tr")
                if ttr!=None:
                    ttd=ttr.find_all('td')
                    lastTranfer=changePriceToNumber(ttd[-1].find('span').text)

            tranferList[i].setAttr(skill,pot,averageETV,matches_num,minutes_play,goals,assists,yellow_cards,yellow_red_cards,red_cards,lastTranfer)
            
            print(f"Finish Page {i}")
        except:
            print("Exception at ",i)
    driver.quit()


NUMBEROFPLAYER=len(list_result)
PAGEPERTHREAD=120

threads = []
for i in range(0, NUMBEROFPLAYER, PAGEPERTHREAD):
    startIndex = i
    endIndex=min(i+PAGEPERTHREAD,NUMBEROFPLAYER)
    thread = threading.Thread(target=getStatPlayer, args=(startIndex, endIndex, list_result))
    threads.append(thread)
    thread.start()

# Chờ tất cả các luồng hoàn thành
for thread in threads:
    thread.join()

import pickle
file_path_tranfer=os.path.join(os.path.dirname(__file__), "tranfers.pkl")
with open(file_path_tranfer, "wb") as file:
    pickle.dump(list_result, file)

print("Get data success")


import json
import requests

form_data = {
    'orderBy': 'date_transfer',
    'orderByDescending': 1,
    'page': 1,
    'pages': 0,
    'pageItems': 500,
    'countryId': 'all',
    'season': 5847,
    'tournamentId': 31,
    'clubFromId': 'all',
    'clubToId': 'all',
    'transferFeeFrom': None,
    'transferFeeTo': None,
}
url = 'https://www.footballtransfers.com/en/transfers/actions/confirmed/overview'
res = requests.post(url, data=form_data)
file_slugAndAge = os.path.join(os.path.dirname(__file__), "slugAndAge.pkl")
if res.status_code == 200:
    json_data = res.json()
    import pickle
    name_slug_age=[]
    with open(file_slugAndAge, "wb") as file:
        for i in range(json_data['filter_records']):
            age=json_data['records'][i]['age']
            if age!=None and age.isdigit():
                age=int(age)
            else:age=0
            arr=[age,json_data['records'][i]['player_slug']]
            name_slug_age.append(arr)
        pickle.dump(name_slug_age,file)
else:
    print("Lỗi")

