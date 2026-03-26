from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/anusi/Desktop/portfolio/index.html")

time.sleep(2)

print("Title:", driver.find_element(By.ID, "title").text)

driver.find_element(By.LINK_TEXT, "About").click()
time.sleep(2)

print("About:", driver.find_element(By.ID, "aboutText").text)

# KEEP BROWSER OPEN
input("Press Enter to close browser...")

driver.quit()