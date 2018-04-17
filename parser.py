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
