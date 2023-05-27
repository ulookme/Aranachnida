from bs4 import BeautifulSoup
import requests

'''
Fonction faire une requet get a l' URL 
si la requete reussi est egale a 200 
ouvrie le fichier en mode ecriture binaire et l'enregistre

'''

def save_image(url, path):
    if url.startswith('http'):
        response = requests.get(url, stream = True)
        if response.status_code == 200:
            with open(path, 'wb') as out_file:
                out_file.write(response.content)
    else:
        os.shutil.copy(url, path)
