from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
s=Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver=uc.Chrome()
Product_name, Prices,Sales,Reviews=[],[],[],[]
for page in range(1,6):
    url=f"https://www.daraz.com.np/catalog/?page={page}&q=Men%20winter%20jackets&spm=a2a0e.tm80335409.search.d_go"
    driver.get(url)
    # time.sleep(60)
    names=driver.find_elements(By.CLASS_NAME,"RfADt")
    # print(len(names))
    
    prices=driver.find_elements(By.CLASS_NAME,"ooOxS")
    # print(len(prices))

    sales=driver.find_elements(By.CLASS_NAME,"_1cEkb")
    # print(len(sales))

    reviews=driver.find_elements(By.CLASS_NAME,"qzqFw")
    # print(len(reviews))

    from itertools import zip_longest
    for n,p,s,r in zip_longest(names,prices,sales,reviews):
        name=n.text if n else 'N/A'
        price=p.text if p else 'N/A'
        sale=s.text if s else 'Sales rate not available'
        review=r.text if r else 'Reviews are not available'

        Product_name.append(name)
        Prices.append(price)
        Sales.append(sale)
        Reviews.append(review)

import pandas as pd
df=pd.DataFrame({
        'Product Details':Product_name,
        'Prices':Prices,
        'Sales':Sales,
        'Reviews':Reviews
    })
df.to_csv("Jackets.csv",index=False)