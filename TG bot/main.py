import requests
import re
from bs4 import BeautifulSoup


def get_name_to_look():

    name_to_look = input('Введите наименование искомого товара: ')
    return name_to_look

def pars_wild(name_to_look):

    #name_to_look = input('Введите наименование искомого товара: ')
    url_to_look = f'https://www.wildberries.ru/catalog/0/search.aspx?search={name_to_look}&search=true'
    response = requests.get(url_to_look)
    rows_data = BeautifulSoup(response.text, 'lxml').find_all('div', class_='dtList i-dtList j-card-item no-left-part')
    #print(rows_data)

    for element in rows_data:
        item = element.find_all('div', class_='l_class')
        id_item = re.findall()
    print(item)


pars_wild(get_name_to_look())


