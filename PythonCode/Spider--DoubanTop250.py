import re
import os
from urllib import request


class HttpRequest(object):
    """docstring for UrllibRequest"""

    def urllib_request(self, url):
        # 使用urlopen打开url并赋值给req
        req = request.urlopen(url)
        # 得到返回的code状态码
        if req.code == 200:
            # 如果200成功，读取页面信息，赋值给context
            print("连接成功...")
            context = req.read()
            # 将context返回出去
            return context


class DoubanSpider(object):
    """docstring for DoubanSpider"""

    def __init__(self, spath='./', baseurl=""):
        self.spath = spath
        self.baseurl = baseurl

    def start_req_url(self, url):
        # 调用HttpRequest.urllib_request，会返回context
        page = HttpRequest().urllib_request(url)
        # 如果返回context为真，即得到了context数据
        if page:
            # 将context解码重新赋值给context
            context = page.decode('utf-8')
            # 获取当前页面需要的信息并进行处理
            self.parse_page(context)
            # 完成信息处理后获取下一页信息，使用正则获取
            nexturl = self.get_next_page(context)
            # 如果有下一页，则重新调用start_req_url方法，将下一页的url传入
            if nexturl:
                self.start_req_url(nexturl)
            else:
                print("所有连接获取完毕，请检查结果")

    def parse_page(self, context):
        # 使用正则获取标题和图片链接
        target = re.findall(r'alt="(.+)" src="(.+)" cl', context)
        # 使用if判断是否获取
        if target:
            # 如果获取到内容，使用name和url接收
            for name, url in target:
                # 提升人类友善度，获取url最后的格式结尾并追加给name
                tail = url.rsplit('.', 1)[1]
                name += '.' + tail
                # 调用saveImage保存文件，传入url和修改后的name
                self.save_image(name, url)

    def save_image(self, name, url):
        print('当前正在获取:', name)
        # 考虑多平台使用，使用os.path.join将路径和文件名拼接
        filepath = os.path.join(self.spath, name)
        # 使用urlretrieve保存文件
        request.urlretrieve(url, filepath)

    def get_next_page(self, context):
        # 使用正则获取下一页的链接
        nextpage = re.search('<a href="(.*)" >后页', context)
        # 使用if判断链接是否被抓取到
        if nextpage:
            # 如果有下一页，将下一页信息返回出去
            return self.baseurl + nextpage.groups()[0]


if __name__ == '__main__':
    requrl = "https://movie.douban.com/top250"
    spath = '/home/ubuntu/spider/douban250/'
    doubanspider = DoubanSpider(spath, requrl)
    doubanspider.start_req_url(requrl)
