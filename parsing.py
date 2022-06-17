import requests
from bs4 import BeautifulSoup


class NewsParser:

    def __init__(self):
        self.news = []

    def parse(self):
        url = 'https://www.rbc.ru/short_news'

        req = requests.get(url)

        soup = BeautifulSoup(req.text, 'html.parser')

        tags = soup.find_all("div", "item__wrap l-col-center")
        self.news = []

        for tag in tags:
            title = tag.find("span", "item__title rm-cm-item-text").text
            heading = tag.find("a", "item__category").text.replace(",", "")
            if title is not None:
                if heading is not None:
                    heading = heading.strip()
                item = {'title': title.strip(), 'time': tag.find("span", "item__category").text,
                        'heading': heading}
            self.news.append(item)

    def save(self):
        f = open("digest.txt", "w")
        for item in self.news:
            f.write(item['title'] + ", " + item['time'] + ", " + item['heading'] + "\n")
        f.close()

    def print_all(self):
        for item in self.news:
            print(item['title'] + ", " + item['time'] + ", " + item['heading'])



