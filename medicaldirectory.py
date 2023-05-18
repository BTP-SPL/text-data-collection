
#  import the library utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import json




#  store the class ids for different classes
class_ids = {
        "article" :"css-8sm3l3", # class for the articles
        "article_heading" : "css-1xlgwie", # class for the article heading
        "article_text" : "css-onvglr" # class for the article text
}

# url = "https://www.medicalnewstoday.com/directory/a-b" # url of the website
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
        os.mkdir("try")
    except:
        print("Error: Directory already exists")
        # return

    # for each tab get the categories
    # category is text after last '/' in url 
    url2 = url
    category_name = url2.split('/')[-1]

         #replace '/' and ':' with '-'
    category_name = category_name.replace('/', '-')
    category_name = category_name.replace(':', '-')

    try:
      os.mkdir("try/{}".format(category_name))
    except:
      print("11")
      print("Error: Directory already exists")
      return

    sleep(2)
    articles = driver.find_elements(By.CLASS_NAME, class_ids["article"])
    sleep(10)
    text_to_be_found = []
    i = 0
    articles = driver.find_elements(By.CLASS_NAME, class_ids["article"])
    
    for article in articles:
        i+=1
    # highlight the element
        article = driver.find_elements(By.CLASS_NAME, class_ids["article"])[i-1]
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", article, "background: yellow; border: 2px solid red;")
        # print(article.text)
        heading = article.find_element(By.CLASS_NAME, class_ids["article_heading"])
        # print(heading.text)
        text = article.find_element(By.CLASS_NAME, class_ids["article_text"])
        text_to_be_found.append({"heading": heading.text, "text": text.text})
        # scroll 
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", article, "background: none; border: none;") 
        driver.execute_script("arguments[0].scrollIntoView();", article)    
        sleep(2)
       
       
    j = 0
    for text in text_to_be_found:
        print(text)
        f = open('try/{}/{}.json'.format(category_name,j), 'x')   
        j+=1
        json.dump(text, f)
        f.close()
    print("going back")
    driver.get(url)
        
    sleep(3)
    driver.quit()
urls = [
       "https://www.medicalnewstoday.com/alzheimers-and-dementia",
       "https://www.medicalnewstoday.com/coronavirus?correlationId=2b137d5a-dcfb-464e-9ea6-72c5a54b4e92",
        "https://www.medicalnewstoday.com/hiv-and-aids",
        "https://www.medicalnewstoday.com/nutrition",
        "https://www.medicalnewstoday.com/anxiety",
        "https://www.medicalnewstoday.com/diabetes"
        "https://www.medicalnewstoday.com/human-biology",
        "https://www.medicalnewstoday.com/parkinsons-disease"
        ,"https://www.medicalnewstoday.com/asthma-and-allergies",
        "https://www.medicalnewstoday.com/human-biology",
        "https://www.medicalnewstoday.com/diabetes",
        "https://www.medicalnewstoday.com/environment-and-sustainability",
        "https://www.medicalnewstoday.com/leukemia",
        "https://www.medicalnewstoday.com/program/a-deeper-look-at-psoriasis",
        "https://www.medicalnewstoday.com/LGBTQIA",
        "https://www.medicalnewstoday.com/sexual-health",
        "https://www.medicalnewstoday.com/breast-cancer",
        "https://www.medicalnewstoday.com/cardiovascular-health",
        "https://www.medicalnewstoday.com/health-equity",
        "https://www.medicalnewstoday.com/program/investigating-ulcerative-colitis",
        "https://www.medicalnewstoday.com/womens-health"
    ] 

for url in urls:
  get_data(url)