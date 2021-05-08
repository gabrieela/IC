import bs4
import pandas
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

from pathlib import Path
import requests

baseUrl = 'http://www.ans.gov.br'
url = baseUrl + '/prestadores/tiss-troca-de-informacao-de-saude-suplementar'

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')

link = soup.find('div', {"class": "alert alert-icolink"}).find('a', {"class": 'alert-link'})['href']

completeLink = baseUrl + link

response = urlopen(completeLink)

html = response.read()

soup = BeautifulSoup(html, 'html.parser')

nameFile = soup.findAll('td')[0].getText()

version = soup.findAll('td')[1].getText()

linkFile = soup.find('a', {"class": 'btn btn-primary btn-sm center-block'})['href']

completeLinkFile = baseUrl + linkFile

filename = Path(nameFile + ' - Versão ' + version + '.pdf')

response = requests.get(completeLinkFile)
filename.write_bytes(response.content)
print(f'O arquivo "{filename}" foi salvo com sucesso!')