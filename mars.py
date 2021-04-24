# 10.3.3 Scrape Mars Data: The News

# Import Splinter


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # 10.3.4 Scrape Mars Data: Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'#This variable holds our f-string. 
#The curly brackets hold a variable that will be inserted into the f-string when it's executed.
img_url

# # 10.3.5 Scrape Mars Data: Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()



# 10.3.6 Export to Python

# 10.4.1 Store the Data
# Create a Database

## = type
## "use practicedb" 

## db (it returns the name of the current active database)

# how many databases are stored locally
## show dbs

# Insert Data
## db.zoo.insert({name: 'Cleo', species: 'jaguar', age: 12, hobbies: ['sleeping', 'eating', 'climbing']})

# WriteResult({ 'nInserted" : 1 })This means that we've successfully inserted Cleo into the database.

## db.zoo.insert({name: 'Banzai', species: 'fox', age: 1, hobbies: ['sleeping', 'eating', 'playing']})
## db.zoo.insert({name: 'Gomzi', species: 'Cat', age: 2, hobbies: ['sleeping', 'eating', 'playing']})
## db.zoo.insert({name: 'Methi', species: 'Bird', age: 3, hobbies: ['sleeping', 'eating', 'playing']})
## db.zoo.insert({name: 'Lilly', species: 'Dog', age: 1, hobbies: ['sleeping', 'eating', 'playing']})

# Documents can also be deleted or dropped. The syntax to do so follows:
## db.zoo.remove({})

# if we wanted to remove Cleo from the database, we would update that line of code to:
## db.zoo.remove({name: 'Cleo'})

# For example, to empty our pets collection, we would type:
## db.zoo.remove({})

# to remove a collection all together, we would use
## db.zoo.drop()

# to remove the test database, we will use this line of code:
## db.dropDatabase()

