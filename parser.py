import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urlib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(hm)
    table = soup.find('div', id='content')
    print(table.prettify())

def main():
    parse(get_html('http://hosting101.ru/hoster.ru'))

if __name__ == '__main__':
    main()
