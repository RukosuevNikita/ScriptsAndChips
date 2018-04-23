from bs4 import BeautifulSoup
import urllib

# Parser works for any site on hosting101.ru.
# As example set hoster.ru, but you can change manually
# Site thats you need on line 23

def Parser(SITE):
    downPage = urllib.request.urlopen(SITE)
    soup = BeautifulSoup(downPage,'html.parser')
    sorting = soup.find('div',id='comments')
    reviews = sorting.find_all('div','content')[:-1] # First 'div' element has no practical meaning

    for each in reviews:
        comment = each.find_all('p')
        total = '{}'.format(comment).replace('[<p>',' ').replace('</p>]', ' ')
        with open('reviews.txt','a') as f: 
            f.write(total + '\n\n')
        print(total)

if __name__ == '__main__':
    for i in range(1,12): # This is page pool, you can change it manually for hosting thats you need 
        SITE = 'http://hosting101.ru/hoster.ru?page={}'.format(i) # Here you can change site
        Parser(SITE)

# P.S. I know that i can reqest pagepool from html page as self-contained function, but there is no needed in my work.
