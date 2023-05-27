# Aranachnida




Web Image Scraper && Extraction Infos Exifs Images et Modification 

Description
Ce programme est un outil de récupération d'images à partir d'une URL spécifiée, qui peut fonctionner sur des sites Web locaux ou en ligne. Il peut télécharger toutes les images d'une page Web et possède une option pour le faire récursivement jusqu'à une certaine profondeur de niveau.

Installation
Assurez-vous d'avoir Python 3 et les dépendances suivantes installées :

BeautifulSoup
requests
Vous pouvez les installer en utilisant pip :

bash
Copy code
pip install beautifulsoup4 requests
Usage
Le programme est utilisé à partir de la ligne de commande. Les arguments sont l'URL à partir de laquelle les images doivent être récupérées, l'option -r ou --recursive pour indiquer si le téléchargement doit être récursif, l'option -l ou --level pour spécifier le niveau de profondeur de téléchargement récursif, et l'option -p ou --path pour spécifier le chemin où sauvegarder les images téléchargées.

Par exemple, pour télécharger toutes les images à partir d'une URL spécifique à une profondeur de 2 niveaux, vous pouvez utiliser :

bash
Copy code
python main.py "http://example.com" --recursive --level 2 --path "./downloaded_images/"
Ce qui téléchargera toutes les images de "http://example.com" et de toutes ses pages liées jusqu'à une profondeur de 2 niveaux dans le répertoire "./downloaded_images/".

Notes
Lors de l'utilisation de sites Web locaux, veillez à utiliser le chemin correct vers le fichier HTML local dans l'URL.
