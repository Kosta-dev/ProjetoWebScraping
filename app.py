import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todos_textos = dados_pagina.find_all('a', class_='_flex actTriggerGA')

for a in todos_textos:
    clima = a.find('h4', class_='-gray-dark-2 -font-base -bold').text
    print(clima)