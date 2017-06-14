from .sql import Sql
from lp.items import LpItem


class LpPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, LpItem):
            title = item['title']
            area = item['area']
            edu =item['edu']
            exp = item['exp']
            salary = item['salary']
            stype = item['stype']
            comname = item['comname']
            welfarekey = item['welfarekey']
            print('开始存储job')
            Sql.insert_lp(title, area, edu, exp, salary, stype, comname, welfarekey)

        #deferToThread(self._process_item, item, spider)



