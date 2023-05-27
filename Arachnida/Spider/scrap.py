import requests
from bs4 import BeautifulSoup
from save_pict import save_image
import urllib.parse
import os

'''
fonction pour recuperer les images a partir de l'Url
verifie si le ste est en local et ouvre url
>>>>
'''

def scrape(url, depth, path, current_depth=1):
    if url.startswith('http'):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    else:
        with open(url) as f:
            soup = BeautifulSoup(f, 'html.parser')

    for img in soup.find_all('img'):
        img_url = urllib.parse.urljoin(url, img.get('src'))
        if(img_url.endswith(tuple([".jpg", ".jpeg", ".png", ".gif", ".bmp"]))):
            filename = os.path.join(path, img_url.split("/")[-1])
            save_image(img_url, filename)

        if(current_depth < depth):
            for link in soup.find_all('a'):
                page_url = urllib.parse.urljoin(url, link.get('href'))
                scrape(page_url, depth, path, current_depth + 1)
