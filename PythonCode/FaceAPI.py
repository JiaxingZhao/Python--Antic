import requests
import os
import mimetypes
import csv
from fake_useragent import FakeUserAgent


class GetFakeAgent(object):
    """docstring for GetFakeAgent"""

    @staticmethod
    def get_agent(choice='random'):
        # 获取伪装Agent
        ua = FakeUserAgent()
        browser = {'ie': ua.internetexplorer,
                   'opera': ua.opera,
                   'safari': ua.safari,
                   'random': ua.random,
                   'chrome': ua.chrome,
                   'firefox': ua.firefox
                   }
        return {'User-Agent': browser[choice]}


class FaceApi(object):
    """docstring for FaceApi"""

    def __init__(self, spath, attrs='gender,age'):
        self.attrs = attrs
        self.spath = spath
        self.frist_write = True
        self.faceurl = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
        self.payload = {'api_key': 'your_api_key',
                        'api_secret': 'your_api_secret',
                        'return_attributes': self.attrs}
        self.headers = GetFakeAgent.get_agent()
        self.info_dict = {'pic': '',
                          "width": '',
                          "top": '',
                          "left": '',
                          "height": ''}

    def get_result(self):
        file_list = os.listdir(self.spath)
        if len(file_list) > 0:
            for file in file_list:
                self.request_api(self.spath + file)

    def request_api(self, file):
        fname = file
        bname = os.path.basename(fname)
        ftype = mimetypes.guess_type(fname)[0]
        files = {'image_file': (bname, open(fname, 'rb'), ftype)}
        req = requests.post(self.faceurl,
                            data=self.payload,
                            headers=self.headers,
                            files=files)
        self.parse_json(req, bname)

    def parse_json(self, obj, bname):
        json = obj.json()
        info_dict = {'pic': '',
                     "width": '',
                     "top": '',
                     "left": '',
                     "height": ''}
        for key in info_dict.keys():
            if key == 'pic':
                info_dict[key] = bname
            else:
                info_dict[key] = json['faces'][0]['face_rectangle'][key]
        for attr in self.attrs.replace(' ', '').split(','):
            info_dict.update(
                {attr: json['faces'][0]['attributes'][attr]['value']})
        print(bname, '获取完毕，正在保存...')
        self.save_info(info_dict)

    def save_info(self, obj):
        with open(self.spath + 'result.csv', 'a+') as csvfile:
            writer = csv.writer(csvfile)
            if self.frist_write:
                writer.writerow(['图片名', 'width', 'top', 'left', 'height'] +
                                self.attrs.replace(' ', '').split(','))
                self.frist_write = False
            writer.writerow(list(obj.values()))


if __name__ == '__main__':
    spath = './360pic/'
    attrs = 'gender,age'
    faceapi = FaceApi(spath, attrs)
    faceapi.get_result()
