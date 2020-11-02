from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import pandas as pd

#pseudo code strategy
#get links to all the headers
    #get all next page links within the headers
        #get data from table
            #ingest into postgres and pandas

year = ['1971']
stat_year = 1971
#get all years on ESPNs website
while stat_year < 2019:
    stat_year += 1
    year.append(stat_year)

html = urlopen('https://nfl.com/stats/player-stats/')
content = html.read()
soup = BeautifulSoup(content,'html.parser')
#get the links to see Passing, Rushing, Kicking, etc. aka statistical categories 
filtered_soup = soup.find_all('li',{'class': ['d3-o-tabs__list-item']},'href') 
print(filtered_soup[0].text)
list_of_links = ['https://nfl.com/' + str(tag.a['href']) for tag in filtered_soup]

next_button = soup.find_all('a',{'class': ['nfl-o-table-pagination__next']})
for link in next_button:
    next_button_url = 'https://nfl.com' + link['href']

table = soup.find('table',{'class': ['d3-o-table']}) # Grab the first table

#get column headers (statistical categories)
columns = []
for header in table.find_all('th',{'class':['header']}):
    columns.append(header.text.strip())

i=0
rows= {}
temp_list = []
for data_value in table.find_all('tbody'):
    test = data_value.find_all('tr')
    for data in test:
        i+=1
        test1 = data.find_all('td')
        temp_list = []
        for data1 in test1:
            table_data = data1.text.strip()
            temp_list.append(table_data)
        rows[i] = temp_list

#recursive function for web crawling
list_of_next_pages = []
def next_page(seed_url):
    try:
        html = urlopen(seed_url)
        content = html.read()
        soup = BeautifulSoup(content,'html.parser')
        next_button = soup.find_all('a',{'class': ['nfl-o-table-pagination__next']})
        for link in next_button:
            next_link = 'https://nfl.com' + link['href']
            print(next_link)
            list_of_next_pages.append(next_link)
            return next_page(next_link)
            
    except:
        pass

# next_page('https://nfl.com/stats/player-stats/')

import re
p = re.compile("[0-9]")
for m in p.finditer('a1b2c3d4'):
    print(m.start(), m.group())