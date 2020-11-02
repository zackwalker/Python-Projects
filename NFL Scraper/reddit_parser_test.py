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
    while stat_year > 2012:
        stat_year -= 1
        years.append(stat_year)

    seed_url = 'https://www.pro-football-reference.com/years/'
    weeks = list(('week_' + str(week_num) for week_num in range(1,2)))
    #gets game by game links
    for year in years:
        for week in weeks:
            urls.append(seed_url + str(year) + '/' + week + '.htm')
    
    url = 'https://www.nfl.com/stats/player-stats/'
    options = Options()
    options.headless = True
    #uses chrome and with the given webdriver location (make this a env var)
    with webdriver.Chrome("C:\\Users\\zwalk\\Downloads\\chromedriver_win32\\chromedriver.exe") as driver:
        driver.implicitly_wait(2) #wait 3 seconds
        driver.get(url) #go to URL
        soup = bs4.BeautifulSoup(driver.page_source, 'lxml') #renders out the page
        #gets ul with specific class, getting all href attributes that contain 'category'
        links = soup.find('ul', 'd3-o-tabs').find_all(href=re.compile('category'))
        cat_links = [[a.text.strip(), str(urljoin(url, a['href']))] for a in links][:6] #list comprehension. produce a tuple named cat_links

        all_links = []

        for year in years:
            for link in cat_links:
                point_holder = link[1].find(str(years[0]))
                all_links.append([link[0],link[1][:point_holder] + str(year) + link[1][point_holder+4:], year])

        consolodated_dict = {}
        for url_data in all_links:
            #sets default value for a key
            consolodated_dict.setdefault(url_data[0],[])
            #appends category, url and year
            consolodated_dict[url_data[0]].append([url_data[0],url_data[1], url_data[2]])

        #that tuple has tht text from that tag (stripped to remove spaces)
        #the next tuple is joining the base URL with the href attribute of link
        for category in consolodated_dict:
            page_dfs = []
            for cat, url, year in consolodated_dict[category]:
                    
                driver.get(url) #uses new URL from tuple that was joined
                while True:
                    try:
                        #flavor = parser engine, page_source
                        df = pd.read_html(driver.page_source, index_col=0, flavor='lxml')[0] #page source
                        df['Year'] = year
                        page_dfs.append(df) # appends scraped df
                        # page_dfs['Test'] = page_dfs[1]
                        # page_dfs.append(year,axis=1) # appends scraped df
                        # page_dfs.insert("Year",year) # appends scraped df
                        next_button = driver.find_element_by_class_name('nfl-o-table-pagination__next') #next button's class
                        next_button.click() #clicking the next button
                    except (ValueError, NoSuchElementException):
                        break #if nexxt button doesnt exist, break out of it
            if page_dfs:
                fn = f'{cat}.csv' #name the csv after the category from above
                # print('saving', fn)
                cat_df = pd.concat(page_dfs)
                cat_df.to_csv(fn, mode='a', header=False)


        for url_link in urls:

            links = soup.find_all('td', 'right gamelink')
            year_of_stat = url_link[45:49]
            week_of_stat = url_link[55:56]
            base_url = 'https://www.pro-football-reference.com'
            for link in links:
                weekly_box_scores.append([base_url + str(link.a['href']),year_of_stat,week_of_stat])

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
        game_df = pd.concat(page_dfs)
        game_df.to_csv('test.csv', mode='a',index=False, header=['Player','Tm','Cmp','Att','Yds','TD',
                                                    'Int','Sk','Yds','Lng','Rate','Att',
                                                    'Yds','TD','Lng','Tgt','Rec','Yds','TD','Lng','Fmb','FL','week'])



if __name__ == '__main__':
    main()