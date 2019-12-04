#!/usr/bin/env python
# coding: utf-8

from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import pymongo
import pprint

# For Windows Users
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News
def scrape():
    data = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)


    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

   
    news = soup.find('div', class_='content_title')
    type(news)

    news_title = news.get_text()
    news_title
    #news_title = news.text.strip()
    news_title
    news_para = soup.find('div', class_='rollover_description_inner')
    news_p = news_para.get_text()
    news_p = news_para.text.strip()
    news_p
    data["news_title"] = news_title
    data["news_paragraph"] = news_p
    print(data["news_title"], " ",data["news_paragraph"])

    # ### JPL Mars Space Images - Featured Image

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    elem = browser.find_by_id('full_image').first.click()
    print(elem)

    something = browser. find_link_by_partial_text('more info')
    time.sleep(5)
    something.click()
    time.sleep(5)

    soup = BeautifulSoup(browser.html, 'html.parser')
    result=soup.find('figure',class_="lede")
    print(result)

    url = result.a.img['src']
    url

    featured_image_url = 'https://www.jpl.nasa.gov' + (url)
    featured_image_url
    data["images"] = featured_image_url

    # ### Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_="js-tweet-text-container")
    results

    for result in results:
        mars_weather = result.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)
    data["weather"] = mars_weather

    # ### Mars Facts
    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    tables
    type(tables)

    df = tables[0]
    df.columns = ['Mars - Earth Comparison','Mars']
    df

    html_table = df.to_html()
    html_table

    mars_facts = html_table.replace('\n', '')
    mars_facts
    data["facts"] = mars_facts
    df.to_html('table.html')

    # ### Mars Hemispheres
    
    # url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    # browser.visit(url)
    # hemispheres = browser.html

    # #Parse with Beautiful Soup
    # soup = BeautifulSoup(hemispheres, "html.parser")
    # hemilinks = soup.find_all('div', class_='item')
    # print(hemilinks)

    # # Create empty list to hold data
    # hemisphere_image_urls = []
    # usg_url = 'https://astrogeology.usgs.gov'

    # # Create For Loop
    # for elem in hemilinks:
    #     title = elem.find('h3').text
    #     links = elem.find('a', class_='itemLink product-item')['href']
    #     browser.visit(usg_url + links)
    #     image_html = browser.html
    #     soup = BeautifulSoup(image_html, 'html.parser')
    #     image_url = usg_url + soup.find('img', class_ ='wide-image')['src']
    #     hemisphere_image_urls.append({'title': title, 'image_url': image_url})
    # hemisphere_image_urls 
    # data["hemispheres"] = hemisphere_image_urls

    url_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url_hemi)    
    time.sleep(5)       
    usgs_soup = BeautifulSoup(browser.html, 'html.parser')
    headers = []
    titles = usgs_soup.find_all('h3')  
    time.sleep(5)

    for title in titles: 
      headers.append(title.text)

    images = []
    count = 0
    for thumb in headers:
        browser.find_by_css('img.thumb')[count].click()
        images.append(browser.find_by_text('Sample')['href'])
        browser.back()
        count = count+1

    hemisphere_image_urls = []  #initialize empty list to collect titles
    counter = 0
    for item in images:
        hemisphere_image_urls.append({"title":headers[counter],"img_url":images[counter]})
        counter = counter+1
    # closeBrowser(browser)
    browser.back()
    time.sleep(1)
    data["hemispheres"]=hemisphere_image_urls
    print(hemisphere_image_urls)


 #   data = {
 #           'news': [news_title, news_p],
 #           'images': featured_image_url,
 #           'weather': mars_weather,
 #           'facts': mars_facts,
 #           'hemispheres': hemisphere_image_urls
 #       }
    return data
if __name__ == "__main__":
    print(scrape())
