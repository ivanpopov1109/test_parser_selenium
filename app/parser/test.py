from selenium import webdriver
from bs4 import BeautifulSoup as bs
import undetected_chromedriver
import time
from typing import List, Dict
import re


class Parser:
    URL = "https://mosmetro.ru"

    @classmethod
    def get_soup(cls):
        options = webdriver.ChromeOptions()
        driver = undetected_chromedriver.Chrome(options)
        try:
            driver.get(url=Parser.URL)
            time.sleep(10)
            source_data = driver.page_source
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
        return source_data

    @classmethod
    def create_file_with_html(cls, html):
        with open("index.html", "w") as file:
            file.write(html)
    @classmethod
    def get_news(cls, file: str):
        with open(f'{file}') as file:
            src = file.read()
        soup = bs(src)
        all_news_on_page = soup.find("div",
                                     class_="swiper-container swiper-3 swiper-container-initialized swiper-container-horizontal").find_all(
            'a')
        news: List[Dict] = []
        for i in all_news_on_page:
            style_with_url = i.find('div', class_="news-card__image")['style']
            pattern = "(?:\(['\"]?)(.*?)(?:['\"]?\))"
            url = re.search(pattern, style_with_url).group(1)
            dict = {'title': i.find('div', class_="news-card__caption").text,
                    'url': url,
                    'date': i.find('div', class_="news-card__date").text}
            news.append(dict)
        return news


# html = Parser.get_soup()
# Parser.create_file_with_html(html)
print(Parser.get_news('index.html'))

