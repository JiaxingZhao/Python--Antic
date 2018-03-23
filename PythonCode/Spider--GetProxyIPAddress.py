from fake_useragent import FakeUserAgent
from urllib import request
from bs4 import BeautifulSoup
# from threading import Thread
from multiprocessing import Pool


class GetFakeAgent(object):

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


class GetProxyIP(object):

    def __init__(self, save_path='./'):
        self.save_path = save_path

    def get_proxy(self, url, choice='random'):
        headers = GetFakeAgent.get_agent(choice)
        req_hd = request.Request(url, headers=headers)
        req = request.urlopen(req_hd)
        if req.code == 200:
            self.parse_page(req)

    def parse_page(self, obj):
        if obj:
            con = BeautifulSoup(obj, 'html5lib')
            ip_text = con.body.text.split('\n\t\n\n\n')
            proxy_ip_list = ip_text[0].split("\n\t\t")
            if len(proxy_ip_list) > 0:
                checked_list = []
                pools = Pool(5)
                for ip in proxy_ip_list:
                    checked_list.append(
                        pools.apply_async(
                            self.check_proxy, (ip,)))
                pools.close()
                pools.join()
                self.save_proxy(checked_list)
            else:
                print('没有获取到ip信息，请检查...')

    def save_proxy(self, checked_list):
        with open(self.save_path + "proxylist.txt", 'w+') as f:
            for ip in checked_list:
                ip = ip.get()
                if ip:
                    f.write(ip + '\r\n')
        with open(self.save_path + "proxylist.txt", 'r+') as f:
            count = len(f.readlines())
        if count == 0:
            print('没有可用的代理，请重新获取...')
        else:
            print('获取了{}个可用代理，请检查结果...'.format(count))

    def check_proxy(self, ip, site='httpbin'):
        check_site = {'httpbin': 'http://httpbin.org/get',
                      'ip138': 'http://2017.ip138.com/ic.asp'}
        proxy_hd = request.ProxyHandler({'http': ip})
        opener = request.build_opener(proxy_hd)
        try:
            req = opener.open(check_site[site], timeout=1)
            print(ip, '验证成功')
            return ip
        except Exception as e:
            pass


if __name__ == '__main__':
    save_path = './'
    how_many = input('获取多少代理ip? :')
    proxy_site = 'http://www.66ip.cn/mo.php?sxb=&tqsl=' + how_many
    get_proxy_ip = GetProxyIP(save_path)
    get_proxy_ip.get_proxy(proxy_site, 'random')
