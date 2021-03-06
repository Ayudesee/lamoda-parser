import json

from bs4 import BeautifulSoup
from kafka import KafkaProducer
import requests


url = 'https://www.lamoda.by/c/17/shoes-men/?sitelink=topmenuM&l=3'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
products = soup.find_all('div', class_='x-product-card-description__microdata-wrap')
producer = KafkaProducer(bootstrap_servers='localhost:9093', value_serializer=lambda m: json.dumps(m).encode())

for prd in products:
    # print(prd)
    # print(prd.find_all('span', class_='x-product-card-description__price-new'))
    # print(prd.find_all('span', class_='x - product - card - description__price - single')
    brands = prd.find_all('div', class_='x-product-card-description__brand-name')
    models = prd.find_all('div', class_='x-product-card-description__product-name')
    for brand, model in zip(brands, models):
        print(f"Brand: {brand.text}, Model: {model.text}")
        producer.send('Topic1', {brand.text: model.text})
