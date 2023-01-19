from urllib import request
from myapp.models import Currency
import requests
from bs4 import BeautifulSoup
from myapp.models import *
from django.shortcuts import render, redirect


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


from django.shortcuts import get_object_or_404
from .models import User1
def find_matching_user(name, horoscope):
    current_user = get_object_or_404(User1, name=name, horoscope=horoscope)
    matching_user = User1.objects.filter(horoscope=current_user.horoscope).exclude(name=current_user.name).first()
    return matching_user


