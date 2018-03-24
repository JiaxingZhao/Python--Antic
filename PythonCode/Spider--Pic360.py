import requests
from urllib import request
import os
from fake_useragent import FakeUserAgent


class GetFakeAgent(object):
    """docstring for GetFakeAgent"""

    @staticmethod
    def get_agent(choice='random'):
        # 获取伪装Agent
        ua = FakeUserAgent()
        browser = {'safari': ua.safari,
                   'random': ua.random,
                   'chrome': ua.chrome,
                   'ie': ua.internetexplorer,
                   'opera': ua.opera,
                   'firefox': ua.firefox}
        return {'User-Agent': browser[choice]}


class StartSpider(object):
    """docstring for StartSpider"""

    def __init__(self, info, spath='./360pic/', sn=0, size='small'):
        self.payload = {'q': info,
                        'correct': info,
                        'pn': 60,
                        'sn': sn,
                        'kn': 16,
                        }
        self.requrl = 'http://image.so.com/j'
        self.picsize = size
        self.spath = spath

    def get_request(self):
        headers = GetFakeAgent.get_agent()
        req360 = requests.get(self.requrl,
                              params=self.payload,
                              headers=headers)
        if req360.status_code == 200:
            self.parse_json(req360)
        else:
            print("Status Code is not 200, please check it.")

    def parse_json(self, obj):
        image_list = obj.json()['list']
        for pic in image_list:
            pic_url = pic['_thumb'] if self.picsize == 'small' else pic['img']
            pic_name = pic['id'] + '.' + pic_url.rsplit('.', 1)[1]
            self.save_pic(pic_url, pic_name)

    def save_pic(self, url, name):
        if not os.path.exists(self.spath):
            os.mkdir(self.spath)
        print('Download: ', name)
        try:
            request.urlretrieve(url, self.spath + name)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    search_info = "大头照"
    start_num = 136  # 默认自起始值开始请求60页，但实际请求数量不确定
    picsize = 'small'  # small为缩略图，large为原图
    spath = './360pic/'
    startspider = StartSpider(search_info, spath, start_num, picsize)
    startspider.get_request()
