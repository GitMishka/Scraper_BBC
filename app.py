import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []

    for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        headlines.append(h.get_text(strip=True))

    return headlines

headlines = scrape_headlines('https://www.bbc.com/news')
for headline in headlines:
    print(headline)
