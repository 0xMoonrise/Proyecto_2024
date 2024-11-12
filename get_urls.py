#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.uabcs.mx/dasc/estudiantes/horarios/horarios-ingenieria-en-desarrollo-de-software/",
#    "https://www.uabcs.mx/dasc/estudiantes/horarios/horarios-ingenieria-en-tecnologia-computacional/",
#    "https://www.uabcs.mx/dasc/estudiantes/horarios/horarios-licenciatura-en-computacion/",
#    "https://www.uabcs.mx/dasc/estudiantes/horarios/horarios-licenciatura-en-tecnologias-de-la-informacion/",
#    "https://www.uabcs.mx/dasc/estudiantes/horarios/horarios-lingenieria-en-ciberceguridad/"
]

def get_image_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        image_urls = [img.get('src') for img in images if img.get('src')]
        image_urls = [url for url in image_urls if url.endswith('.jpg')]

        return image_urls
    else:
        print(f"Error al acceder a la URL: {url}")
        return []

all_image_urls = {}
for url in urls:
    print(f"Extrayendo URLs de horarios de: {url}")
    image_urls = get_image_urls(url)
    all_image_urls[url] = image_urls

for url, image_urls in all_image_urls.items():
    print(f"\nHorarios encontrados en {url}:")
    for image_url in image_urls:
        print(image_url)
