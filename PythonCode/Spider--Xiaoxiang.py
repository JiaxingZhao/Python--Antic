import requests
import os
from GetFakeUserAgent import GetFakeAgent
from bs4 import BeautifulSoup


class StartSpider(object):
    """docstring for StartSpider"""

    def __init__(self, base_url, save_path='./'):
        self.headers = GetFakeAgent.get_agent()
        self.base_url = base_url
        self.save_path = save_path
        self.book_name = ''

    def start_req(self, url):
        self.parse_page(url)

    def get_soup(self, url):
        req = requests.get(url, headers=self.headers)
        if req.status_code == 200:
            return BeautifulSoup(req.text, 'lxml')

    def parse_page(self, url):
        soup = self.get_soup(url)
        book_list = soup.find_all('h4')
        for book in book_list:
            self.book_name = book.a.text
            book_id = book.a['href'].replace('/info/', '').replace('.html', '')
            self.get_chapter(book_id)

    def get_chapter(self, book_id):
        url = "http://www.xxsy.net/partview/GetChapterList?bookid=" + \
            book_id + "&noNeedBuy=1&special=0"
        soup = self.get_soup(url)
        chapter_list = soup.find_all('a')
        for chapter in chapter_list:
            chapter_url = chapter['href']
            chapter_name = chapter.text
            self.get_chapter_text(chapter_url, chapter_name)

    def get_chapter_text(self, url, name):
        soup = self.get_soup(self.base_url + url)
        text_list = soup.select('.chapter-main p')
        self.save_text(text_list, name)

    def save_text(self, lines_list, name):
        book_path = self.save_path + self.book_name
        if not os.path.exists(book_path):
            os.mkdir(book_path)
        print('正在保存{}:{}'.format(self.save_path.rsplit('/', 1)[1], name))
        with open(book_path + '/' + name + '.txt', 'w') as f:
            for line in lines_list:
                if '本书由潇湘书院首发，请勿转载' not in line.text:
                    f.write(line.text + '\r\n')


if __name__ == '__main__':
    book_url = 'http://www.xxsy.net/search?vip=0&sort=2'
    base_url = 'http://www.xxsy.net'
    save_path = './xiaoshuo/'
    startspider = StartSpider(base_url, save_path)
    startspider.start_req(book_url)
