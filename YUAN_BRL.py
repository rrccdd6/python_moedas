# -*- coding: utf-8 -*-

import requests

def get_yuan_price():
    url = "https://economia.awesomeapi.com.br/json/last/CNY-BRL"
    response = requests.get(url)
    data = response.json()
    if 'CNYBRL' in data:
        preco = float(data['CNYBRL']['bid'])
        mensagem = "O preço atual do yuan em reais é R${:.2f}".format(preco)
        return mensagem
    else:
        return "Desculpe, não foi possível obter o preço do yuan em reais no momento."

print(get_yuan_price())



#   python3.10 Moedas/YUAN_BRL.py