# write your code here!
# coins = float(input())
# rub = 2.98
# rubname = 'RUB'
# ars = 0.82
# arsname = 'ARS'
# hnl = 0.17
# hnlname = 'HNL'
# aud = 1.9622
# audname = 'AUD'
# mad = 0.208
# madname = 'MAD'
# countries = [rub,ars,hnl,aud,mad]
# def convertation(a):
#     if a == rub:
#         print(f'I will get {a*coins} {rubname} from the sale of {coins} conicoins.')
#     if a == ars:
#         print(f'I will get {a*coins} {arsname} from the sale of {coins} conicoins.')
#     if a == hnl:
#         print(f'I will get {a*coins} {hnlname} from the sale of {coins} conicoins.')
#     if a == aud:
#         print(f'I will get {a*coins} {audname} from the sale of {coins} conicoins.')
#     if a == mad:
#         print(f'I will get {a*coins} {madname} from the sale of {coins} conicoins.')
#
# for i in countries:
#     convertation(i)

import requests
import json

cashusd = {}
casheur = {}
cashall = {}
currencies = []

usdall = requests.get(f'http://www.floatrates.com/daily/usd.json')
jsonusd = json.loads(usdall.text)
for key,value in jsonusd.items():
    cashusd[key] = value['rate']
eurall = requests.get(f'http://www.floatrates.com/daily/eur.json')
jsoneur = json.loads(eurall.text)
for key,value in jsoneur.items():
    casheur[key] = value['rate']

basecurrency = input()
getall = requests.get(f'http://www.floatrates.com/daily/{basecurrency}.json')
jsonall = json.loads(getall.text)

while True:
    currency = input()
    if currency == '':
        break
    amount = float(input())
    if currency == 'USD' or currency == 'EUR' or currency == 'usd' or currency == 'eur':
        print('Checking the cache...'
              'Oh! It is in the cache!')
        if currency == 'USD' or currency == 'usd':
            trueform = str(basecurrency.lower())
            convert = (amount/cashusd[trueform])
        elif currency == 'EUR' or currency == 'eur':
            trueform = str(basecurrency.lower())
            convert = (amount/casheur[trueform])
        print(f'You received {round(convert,2)} {currency}.')

    else:
        # getall = requests.get(f'http://www.floatrates.com/daily/{basecurrency}.json')
        # jsonall = json.loads(getall.text)
        # print(len(jsonall))
        # cashall = {}
        if len(cashall) > 0:
            for key in cashall:
                if key == currency:
                    convert = (cashall[currency]) * amount
                    currencies.append(currency)
                    print('Checking the cache...'
                          'Oh! It is in the cache!')
                    print(f'You received {round(convert,2)} {currency}.''')
                else:
                    pass
        if currency not in currencies:
            trueform = str(currency.lower())
            convert = (jsonall[trueform]['rate'])*amount
            print('Checking the cache...')
            print('Sorry, but it is not in the cache!')
            print(f'You received {round(convert,2)} {currency}.''')
            cashall[currency] = jsonall[trueform]['rate']
            # print(cashall)
            # cashall['lsl'] = 'try'
            # print(len(cashall))
    if len(cashall) == len(jsonall):
        break
