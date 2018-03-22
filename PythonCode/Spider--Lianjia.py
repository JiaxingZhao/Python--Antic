from bs4 import BeautifulSoup
from urllib import request
from http import cookiejar
import gzip
import csv


class WebSpider(object):
    """docstring for WebSpider"""

    def __init__(self, spath='./', baseurl='', headinfo=None, info=None, url_name=None):
        # 定义初始属性
        ck = cookiejar.CookieJar()
        cookie = request.HTTPCookieProcessor(ck)
        httphd = request.HTTPHandler(debuglevel=0)
        httpshd = request.HTTPSHandler(debuglevel=0)
        self.opener = request.build_opener(httphd, httpshd, cookie)
        self.spath = spath
        self.baseurl = baseurl
        self.headinfo = headinfo
        self.search_name = info
        self.frist_write = True
        self.rec_list = []
        self.web_site = ""
        self.url_name = url_name
        self.page_num = 1

    def start(self, url):
        # 得到地址，使用HttpRequest.get_request得到页面信息
        # 得到返回值后进行页面解析
        req = self.get_request(url)
        if req:
            self.parse_page(req)

    def get_request(self, url):
        reqhd = request.Request(url, headers=self.headinfo)
        req = self.opener.open(reqhd)
        if req.code == 200:
            con = req.read()
            con = gzip.decompress(con)
            con = con.decode('utf-8')
            return con
        else:
            print('someting wrong! maybe need check! ')

    def parse_page(self, obj):
        # 解析页面，得到相关信息
        # 保存页面
        obj = BeautifulSoup(obj, 'lxml')
        house_list = obj.find_all('a', attrs={'data-el': 'ershoufang',
                                              'class': 'img '})
        for item in house_list:
            if item['href'] not in self.rec_list:
                house_obj = self.get_request(item['href'])
                self.get_detail(house_obj)
                print("进入链接:", item['href'])
                self.rec_list.append(item['href'])
            else:
                print("本次搜索区域所有房屋探索完毕，程序运行结束，请检查结果。")
                break
        next_page = self.get_next_page(obj)
        if next_page:
            self.start(next_page)

    def get_detail(self, obj):
        # 得到页面，处理信息
        # 获取顶部信息
        house_details = []

        obj = BeautifulSoup(obj, 'lxml')
        content = obj.find('div', attrs={'class': 'content'})
        removelist = ['关注房源', '下载链家APP', '房源动态早知道', '预约看房', '已加入待看']
        title_info = [x for x in content.text.split(
            '\n') if x.strip() and x not in removelist]
        print('开始探索新房源:', title_info[0])

        # 价格信息
        price_info = obj.find("div", class_='price').text.replace(
            '正在获取首付和月供...', '').replace('万', '万!!').replace(
            ' 首付及税费情况请咨询经纪人 ', '').split('!!')

        # 房屋信息
        obj.select('.aroundInfo .label')
        house_info = []
        for item in obj.select('.aroundInfo .label'):
            house_info += item.next_sibling.text.replace(
                '举报', '').split('\xa0')

        # 基本信息
        baseinfo = obj.find('div', attrs={'class': 'newwrap baseinform'})
        base_info = []
        for item in baseinfo.find_all('span', class_='label'):
            item = item.parent.text.replace('\n', '')
            base_info.append(item[4:].strip())

        # 更多信息
        basemore = obj.find(
            'div', attrs={'class': 'introContent showbasemore'})
        more_info = []
        for item in basemore.findAll('div', class_='baseattribute clear'):
            item = item.text.replace('\n', '').replace(' ', '')
            if not item[:4] == '核心卖点':
                more_info.append(item[4:].strip())

        # 经纪人信息
        broker_info = obj.find('div', attrs={'class': 'brokerInfoText fr'})
        broker_info = broker_info.text.replace('微信扫码拨号', '').replace(
            '400', '链家400').replace('/', '链家').split('链家')

        house_details += title_info
        house_details += price_info
        house_details += house_info
        house_details += base_info
        # house_details += more_info
        house_details += broker_info

        self.save_page(house_details)

    def save_page(self, obj):
        # 得到页面信息
        # 保存
        # f = open(self.spath + '链家房源信息.txt', 'a+')
        # f.write(str(obj) + '\r\n')
        # f.close()

        csvfile = open(self.spath + 'lianjia.csv', 'a+')
        writer = csv.writer(csvfile)
        if self.frist_write:
            writer.writerow(['标题', '特色卖点', '关注人数', '看房人数', '售价', '平方单价',
                             '小区名称', '二级区域', '三级区域', '四级区域', '看房时间',
                             '链家编号', '房屋户型', '所在楼层', '建筑面积', '户型结构',
                             '套内面积', '建筑类型', '房屋朝向', '建筑结构', '装修情况',
                             '梯户比例', '供暖方式', '配备电梯', '产权年限', '挂牌时间',
                             '交易权属', '上次交易', '房屋用途', '房屋年限', '产权所属',
                             '抵押信息', '房本备件', '经纪人姓名', '经纪人评分', '评价人数',
                             '经纪人电话'])
            self.frist_write = False
        writer.writerow(obj)
        csvfile.close()

    def get_next_page(self, obj):
        # 得到下一页信息
        if self.web_site == '':
            self.web_site = obj.find('a', string=self.search_name)['href']
        self.page_num += 1
        next_page = self.baseurl + 'pg' + \
            str(self.page_num) + 'rs' + self.url_name
        if self.web_site:
            print("本页房源探索完毕，进入第", self.page_num, "页继续进行探索...")
            return next_page


if __name__ == '__main__':
    info = input("要搜索的内容：")
    url_name = request.quote(info)
    headinfo = {
        # 'Host': 'www.lagou.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://bj.lianjia.com/ershoufang/rs' + url_name + '/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    baseurl = 'http://bj.lianjia.com/ershoufang/'
    requrl = "http://bj.lianjia.com/ershoufang/rs" + url_name
    path = './lianjia/'
    webspider = WebSpider(path, baseurl, headinfo, info, url_name)
    webspider.start(requrl)
