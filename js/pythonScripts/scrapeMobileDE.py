import re
import os
import sys
import requests
import threading
import htmlToPDF
import unicodedata
from subprocess import Popen, DEVNULL
from bs4 import BeautifulSoup


def scrape(r):
    # Main soup
    soup = BeautifulSoup(r.text, 'html.parser')
    tecnicData = soup.find_all('div', {'class': 'g-row'})
    rows = []

    # Non-iterable soups
    title = r.url.replace('https://www.mobile.de/es/Veh%C3%ADculo', '')
    title = re.search('(?<=/)(.+?)(?=/)', title)

    images = soup.find_all('img')
    for n, im in enumerate(images):
        try:
            url = im.attrs['src']
            if 'https://img.classistatic.de/api/v1/mo-prod/images/' in url:
                images[n] = url.replace('160.jpg', '1024.jpg')
            else:
                images[n] = None
        except:
            images[n] = None

    images = [x for x in images if x != None]
    images = list(dict.fromkeys(images))

    # Iterate and order all data
    data = {
        'title': title,
        'year': None,
        'transmission': None,
        'fuel': None,
        'km': None,
        'power': None,
        'c02': None,
        'images': images
    }

    patterns = {
        'year': '\d{2}\/\d{4}',
        'transmission': '(?<=Cambio)(.+)?',
        'fuel': '(?<=Combustible)(.+)?',
        'km': '\d+(?=\s+?km)',
        'power': '\d+(?=\s+?cv)',
        'c02': '\d+(?=\s+?g/km)'
    }

    # Find the text from each row
    for row in tecnicData:
        row = row.findChildren('span', recursive=False)
        if row != []:
            row = ''.join(list(map(BeautifulSoup.getText, row)))
            row = row.strip().replace('.', '').replace(',', '')
            row = unicodedata.normalize('NFKD', row)
            rows.append(row)

    # Get all re objects
    for row in rows:
        for key in data:
            if data[key] == None:
                data[key] = re.search(patterns[key], row)

    # Get re search result in a nice string format
    for key in data:
        if data[key] != None:
            try:
                data[key] = data[key].group().strip(
                ).capitalize().replace('-', ' ')

            except AttributeError as e:
                pass

    return data


def main(r):
    # Data
    data = scrape(r)
    file_html = os.path.join(os.getcwd(), 'files',
                             'html', data['title']+'.html')
    file_pdf = os.path.join(os.getcwd(), 'files', 'pdfs', data['title']+'.pdf')

    with open(file_html, 'w+') as file:
        file.write(r.text)

    # PDF
    htmlToPDF.htmlToPDF(file_html, file_pdf)

    return data
