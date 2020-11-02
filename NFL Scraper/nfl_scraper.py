
import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# Datset could have multiple pages.  We will set on page 1 to begin
p = 1

statisticCategory = 'rushing'
season = 2019

payload = {"statisticCategory":statisticCategory.upper(),"seasonType":"REG","d-447263-p":str(p),"season":season}
url = 'http://www.nfl.com/stats/player-stats/category'
response = requests.get(url,params=payload)

print("Response:", response.status_code,response.url) #200 means it went through