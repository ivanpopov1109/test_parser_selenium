# test_parser_selenium
FastApi, docker, Postgres


Написать API, которое получает новости за заданный период из базы
и парсер который каждые 10 минут парсит новости
с сайта https://mosmetro.ru/news
(достаточно будет просто взять те новости что есть при первой загрузке)
и сохраняет в базу с меткой когда эти новости спаршены, 

пример метода
/metro/news?day=5

в качестве ответа вернуть JSON новости которые опубликованы за последний 5 дней (включительно) 
заголовок 
url картинки
дата публикации (YYYY-mm-dd)

