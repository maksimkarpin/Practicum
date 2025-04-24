import requests
print("Задание 01")#Получение данных с Википедии
def get_wikipedia_content(url):
    try:
        response=requests.get(url)
        x= response.status_code
        a=response.text


    except Exception:
        print(f"Ошибка при получении страницы. Статус код:{x}")
    return a
print(get_wikipedia_content("https://ru.wikipedia.org/w/api.php"))
print(get_wikipedia_content("https://ru.wikipedia.org/wiki/Python"))
print("Задание 02")#Получение текущего курса доллара
def curse(url):
    try:
        curs=requests.get(url)
        x=curs.status_code
        index=curs.text.find("Доллар США")
        index=curs.text.find('<td>', index)
        index_end=curs.text.find('</td>', index)
        dollar_rate=curs.text[index+4:index_end]
        a=(f"Текущий курс доллара: {dollar_rate}")
        return a
    except Exception:
        print( "Ошибка при выполнении запроса")
print(curse(" https://www.cbr.ru/currency_base/daily/"))