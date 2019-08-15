#Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time




def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'C:/Users/jp_ba/Desktop/WebScraping/chromedriver.exe'}
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




  #url and use Splinter to visit
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    #Extract title text
    news_title = soup.find_all('div', class_='content_title')[0].text
    

    #Extract paragraph text
    news_p = soup.find('div', class_="article_teaser_body").get_text()
    

    #url and use Splinter to visit
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")


    #Create object to find image and replace extra punctuation to create accurate url
    image_url = soup.find('article')['style']
    image_url = image_url.replace('background-image: url(','').replace('(','').replace(');','')[1:-1]

    featured_image_url = (url2 + image_url)


    #Visit twitter url
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    #Text from Twitter
    timeline = soup.select('#timeline div.js-actionable-tweet')

    for twitter in timeline:
    # select the tweet id 
    tweet = twitter['data-screen-name']
    
    if tweet == "MarsWxReport":
        tweet_text = twitter.select('p.tweet-text')[0].get_text()
        mars_weather = tweet_text
        break


    #Visit facts url
    url4 = 'https://space-facts.com/mars/'
    browser.visit(url4)

    # Create BeautifulSoup object; parse with 'html'
    soup = bs(browser.html, 'html.parser')

    facts = pd.read_html(url4)

    df_facts = pd.DataFrame(facts[0])

    html_facts = df_facts.to_html()


    #Visit astrogeology url
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)

    html = browser.html
    soup = bs(html, "html.parser")

    #Select items
    items = soup.find_all('div', class_='item')

    base_url = "https://astrogeology.usgs.gov"

    #Empty list to append when iterated
    hemisphere_image_urls = []

    #Iterate through items to visit urls and retrieve image urls
    for x in items: 
        title = x.find('h3').get_text()
        image_url = x.find('a', class_="itemLink product-item")['href']
        browser.visit(base_url + image_url)
        html = browser.html
        soup = bs(html, "html.parser")
        resolution_url = soup.find('img',class_='wide-image')['src'] 
        hemisphere_image_urls.append(
            {"title":title,
            "image_url":base_url + resolution_url}
        )

    #Create BeautifulSoup object; parse with 'html'
    soup = bs(browser.html, 'html.parser')
    mars_data = {}
    mars_data = {
        "news_title": news_title,
        "news_text": news_p,
        "featured_image": featured_image_url,
        "html":html_facts,
        "mars_weather": mars_weather,
        "hemisphere_images": hemisphere_image_urls
    }
    browser.quit()
    return(mars_data)
    


    


   

    # set url for facts
    facts_url = "https://space-facts.com/mars/"

    # extract table from website using pandas
    table = pd.read_html(facts_url)

    # convert table into a dataframe
    df = pd.DataFrame(table[0])

    # convert dataframe to html 
    html_table = df.to_html()
    
    # initialize visit to astrogeology
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    html = browser.html
    hemi_soup = bs(html, "html.parser")

    # select all product items
    products = hemi_soup.find_all('div', class_='item')

    # identify base url to be used to build out additional links
    base_url = "https://astrogeology.usgs.gov"

    hemisphere_image_urls = []

    # iterate through products to visit their urls and get image links
    for i in products:
        # collect titles and urls for enhanced images 
        titles = i.find('h3').get_text()
        url = i.find('a', class_="itemLink product-item")['href']
        # visit each url
        browser.visit(base_url + url)
        time.sleep(1)
        html = browser.html
        hemi_soup = bs(html, "html.parser")
        # get url for enhanced image
        enhanced_url = hemi_soup.find('img',class_='wide-image')['src']
        hemisphere_image_urls.append(
            {"title":titles,
            "img_url":base_url + enhanced_url}
        )

    