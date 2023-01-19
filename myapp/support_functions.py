from urllib import request
from pandas.plotting import table
from myapp.models import Currency
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from myapp.models import *


def get_currency_list():
    currency_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "https://thefactfile.org/countries-currencies-symbols/"
    response = requests.get(url)
    if not response.status_code == 200:
        return currency_list
    soup = BeautifulSoup(response.content)
    data_lines = soup.find_all('tr')
    for line in data_lines:
        try:
            detail = line.find_all('td')
            currency = detail[2].get_text().strip()
            iso = detail[3].get_text().strip()
            if (currency, iso) in currency_list:
                continue
            currency_list.append((currency, iso))
        except:
            continue
    return currency_list


def add_currencies(currency_list):
    for currency in currency_list:
        currency_name = currency[0]
        currency_symbol = currency[1]
        try:
            c = Currency.objects.get(iso=currency_symbol)
        except:
            c = Currency(long_name=currency_name, iso=currency_symbol)
            c.save()  # To test out the code, replace this by print(c)
            print(c)


import requests
from bs4 import BeautifulSoup


def scrape_zodiac():
    zodiac_list = []
    import requests
    from bs4 import BeautifulSoup
    url = 'https://en.wikipedia.org/wiki/Zodiac#Twelve_signs'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all('td')
        sign = cols[0].text.strip()
        symbol = cols[1].text.strip()
        planet = cols[2].text.strip()
        element = cols[3].text.strip()
        quality = cols[4].text.strip()
        zodiac_list.append({"sign": sign, "symbol": symbol, "planet": planet, "element": element, "quality": quality})
    return zodiac_list

from .models import ZodiacSign

def add_zodiac(zodiac_list):
    for zodiac in zodiac_list:
        sign = zodiac["sign"]
        symbol = zodiac["symbol"]
        planet = zodiac["planet"]
        element = zodiac["element"]
        quality = zodiac["quality"]
        try:
            z = ZodiacSign.objects.get(symbol=symbol)
        except:
            z = ZodiacSign(sign=sign, symbol=symbol, planet=planet, element=element, quality=quality)
        z.sign = sign
        z.save()