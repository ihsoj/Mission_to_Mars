# Mission to Mars

## Project Description:
This project is a full-stack web scraping endeavor to retrieve the latest Mars-related data from various websites utilizing Python, Beautiful Soup, Splinter/Selenium, HTML/CSS/Bootstrap, and Flask. The web page populates with real-time data at the click of a button.

![image](https://user-images.githubusercontent.com/51388767/71016082-a14ace80-20c2-11ea-803b-71fa4f191a6f.png)

![image](https://user-images.githubusercontent.com/51388767/71016503-3ea60280-20c3-11ea-85d1-e97abac256b2.png)

## Data:
The scraped data was stored in a MongoDB database. PyMongo and Flask were used to connect Python to the data; MongoDB Compass was utilized to verify the data structure.  

The data came from the following websites:

(1) https://tinyurl.com/wcl63gs,

(2) https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars,

(3) https://twitter.com/marswxreport?lang=en, and 

(4) https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

## Notes:
Simply navigate to the folder with app.py and "python app.py" from your terminal.
Copy the web address to your browser. Leave the browser open and then click the "Scrape New Data" button on the web page. 
Sometimes the Mars site is down so if you are having issues, attempt later. 


