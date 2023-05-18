# Text Data Collection

This repository contains, python scripts for scraping the data from various medical sites, done as a part of BTP-1 project, at LTRC lab, using the libraries like selenium and beautifulsoup, to extract the data. 

Data : `https://drive.google.com/drive/folders/1EizJyA6CBcW90YtU32p80-3Ilw0-J5-r?usp=sharing`

## installing requirments.txt

Run the following command, to setup dependancies: 

```py
    pip3 install -r requirements.txt
```

## crawler.py

This file contains the general crawler code, upon running the file as below, it'll start scrapping the webpages from the starting url provided in the urls array. You can modify this url startpoint, as per your convinience, and it'll start scraping the web pages, and store them into json objects. The filtering of data, etc. remains to be done, and will be covered in future releases.

Run the following command, to run the script: 

```py
    python3 crawler.py
```
## edutopia.py

Run the following command, to run the script: 
This file scraps, data from the edutopia website and generates a folder under the name of `edutopia`, and generates json objects accordingly.

```py
    python3 edutopia.py
```

## medicaldirectory.py

This file scraps the data from `https://www.medicalnewstoday.com/directory/a-b`, and extracts all the data and stores them into category wise sorted data that could be found at : `https://drive.google.com/drive/folders/1EizJyA6CBcW90YtU32p80-3Ilw0-J5-r?usp=sharing`. As shown in the report the data collected, is well categorised into several domains, each with an easily modifiable json file.

Run the following command, to run the script: 

```py
    python3 medicaldirectory.py
```

## medicalnews.py

Run the following command, to run the script: 

```py
    python3 medicalnews.py
```
