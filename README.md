# scrappingXpath
Introduction to Web scrapping with XPATH

This repository contains two python files:

- scraper.py 
- comercioscrap.py

scraper.py use the module **requests** and **lxmx** to get a **HTTP** file from the news website: **'https://www.larepublica.co'**. Use the module **lxml** to setup the HTTP with encoding **"UTF-8"** and uses XPATH format to locate specific nodes with links to the articles of the Home.

Then creates a folder with the current date. Inside this folder a .txt file is created with the name of the article on the site.

__The .txt files depends on the articles of the web site home__

comercioscrap.py use the same script adapted to the Ecuadorian News site: **'https://www.elcomercio.com'**