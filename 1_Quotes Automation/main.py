from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

s=Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe ")
driver=webdriver.Chrome(service=s)

driver.get("https://quotes.toscrape.com/")
# time.sleep(50)

quotion=[]
names=[]

for page in range(1,6):
    url=f"https://quotes.toscrape.com/page/{page}/"
    driver.get(url)
    time.sleep(2)
    quotes=driver.find_elements(By.CLASS_NAME,"quote")
    for quote in quotes:
        text=quote.find_element(By.CLASS_NAME,"text").text
        quotion.append(text)

        authors=quote.find_element(By.CLASS_NAME,"author").text
        names.append(authors)
    height=driver.execute_script("return document.body.scrollHeight")  
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  
    time.sleep(5)
    df=pd.DataFrame({
    "Quotions":quotion,
    "Author Name":names
     })
    df.to_csv("Quotes.csv",index=False)


