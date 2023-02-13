import requests

url = 'https://sapi.xt.com/v4/public/trade/history/'
headers = {
    'Content-Type': 'application/json'
}
parameters = {
    'symbol': 'btc_usdt',
    'direction': 'NEXT',
}
response = requests.get(url=url, headers=headers, params=parameters)
response.encoding = 'utf-8'
print(response.text)
