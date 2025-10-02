from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

s = Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.imdb.com/chart/top/")
time.sleep(3)

wait = WebDriverWait(driver, 20)

# Sare movies select karna
movies = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")))

Names, Ratings, Years, Time_periods, Reviews = [], [], [], [], []

for movie in movies:
    try:
     
        name = movie.find_element(By.CSS_SELECTOR, "h3").text
        Names.append(name)
    except:
        Names.append("N/A")

    try:
       
        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text
        Ratings.append(rating)
    except:
        Ratings.append("N/A")

    try:

        meta = movie.find_elements(By.CSS_SELECTOR, "span.cli-title-metadata-item")
        if len(meta) > 0:
            Years.append(meta[0].text)
        else:
            Years.append("N/A")

        if len(meta) > 1:
            Time_periods.append(meta[1].text)
        else:
            Time_periods.append("N/A")
    except:
        Years.append("N/A")
        Time_periods.append("N/A")

    try:
    
        review = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--voteCount").text
        Reviews.append(review)
    except:
        Reviews.append("N/A")

# # Print results
# print("Names:", Names[:5])
# print("Ratings:", Ratings[:5])
# print("Years:", Years[:5])
# print("Durations:", Time_periods[:5])
# print("Reviews:", Reviews[:5])

df=pd.DataFrame({
    "Name":Names,
    "Rating":Ratings,
    "Year":Years,
    "Duration":Time_periods,
    "Reviews":Reviews
})
df.to_csv("IMDB Movies.csv",index=False)