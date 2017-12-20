REM This file executes a series of scripts instead of exceting all the scripts manually.

REM Here the below path is given based on my local system it needs to be changed to execute in your system.

REM Downloader script downloads the file from the bse website and places to the required folder.

python C:\Users\sa352283\Desktop\SimpleTask\Downloader.py

REM Extracter script extracts the downloaded zip file.

python C:\Users\sa352283\Desktop\SimpleTask\Extracter.py

REM Loader script flushes the previous days data in the database and loads the todays data.

python C:\Users\sa352283\Desktop\SimpleTask\Loader.py

REM Move_To_Archive script moves the scripts downloaded in to the Archive location.

python C:\Users\sa352283\Desktop\SimpleTask\Move_To_Archive.py

