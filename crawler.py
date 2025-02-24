import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/sch/i.html?_nkw=notebook&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = soup.find_all('span', class_='s-item__price')

    with open('precos.txt', 'w') as file:
        for price in prices:
            file.write(price.text.strip() + '\n')

    print("Preços salvos com sucesso em 'precos.txt'.")

else:
    print("Falha ao acessar a página.")

