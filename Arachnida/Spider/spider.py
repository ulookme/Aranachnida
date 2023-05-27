import os
import requests
from bs4 import BeautifulSoup
from scrap import scrape
import argparse

'''
Fonction principale main avec ARGV

'''

def main():
    parser = argparse.ArgumentParser()  # Créer un analyseur d'arguments
    # Ajouter les arguments nécessaires
    parser.add_argument('url', help='L\'URL à partir de laquelle récupérer les images.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Télécharger les images de manière récursive.')
    parser.add_argument('-l', '--level', type=int, default=5,
                        help='Le niveau de profondeur maximal de téléchargement récursif.')
    parser.add_argument('-p', '--path', default='./data/',
                        help='Le chemin où sauvegarder les images téléchargées.')
    args = parser.parse_args()  # Analyser les arguments de la ligne de commande

    if not os.path.exists(args.path):  # Si le chemin spécifié n'existe pas,
        os.makedirs(args.path)  # Créer ce chemin

    # Si l'option de téléchargement récursif est activée,
    if args.recursive:
        scrape(args.url, args.level, args.path)  # Récupérer les images de manière récursive
    else:
        scrape(args.url, 1, args.path)  # Récupérer les images sans récursion

if __name__ == "__main__":
    main()