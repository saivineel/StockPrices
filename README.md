*******************************************************************************************
Project Overview

This project gives info about the prices of BSE stocks on a daily basis.

Project Flow:

1)BSE places a bhav file daily in their website.
2)This file is downloaded from the website and then extracted in to csv file.
3)Redis database is used to load the data from the csv file using appropriate data structure.
4)Cherrypy,python web framework is being used for developing a web application which gets the data from the redis database.
5)10 stock details are displayed in the webpage,however you can search for the details of your favourite stock in the search bar provided.



Executer.cmd  is the file which does all these actions step by step.
This file contains the details of the each file and the description of what it does.

*******************************************************************************************