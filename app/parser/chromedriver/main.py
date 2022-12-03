from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='/home/ivan/python_Lesson/My_projects/parsing_projects/test_selenium/chromedriver/chromedriver')
url = "https://ya.ru/"
driver.get(url=url)
# get_url = driver.current_url
# print("The current url is:"+str(get_url))
# driver.quit()
#
# driver.close()
# driver.quit()
#
driver.get("https://www.google.com")
get_url = driver.current_url

