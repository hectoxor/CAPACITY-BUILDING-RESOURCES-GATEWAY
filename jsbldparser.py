import shorter
import diffinder
import topicfinder
import subjectfinder
import transcription

import requests
from bs4 import BeautifulSoup
import re

def news(href):
    return href and re.compile("missions/").search(href)

url = 'https://www.eoportal.org/satellite-missions'

response = requests.get(url+'?page='+str(i))
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all(href=news)
for link in quotes:
    if link.has_attr('href'):
        print('https://www.eoportal.org/'+link['href'])
        f = open('unspiderlink.txt', "a")
        f.write('https://www.eoportal.org/'+link['href'])
        f.write('\n')