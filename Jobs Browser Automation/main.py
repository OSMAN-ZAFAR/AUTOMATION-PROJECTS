from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pandas as pd
import time
s=Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver=uc.Chrome()
driver.get("https://pk.indeed.com/")
time.sleep(30)

Title=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/span/div[4]/div[1]/div/div/div/div/div/form/div/div[1]/div/div[1]/div/div/span/input")
Title.send_keys("Software Engineer")
Title.send_keys(Keys.TAB)

Loc=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/span/div[4]/div[1]/div/div/div/div/div/form/div/div[1]/div/div[3]/div/div/span/input")
Loc.send_keys("Lahore")
Loc.send_keys(Keys.TAB)
find=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/span/div[4]/div[1]/div/div/div/div/div/form/div/div[2]/button")
find.click()
time.sleep(30)

Jobs,Companies,Salaries,Apply_Links=[],[],[],[]
page=0
while True:
	page+=1
	jobs = driver.find_elements(By.CSS_SELECTOR, ".jobTitle")
	# print(len(Job))

	companies = driver.find_elements(By.CSS_SELECTOR, ".css-1ssrdda")

	salaries = driver.find_elements(By.CSS_SELECTOR, ".mosaic-provider-jobcards-1f1q1js")

	from itertools import zip_longest
	for j, c, s in zip_longest(jobs, companies, salaries,  fillvalue=None):
		job = j.text if j else "N/A"
		company = c.text if c else " Company name is not given"
		salary = s.text if s else "Salary is not given"
		link = j.find_element(By.TAG_NAME, "a").get_attribute("href") if j else "Link not available"

		Jobs.append(job)
		Companies.append(company)
		Salaries.append(salary)
		Apply_Links.append(link)
	if page >= 10:
		break
	try:
		wait = WebDriverWait(driver, 20)
		next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Next Page']")))
		next_page.click()
		time.sleep(30)
	except:
		print("No more pages left")
		break
df=pd.DataFrame({
	"Tittle":Jobs,
	"Company Name":Companies,
	"Salary":Salaries,
	"Link":Apply_Links
})
df.to_csv("Jobs Details.csv",index=False)



