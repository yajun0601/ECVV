import requests
from bs4 import BeautifulSoup
import time
import random
HOST = "http://www.ecvv.com{}"


def open_company_file(start):
    with open("file_cs-uri-stem_product_W3SVC.txt", 'r') as r:
        ret = r.readlines()[start + 1:]
    return ret


def open_products_file(start):
    with open("file_cs-uri-stem_product_W3SVC.txt", 'r') as r:
        ret = r.readlines()[start + 1:]
    return ret


def restart():
    with open("product_title.txt", "r") as r:
        line_numbers = r.readlines().__len__()
    return line_numbers


def get_title(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if "404.0" in soup.text:
        return "404"
    else:
        return soup.select("title")[0].text.strip()


def parse_line(line):
    return line.split(',')[1]


if __name__ == '__main__':
    with open('product_title.txt', 'a') as w:
        line_numbers = restart()
        print(line_numbers)
        url_list = open_products_file(line_numbers)
        for i in url_list:
            if "\"" in i:
                w.writelines("url wrong\r\n")
            else:
                url = HOST.format(parse_line(i))
                title = get_title(url)
                print(url,title)
                w.writelines(title + "\r\n")
            time.sleep(0.5+random.random()*5)

