# Web Scraping- Mission to Mars

Tools used: Jupyter Notebook, BeautifulSoup, Pandas, Requests/Splinter, MongoDB, Flask app, Bootstrap(V4.6), HTML5, CSS

I will be building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following is an outline of the steps taken.

## Step 1 - Scraping

* Created a Jupyter Notebook file called `mission_to_mars.ipynb` and used this to complete all of the scraping and analysis tasks.

### NASA Mars News

* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collected the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visited the url for JPL Featured Space Image.

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.

### Mars Facts

* Visited the Mars Facts webpage [here](https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visited the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list (one dictionary for each hemisphere).

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Started by converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed all of the scraping code from above and returned one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that imported the `scrape_mars.py` script and called the `scrape` function.

  * Stored the return value in MongoDB as a Python dictionary.

* Created a root route `/` that queried the Mongo database and passed the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements.