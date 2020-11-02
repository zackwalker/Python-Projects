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
    # get all years on ESPNs website
    while stat_year > 2019:
        stat_year -= 1
        years.append(stat_year)

    seed_url = 'https://www.pro-football-reference.com/years/'
    weeks = list(('week_' + str(week_num) for week_num in range(1, 2)))

    for year in years:
        for week in weeks:
            urls.append(seed_url + str(year) + '/' + week + '.htm')

    base_url = 'https://www.pro-football-reference.com'
    options = Options()
    options.headless = True
    page_dfs = []
    # uses chrome and with the given webdriver location (make this a env var)
    with webdriver.Chrome("C:\\Users\\zwalk\\Downloads\\chromedriver_win32\\chromedriver.exe") as driver:
        driver.implicitly_wait(2)  # wait 3 seconds
        for url_link in urls:
            driver.get(url_link)  # go to URL
            # renders out the page
            soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
            # gets ul with specific class, getting all href attributes that contain 'category'
            links = soup.find_all('td', 'right gamelink')

            # print(urls)
            for link in links:
                weekly_box_scores.append(base_url + str(link.a['href']))
        # weekly_box_scores.pop(0)

        for link in weekly_box_scores:

            driver.get(link)  # uses new URL from tuple that was joined
            # flavor = parser engine, page_source
            # renders out the page
            soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
            # gets ul with specific class, getting all href attributes that contain 'category'
            df = pd.read_html(driver.page_source, index_col=0, flavor='lxml', attrs={
                              'id': 'player_offense'})[0]  # page source
            # to get more accurate week and season,
            # I need to create a dict to corresponde the values in 'urls'
            # to the links that come from it
            df['Week'] = link[link.find('20'):len(link)-4]
            df['Season'] = link[link.find('20'):link.find('20')+4]
            # df = df[df.line_race != 0]
            page_dfs.append(df)
        cat_df = pd.concat(page_dfs)
        cat_df.to_csv('test.csv', mode='a',index=False, header=['Player','Tm','Cmp','Att','Yds','TD',
                                                    'Int','Sk','Yds','Lng','Rate','Att',
                                                    'Yds','TD','Lng','Tgt','Rec','Yds','TD','Lng','Fmb','FL','week'])

    print(page_dfs)


if __name__ == '__main__':
    main()
