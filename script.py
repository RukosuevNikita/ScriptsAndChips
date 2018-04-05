import os

#Return console command's: ping, dig ANY and whois.
def firstdiag(data):
    ping = (os.system('ping -c 2 ' + data  ))
    dig = (os.system('dig ANY ' + data +' |sed -n "/ANSWER SECTION:/,/Query time:/p"'))
    nslookup = (os.system('whois ' + data +' | sed -n "/domain/,/source/p" ' ))
    invite = input('Press 1 to ping\nPress2 to dig ANY\nPress 3 to nslookup')




if __name__ == '__main__':
    data = input('Enter site: ')
    firstdiag(data)
