import re
import os
from bs4 import BeautifulSoup
from urllib import request
from threading import Thread


class HttpRequest(object):
    """docstring for HttpRequest"""

    @staticmethod
    def request_url(url):
        # 得到url地址，进行连接
        # 判断是否链接成功，如果成功，获取内容并返回

        url_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        req = request.Request(url)
        req.add_header('User-Agent', url_agent)
        req = request.urlopen(req)
        if req.code == 200:
            context = req.read()
            return context
        else:
            print('code==', req.code)


class StartSpider(object):
    """docstring for StartSpider"""

    def __init__(self, spath="d:/", baseurl=''):
        self.spath = spath
        self.baseurl = baseurl
        self.download_list = []

    def start(self, url):
        # 连接网页，返回内容
        # 判断内容
        # 如果有内容，开爬
        # 下载后判断是否有下一页，有的话进入继续爬
        # 如果没有下一页，进入下一套图，继续爬
        page = HttpRequest.request_url(url)
        if page:
            context = BeautifulSoup(page, 'lxml')
            if url not in self.download_list:
                self.parse_page(context)
                self.download_list.append(url)
            next_page = self.get_next_page(context)
            if next_page:
                self.start(next_page)

    def parse_page(self, context):
        # 分析网页中的文件
        # 如果文件存在，调用下载函数下载
        title = list(context.h1.strings)[0]
        retitle = title.replace('(', '.').replace(')', '.')
        retitle = title.replace('[', '.').replace(']', '.')
        pic_list = context.find_all(alt=re.compile(retitle))
        for pic in pic_list:
            try:
                picurl = pic['src']
                picname = picurl.rsplit('/', 1)[1]
                Thread(target=self.save_image, args=(
                    title, picurl, picname)).start()
            except Exception as e:
                print('有图片src错误')
            # self.save_image(title, picurl, picname)

    def save_image(self, title, url, name):
        # 得到要下载的连接和名字
        # 保存
        print('正在保存：%s图集的%s' % (title, name))
        if not os.path.exists('d:/aitaotu/' + title):
            os.mkdir('d:/aitaotu/' + title)
        file = os.path.join(self.spath, title, name)
        request.urlretrieve(url, file)

    def get_next_page(self, context):
        # 分析链接，判断是否有下一页
        # 有的话将下一页链接返回
        # 如果没有的话，将下一套图链接返回
        a = context.find('a', string='下一页')
        b = context.find(class_='preandnext connext')
        next_page = a['href'] if a else b.a['href'] if b else ''
        if next_page:
            go_next = self.baseurl + next_page
            return go_next


if __name__ == '__main__':
    baseurl = 'https://www.aitaotu.com'
    targeturl = 'https://www.aitaotu.com/guonei/34463.html'
    filepath = 'd:/aitaotu/'
    startspider = StartSpider(filepath, baseurl)
    startspider.start(targeturl)
