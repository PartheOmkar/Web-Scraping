# Web-Scraping
Web scraping is the process of using bots to extract content and data from a website. Unlike screen scraping, which only copies pixels displayed on screen, web scraping extracts underlying HTML code and, with it, data stored in a database. The scraper can then replicate entire website content elsewhere.

# Web Scraping on flipkart 
in this repository one python file is [Flipkart.py](https://github.com/PartheOmkar/Web-Scraping/blob/main/Flipkart.py) 
  - In this file i have used python beautifulsoup to extract data.
  - here i have extracted category wise data from the Flipkart website.
  - basically in this [Flipkart.py](https://github.com/PartheOmkar/Web-Scraping/blob/main/Flipkart.py) file i have scraped mobile category data.
  - if you want to scrap another category data then you need to change in **my_url** variable and drop your link there. 
  
# Database SQLite
  - there is no need to data-base for Web-Scraping.
  - but if you want to perform analysis operations on the abstracted data then you need to store abstracted data in Database.
  - in this Repository we have added [flipkart.sqlite](https://github.com/PartheOmkar/Web-Scraping/blob/main/Flipkart.sqlite) database file for store data.
  - if you want to change the Database file then you need to make some changes in [Flipkart.py](https://github.com/PartheOmkar/Web-Scraping/blob/main/Flipkart.py) file.
  - you Don't need to create a table in the database, once [Flipkart.py](https://github.com/PartheOmkar/Web-Scraping/blob/main/Flipkart.py) file is executed it creates a required table.
