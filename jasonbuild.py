import shorter
import diffinder
import topicfinder
import subjectfinder
import transcription

import requests
from bs4 import BeautifulSoup
import re

with open('unspiderlink.txt') as file:
    links = file.read().splitlines()

for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('p', class_='chakra-text css-lnjjrs')

    title = ''
    for title in soup.find_all('title'):
        title = title.get_text()

    for quote in quotes:
        print(quote.text)
        f = open(title+'.txt', "a")
        f.write(quote.text)
        f.write('\n')