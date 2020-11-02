import re
import sys
from urllib.parse import urljoin

import bs4
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def main():

    years = []
    urls = []
    weekly_box_scores = []
    stat_year = 2020
    #get all years on ESPNs website
    while stat_year > 2019:
        stat_year -= 1
        years.append(stat_year)

    seed_url = 'https://www.pro-football-reference.com/years/'
    weeks = list(('week_' + str(week_num) for week_num in range(1,2)))


    for year in years:
        for week in weeks:
            urls.append(seed_url + str(year) + '/' + week + '.htm')

    base_url = 'https://www.pro-football-reference.com'
    options = Options()
    options.headless = True
    #uses chrome and with the given webdriver location (make this a env var)
    with webdriver.Chrome("C:\\Users\\zwalk\\Downloads\\chromedriver_win32\\chromedriver.exe") as driver:
        driver.implicitly_wait(2) #wait 3 seconds
        for url_link in urls:
            driver.get(url_link) #go to URL
            soup = bs4.BeautifulSoup(driver.page_source, 'lxml') #renders out the page
            #gets ul with specific class, getting all href attributes that contain 'category'
            links = soup.find_all('td', 'right gamelink')
            year_of_stat = url_link[45:49]
            week_of_stat = url_link[55:56]
            for link in links:
                weekly_box_scores.append([base_url + str(link.a['href']),year_of_stat,week_of_stat])
    print(weekly_box_scores)



if __name__ == '__main__':
    main()