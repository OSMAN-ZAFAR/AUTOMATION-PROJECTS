from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
s=Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.bbc.com/news")
# time.sleep(50)
Links=[]
Decs=[]
UpDates=[]
Catagries=[]

links=driver.find_elements(By.XPATH,"//h2[@data-testid='card-headline']")

decs=driver.find_elements(By.XPATH,"//p[@data-testid='card-description']")

last_updates=driver.find_elements(By.XPATH,"//span[@data-testid='card-metadata-lastupdated']")

catagries=driver.find_elements(By.XPATH,"//span[@data-testid='card-metadata-tag']")
from itertools import zip_longest
for l,d,u,c in zip_longest(links,decs,last_updates,catagries,fillvalue=None):
    link=l.text.strip() if l else "N/A"
    dec=d.text.strip() if d else "Summary is not given"
    last_update=u.text.strip() if u else "Last update is no given"
    catagroy=c.text.strip() if c else "Catagory is not given"

    Links.append(link)
    Decs.append(dec)
    UpDates.append(last_update)
    Catagries.append(catagroy)

# print(len(Links))
# print(len(Decs))
# print(len(UpDates))
# print(len(Catagries))

import pandas as pd
df=pd.DataFrame({
    "HeadLines":Links,
    "Summary":Decs,
    "Updates":UpDates,
    "Catagries":Catagries
})
# print(df)
df.to_csv("News from BBC.csv",index=False)