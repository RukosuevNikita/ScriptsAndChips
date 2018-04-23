from bs4 import BeautifulSoup
import urllib


def Parser(SITE):
    downPage = urllib.request.urlopen(SITE)
    soup = BeautifulSoup(downPage,'html.parser')
    sorting = soup.find('div',id='comments')
    reviews = sorting.find_all('div','content')[:-1]
    for each in reviews:
        comment = each.find_all('p')
        total = '{}'.format(comment).replace('[<p>',' ').replace('</p>]', ' ')
        with open('reviews.txt','a') as f:
            f.write(total + '\n\n')
        print(total)

if __name__ == '__main__':
    for i in range(1,12):
        SITE = 'http://hosting101.ru/hoster.ru?page={}'.format(i)
        Parser(SITE)
