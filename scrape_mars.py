from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit 
    url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # 
    featured_img_url = soup.find_all('img')[]["src"]
    img_url = url + featured_image_url

    # 
    title = .find_all('strong')[0].text


    # Store data in a dictionary
    mars_data = {
        "img_url": featured_image_url,
        "title": title
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data