import re
import json
from bs4 import BeautifulSoup


def scrape(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('div', {'class': 'g-row'})
    for n, row in enumerate(rows):
        rows[n] = row.getText()

    print(rows)

    return json.dumps(rows)
