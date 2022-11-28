from bs4 import BeautifulSoup
from requests import get
import dateparser
from model import *


headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

for i in range(1, 94):
    URL = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273"
    response = get(URL, headers=headers)
    text=response.text
    soup = BeautifulSoup(text, 'lxml')
    apartment = soup.find_all('div', class_='search-item')
    for item in apartment:
    
        date_posted = item.find(class_='date-posted').text
        if '/' in date_posted:
            date_posted
        else:
            date_posted=date_posted.replace("<", "")
            date_posted = dateparser.parse(date_posted)
            date_posted = date_posted.strftime("%d/%m/%Y")  
        price = item.find(class_='price').text.strip()
        if price=='Please Contact':
            price=price
            currency="None"
        else:
            currency = price[:1]  
            price = price[1::] 
        image = item.find("img").get("data-src")
        image = image if image else "None"
    

        Data.create(
        date_posted=date_posted,
        price=price,
        currency=currency,
        image=image
        )








