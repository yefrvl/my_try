import requests
from bs4 import BeautifulSoup


def get_name_to_look():

    name_to_look = input('Введите наименование искомого товара: ')
    return name_to_look

def pars_wild(name_to_look):

#    name_to_look = input('Введите наименование искомого товара: ')
    url_to_look = f'https://www.wildberries.ru/catalog/0/search.aspx?search={name_to_look}&search=true'
    response = requests.get(url_to_look)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)

pars_wild(get_name_to_look())
