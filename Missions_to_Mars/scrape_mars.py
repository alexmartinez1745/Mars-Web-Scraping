# Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #### Mars News ####
    # Visit news url with splinter
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
        
    # HTML object
    html = browser.html
    
    # Parse with BeautifulSoup
    soup = bs(html, 'html.parser')
    
    # Grab first element that contains news
    articles = soup.find_all('li', class_='slide')[0]
    
    # Loop through articles to find title and paragraph
    for article in articles:
        title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_='article_teaser_body').text

    #### JPL Mars Featured Image ####
    # Create base and image url then broswe to image url with splinter
    base_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
    image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(image_url)
    
    # HTML object
    html = browser.html
    
    # Parse with BeautifulSoup
    soup = bs(html, 'html.parser')
    
    # Find featured image source
    image = soup.find('div', class_='floating_text_area').a['href']
    
    # Add source to base url and print
    featured_image_url = base_url + image
        
    #### Mars Facts ####
    # Mars facts url, reading with pandas
    url = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(url)

    # Create dataframe for mars facts table
    df = mars_facts[0]

    # Convert data to HTML table string
    mars_facts_html = df.to_html('mars_facts.html', header=False, index=False)

    #### Mars Hemispheres ####
    hemisphere_base = 'https://astrogeology.usgs.gov/'
    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hemi_url)

    # Empty list to append images
    image_list = []

    # HTML object
    html = browser.html

    # Parse with BeautifulSoup
    soup = bs(html, 'html.parser')

    # Find class all images are located in
    items = soup.find_all('div', class_='item')

    # Iterate through item list
    for item in items:
        
        # Extract the titles and strip 'Enhanced'
        title_i = item.find('div', class_='description').h3.text
        title_striped = title_i.strip('Enhanced')
        
        # Image link page
        images = item.a['href']
        image_end_url = hemisphere_base + images

        # Browse to image end link
        browser.visit(image_end_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        d_link = soup.find('div', class_='downloads')
        image_end_link = d_link.find('a')['href']
        image_list.append({'title': title_striped, 
                        'url': image_end_link}) 
        
    # Create dict for mars info
    mars_info = {}
    mars_info['news_title'] = title
    mars_info['news_body'] = news_p
    mars_info['featured_image'] = featured_image_url
    mars_info['mars_facts'] = mars_facts_html
    mars_info['mars_hemispheres'] = image_list

    # Quit browser
    browser.quit()

    # Return mars info
    return mars_info