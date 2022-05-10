import re
import os
import json
import requests
import htmlToPDF
from datetime import datetime
from bs4 import BeautifulSoup


class Scraper(object):
    def __init__(self, url) -> None:
        self.url = url
        self.request = requests.get(url)

    def scrape(self):
        data = {}
        soup = BeautifulSoup(self.request.text, 'html.parser')
        scriptJSON = soup.find(
            'script', {'id': '__NEXT_DATA__', 'type': 'application/json'})
        scriptJSON = json.loads(scriptJSON.getText())
        details = scriptJSON['props']['pageProps']['listingDetails']

        # Data return values
        data['title'] = ' '.join([details['vehicle'].get('make'), details['vehicle'].get(
            'model'), details['vehicle'].get('modelVersionInput')])
        data['year'] = details['vehicle'].get('firstRegistrationDate')
        data['transmission'] = details['vehicle'].get('transmissionType')
        data['fuel'] = details['vehicle']['fuelCategory']['formatted']
        data['km'] = details['vehicle'].get('mileageInKmRaw')
        data['power'] = details['vehicle'].get('rawPowerInHp')
        data['c02'] = details['vehicle']['co2emissionInGramPerKm']['formatted']
        data['images'] = scriptJSON['props']['pageProps']['listingDetails']['images']
        data['vendedor'] = {
            'name': details['seller']['companyName'],
            'location': ' '.join([details['location'][x]
                                  for x in details['location']]),
            'phone': details['seller']['phones'][0]['callTo']
        }

        return data

    def pdf(self, title: str):
        # Paths
        now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        file_html = os.path.join(os.getcwd(), 'files',
                                 'html', f'{now}_{title}.html')
        file_pdf = os.path.join(os.getcwd(), 'files',
                                'pdfs', f'{now}_{title}.pdf')

        # Create html
        html = self.request.text
        html = re.sub(r'(?i)(color)', '', html)
        with open(file_html, 'w+') as file:
            file.write(html)

        # PDF
        htmlToPDF.htmlToPDF(file_html, file_pdf)


def main(url: str):
    scrpr = Scraper(url)
    data = scrpr.scrape()
    pdf = scrpr.pdf(data['title'])
    return data
