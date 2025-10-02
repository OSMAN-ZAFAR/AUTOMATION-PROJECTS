from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
s=Service("C:/Users/MIAUZ/Downloads/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver=uc.Chrome(Service=s)
driver.get("http://www.google.com")
time.sleep(2)

search=driver.find_element(By.CLASS_NAME,"gLFyf")
search.send_keys("House of Dragon")
search.send_keys(Keys.ENTER)
# time.sleep(50)
wait=WebDriverWait(driver,20)

link=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div[12]/div[4]/div[1]/div[2]/div/div/div[10]/div/div/div/div[1]/div/div/span/a/h3")))
link.click()
time.sleep(2)

img=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/a")))
img.click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div[3]/div[1]").screenshot("C:/Users/MIAUZ/OneDrive/Pictures/Screenshots/House of Dragon.png")
time.sleep(2)

driver.quit()
print("project is completed !")