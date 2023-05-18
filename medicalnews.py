#  import the library utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import json




#  store the class ids for different classes
class_ids = {
        "tab" : "css-1jz3emd", # class for the tabs
        "category" : "css-vyngri", # class for the categories
        "article" :"css-kbq0t", # class for the articles
        "article_heading" : "css-5dw8ta", # class for the article heading
        "article_text" : "css-ur5q1p" # class for the article text
}

url = "https://www.medicalnewstoday.com/directory/a-b" # url of the website
# initialize the driver


def init_driver():
    # initialize the driver
    try:    
        driver = webdriver.Chrome()
        driver.wait = WebDriverWait(driver, 5)
        return driver
    except Exception as e:
        print(e)
        return None
    
def load_website(driver, url):
    # load the website
    try:
        driver.get(url)
        sleep(2)
        return True
    except:
        return False

counter = 0
def get_data(url):
  
    driver = init_driver()
    
    if driver is None:
        print("Error: Driver not initialized")
        return
    
    website_loaded = load_website(driver, url)
    
    if not website_loaded:
        print("Error: Website not loaded")
        return
    
    try:
        os.mkdir("medicalnewsDirectory")
    except:
        print("Error: Directory already exists")
        # return

    # for each tab get the categories
        
    categories = driver.find_elements(By.CLASS_NAME, class_ids["category"])
    l = len(categories)
    print(l)
    for i in range(l):
        category = driver.find_elements(By.CLASS_NAME, class_ids["category"])[i]
        category_name = category.text
         #replace '/' and ':' with '-'
        category_name = category_name.replace('/', '-')
        category_name = category_name.replace(':', '-')

        try:
            os.mkdir("medicalnewsDirectory/{}".format(category_name))
        except:
            print("Error: Directory already exists")
            continue
        category.click()    
        sleep(2)
        articles = driver.find_elements(By.CLASS_NAME, class_ids["article"])
        sleep(2)
        text_to_be_found = []
        for article in articles:
        # highlight the element
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", article, "background: yellow; border: 2px solid red;")
            print(article.text)
            heading = article.find_element(By.CLASS_NAME, class_ids["article_heading"])
            print(heading.text)
            text = article.find_element(By.CLASS_NAME, class_ids["article_text"])
            text_to_be_found.append({"heading": heading.text, "text": text.text})
            # scroll 
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", article, "background: none; border: none;") 
            driver.execute_script("arguments[0].scrollIntoView();", article)    

            sleep(2)
        
       
        
        j = 0
        for text in text_to_be_found:
            f = open('medicalnewsDirectory/{}/{}.json'.format(category_name,j), 'x')   
            j+=1
            json.dump(text, f)
            f.close()
        print("going back")
        driver.get(url)
        
        sleep(3)

urls = [
       "https://www.medicalnewstoday.com/directory/a-b",
       "https://www.medicalnewstoday.com/directory/c-d",
       "https://www.medicalnewstoday.com/directory/e-g",
       "https://www.medicalnewstoday.com/directory/h-l",
       "https://www.medicalnewstoday.com/directory/m-o",
       "https://www.medicalnewstoday.com/directory/p-r",
       "https://www.medicalnewstoday.com/directory/s-z",]

for url in urls:
    get_data(url)
# get_data(url)
