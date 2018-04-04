import os

def firstdiag():


    data = input('Enter site: ')
    ping = (os.system('ping -c 2 ' + data  ))
    dig = (os.system('dig ANY ' + data +' |sed -n "/ANSWER SECTION:/,/Query time:/p"'))
    nslookup = (os.system('whois ' + data +' | sed -n "/domain/,/source/p" ' ))
    invite = input('Enter to user folder? - y\nQuit - q: ')
    if invite == 'y':
        firstdiag()
    if invite == 'q':
        pass

def gotobackend():
    pass

if __name__ == '__main__':
    firstdiag()
