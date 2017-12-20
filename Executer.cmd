REM This file executes a series of scripts instead of exceting all the scripts manually.

REM Here the below path is given based on my local system it needs to be changed to execute in your system.

REM Downloader script downloads the file from the bse website and places to the required folder.

python C:\Users\sai\Desktop\PythonProject\Downloader.py

REM Extracter script extracts the downloaded zip file.

python C:\Users\sai\Desktop\PythonProject\Extracter.py

REM Loader script flushes the previous days data in the database and loads the todays data.

python C:\Users\sai\Desktop\PythonProject\Loader.py

REM Move_To_Archive script moves the scripts downloaded in to the Archive location.

python C:\Users\sai\Desktop\PythonProject\Move_To_Archive.py

REM MyProj.py is the heart of this project.This files is responsible for the web server to run and server the search requests.

python C:\Users\sai\Desktop\PythonProject\Website



