from bs4 import BeautifulSoup
import requests
import json
from time import sleep
import os

# get the links from the soup
def get_links(urls,soup):
    start_url = urls[0]
    urls.pop(0)
    # append all the links to the urls list
    for link in soup.find_all("a"):
        url = link.get("href") # get the href tag
        if url is None:
            continue 
        if url.startswith("/"): # relative url
            url = start_url + url
        else: # dont want to go outside the domain
            continue

        urls.append(url)
    
    return urls

# get the headings from the soup
def get_headings(divs):

    heading = ""
    if divs.find("h1") is not None:
        heading = divs.find("h1").get_text()
    elif divs.find("h2") is not None:
        heading = divs.find("h2").get_text()
    elif divs.find("h3") is not None:
        heading = divs.find("h3").get_text()
    elif divs.find("h4") is not None:
        heading = divs.find("h4").get_text()
    elif divs.find("h5") is not None:
        heading = divs.find("h5").get_text()
    elif divs.find("h6") is not None:
        heading = divs.find("h6").get_text()   

    return heading 


# main function  
def crawl(urls,max_iterations=100):
    iterations = 0
    
    try:
        os.mkdir("crawler")
    except:
        print("Error: Directory already exists")
        return
    urls_done = 0
    i = 0
    counter = 0
    while len(urls) > 0:
        iterations += 1
        if iterations > max_iterations:
            break
        print("Iterations: ", iterations)
        try:
            print ("crawling  : " ,urls[0])
            html_text = requests.get (urls[0]).text
            sleep(2)
            soup = BeautifulSoup(html_text,"lxml")
            data = []
           # print(urls)
            div_count = 0
            urls = get_links(urls,soup)
            for divs in soup.find_all("div"):
                div_count += 1
                text = divs.get_text()              
                heading = get_headings(divs)
                
           
                if text is None or text == "":
                    continue
                data_object = {}
                data_object["heading"] = heading
                data_object["text"] = text
                data.append(data_object)
                # print(data_object)
               
        
            for data_object in data:
                try:
                    f = open('crawler/{}.json'.format(counter), 'x')   
                    counter += 1
                    json.dump(data_object, f)
                    f.close()
                except Exception as e:
                    print(e)
                    continue
            
        except Exception as e:
            print(e)
            continue



url = ["https://www.medicalnewstoday.com"]

crawl(url)
