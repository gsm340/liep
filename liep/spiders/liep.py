import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from liep.items import LiepItem
import time



class Myspider(scrapy.Spider):
    name = 'liep'
    allowed_domains = ['liepin.com']
    bash_url = 'https://www.liepin.com/zhaopin/?pubTime=&jobTitles=100090&ckid=0035075c494caf9d&fromSearchBtn=2' \
               '&compkind=&isAnalysis=&init=-1&searchType=1&flushckid=1&dqs=&industryType=industry_01&jobKind' \
               '=&sortFlag=11&industries=040&salary=*&compscale=&key=&clean_condition=&headckid=641324baaa134e5d '
    bashurl = 'https://www.liepin.com/zhaopin/?pubTime=&jobTitles=100090&ckid=906925df342c6da0&fromSearchBtn=2' \
              '&compkind=&isAnalysis=&init=-1&searchType=1&dqs=&industryType=industry_01&jobKind=&sortFlag=11' \
              '&industries=040&salary=*&compscale=&clean_condition=&key=&headckid=641324baaa134e5d&curPage= '

    def start_requests(self):
        for i in range(0, 100):
            if i == 0:
                url = self.bash_url
                yield Request(url, self.parse)
            else:
                if (i % 2) == 0:
                    url = self.bash_url + '&curPage=' + str(i)
                    time.sleep(1)
                    yield Request(url, self.parse)
                else:
                    url = self.bash_url + str(i)
                    time.sleep(1)
                    yield Request(url, self.parse)

    def parse(self, response):
        item = LiepItem()
        soup = BeautifulSoup(response.text, 'lxml')
        list = soup.find_all(class_='sojob-item-main clearfix')
        for l in list:
            name = l.find('h3')['title'].replace('招聘', '')
            item['title'] = name
            info = l.find(class_='condition clearfix')['title'].split('_')
            ad = info[1].split('-')
            if '面议' not in info[0]:
                pa = info[0].replace('万', '').split('-')
                av = (int(pa[0]) + int(pa[1]))/2
                item['pay'] = av
            else:
                item['pay'] = info[0]
            item['addr'] = ad[0]
            item['edu'] = info[2]
            item['yex'] = info[3]
            yield item
