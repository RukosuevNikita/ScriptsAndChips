<<<<<<< HEAD
from bs4 import BeautifulSoup
import urllib


SITE = 'http://hosting101.ru/hoster.ru'

def Parser(SITE):
    downPage = urllib.request.urlopen(SITE)
    soup = BeautifulSoup(downPage,'html.parser')
    sorting = soup.find('div',id='comments')
    reviews = sorting.find_all('div','content')[:-1]
    for each in reviews:
        comment = each.find_all('p')
        total = '{}'.format(comment).replace('[<p>',' ').replace('</p>]', ' ')
        print(total)


def Pager(SITE):

    counter = urllib.request.urlopen(SITE)
    soup = BeautifulSoup(counter,'html.parser')
    page = soup.find(attrs={"class": "pager"}).prettify()
    lastPage = page.find("pager-last active")
    print(lastPage)


Parser(SITE)
#Pager(SITE)
=======
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
>>>>>>> 84a4055bc5c6ff6fb48b3e5e69ed26cdc943a47c
