#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import json

baseurl = "https://www.dba.dk/soeg/?soeg="

args = sys.argv[1:]

if not args or args[0] == '--help':
    print('Usage: dba.py [--help] [ARGUMENT]...')
    print('')
    print('Search dba.dk for each argument and print results.')
    print('With --help option: print this and exit.')
    print('By Marcus Larsen')
else:
    for arg in args:
        print('Search: ' + arg)
        url = baseurl + arg
        try:
            r = requests.get(url)
        except:
            print('Do you have an internet connection?')
            break

        soup = BeautifulSoup(r.text, 'lxml')

        count = 0
        for td in soup.find_all('td'):
            if td.get('class') and 'mainContent' in td.get('class'):
                count += 1
                data = json.loads(td.script.string)

                print(data['name'])
                print('url:\t' + data['url'])
                print('price:\t' + data['offers']['price'] + data['offers']['priceCurrency'])
                print('')   # newline

        if count == 0:
            print('None\n')