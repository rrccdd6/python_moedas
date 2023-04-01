# -*- coding: utf-8 -*-


import requests
import json

ticker = 'AESB3F.SA'

url = 'https://query1.finance.yahoo.com/v7/finance/quote?symbols={}'.format(ticker)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

price = data['quoteResponse']['result'][0]['regularMarketPrice']

print('O preço da ação é: {:.2f}'.format(price))


#AESB3F
#VALE3F
#PETR3F


###     python3.10 Moedas/preco_da_acao.py