import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from lp.items import LpItem
import time


class Myspider(scrapy.Spider):
    name = 'lp'
    allowed_domains = ['www.liepin.com']
    bash_url = 'https://www.liepin.com/zhaopin/?industries=040&dqs=&salary=*&jobKind=&pubTime=&compkind=&compscale=&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=11&flushckid=0&fromSearchBtn=1&headckid=1a311ce5c59a8ce9&key='
    bashurl = ''
    key = ['ios', 'php', 'python', 'java', '.net', 'android', 'c/c++']

    def start_requests(self):
        # url = self.bash_url + self.key[6]
        for i in range(7):
            url = self.bash_url + self.key[i]
            yield Request(url, self.parse)
        # yield Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = LpItem()
        # 获取页码信息
        c = soup.find(class_='current').get_text()
        print(c)
        pagerflag = soup.find(class_='addition').previous_sibling.previous_sibling
        url = pagerflag['href']

        stype = soup.find(class_='input-main').contents[3]['value']
        list = soup.find_all(class_='sojob-item-main clearfix')
        for l in list:
            name = l.find('h3')['title'].replace('招聘', '')
            item['title'] = name
            info = l.find(class_='condition clearfix')['title'].split('_')
            ad = info[1].split('-')
            if '万' in info[0]:
                pa = info[0].replace('万', '').split('-')
                av = (int(pa[0]) + int(pa[1])) / 2
                item['salary'] = av
            else:
                item['salary'] = info[0]
            item['area'] = ad[0]
            item['edu'] = info[2]
            item['exp'] = info[3]
            item['stype'] = stype
            item['comname'] = l.find(class_='company-name').find('a').get_text()
            wel = l.find(class_='temptation clearfix')
            if None == wel:
                item['welfarekey'] = '暂无福利关键词'
            else:
                item['welfarekey'] = wel.get_text().replace("\n", "1")
            yield item

        if 'javascript:;' in url:  # 判断解析页面码
            print('到达%s末页，停止该系列' % stype)
            return
        else:
            time.sleep(2)
            yield Request(url, self.parse)
