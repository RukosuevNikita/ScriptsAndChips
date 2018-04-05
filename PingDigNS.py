import os

#Return console command's: ping, dig ANY and whois.
#ping delivers only 2 packages
#dig returns only sections that matter
#nslookup as dig

def bunch():
    ping = (os.system('ping -c 2 ' + data  ))
    dig = (os.system('dig ANY ' + data +' |sed -n "/ANSWER SECTION:/,/Query time:/p"'))
    nslookup = (os.system('whois ' + data +' | sed -n "/domain/,/source/p" ' ))


if __name__ == '__main__':
    data = input('Enter site: ')
    bunch()
