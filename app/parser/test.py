from selenium import webdriver
from bs4 import BeautifulSoup as bs
import undetected_chromedriver
import time

url1 = 'https://mosmetro.ru/news'
url2 = 'https://ya.ru'
url3 = 'https://google.ru'
options = webdriver.ChromeOptions()
options.add_argument("user-agent=HelloWord:)")
driver = undetected_chromedriver.Chrome(options)

try:
    driver.get(url=url1)
    time.sleep(5)
    source_data = driver.page_source
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
soup = bs(source_data)
print(soup)