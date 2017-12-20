*******************************************************************************************
Project Overview

This project deals with the prices of stocks on a regular basis.

Project Flow:

1)BSE places a bhav file daily in their website.
2)This file is downloaded from the webiste and then extracted in to csv file.
3)Redis database is used to load the data from the csv file.
4)Cherrypy, a python framework is being used for developing a web application which gets the data from the redis database.
5)Only 10 stock details are displayed in the webpage,however you can search for your favourite stock in the search bar provided. 


*******************************************************************************************