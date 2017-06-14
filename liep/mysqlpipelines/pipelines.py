from .sql import Sql
from liep.items import LiepItem


class LiepPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, LiepItem):
            title = item['title']
            addr = item['addr']
            edu =item['edu']
            yex = item['yex']
            pay = item['pay']
            Sql.insert_liep(title, addr, edu, yex, pay)
            print('开始存储job')
        #deferToThread(self._process_item, item, spider)



