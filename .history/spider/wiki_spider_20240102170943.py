import requests
from bs4 import BeautifulSoup


def scrape_wikipedia_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_div = soup.find('div', {'class': 'mw-parser-output'})
    paragraphs = content_div.find_all('p')

    intro_text = ''
    for paragraph in paragraphs:
        intro_text += paragraph.text

    return intro_text


url = 'https://en.wikipedia.org/wiki/Acanthoscelides_obtectus'
print(scrape_wikipedia_page(url))
