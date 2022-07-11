import requests
from bs4 import BeautifulSoup


class NewsParser:

    def __init__(self):
        self.news = []

    def parse(self, url='https://www.rbc.ru/short_news'):

        req = requests.get(url)

        soup = BeautifulSoup(req.text, 'html.parser')

        if url == 'https://www.rbc.ru/short_news':
            self.news = []

            tags = soup.find_all("div", "item__wrap l-col-center")

            for tag in tags:
                title = tag.find("span", "item__title rm-cm-item-text").text
                heading = tag.find("a", "item__category").text.replace(",", "")
                link = tag.find("a", "item__link")['href']
                if title is not None:
                    if heading is not None:
                        heading = heading.strip()
                    item = {'title': title.strip(), 'time': tag.find("span", "item__category").text,
                            'heading': heading, 'link': link}
                self.news.append(item)
        else:
            tags = soup.find_all("p")
            text = ''
            for tag in tags:
                if tag.text != '' and tag.text[0] != '\n':
                    text += tag.text + '\n'
            if len(text) > 4096:
                return text[:4093] + '...'
            else:
                return text

    def save(self):
        f = open("digest.txt", "w")
        for item in self.news:
            f.write(item['title'] + ", " + item['time'] + ", " + item['heading'] + "\n")
        f.close()

    def print_all(self):
        for item in self.news:
            print(item['title'] + ", " + item['time'] + ", " + item['heading'])

    def get_news(self):
        return self.news

    def get_detailed(self, index):
        url = self.news[index]['link']
        return self.parse(url)


