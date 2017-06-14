import mysql.connector
from liep import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert_liep(cls, title, addr, edu, yex, pay):
        sql = 'INSERT INTO liep(`title`, `addr`, `edu`, `yex`, `pay`) VALUES (%(title)s, %(addr)s, %(edu)s, %(yex)s, %(pay)s)'

        value = {
            'title': title,
            'addr': addr,
            'edu': edu,
            'yex': yex,
            'pay': pay
        }
        cur.execute(sql, value)
        cnx.commit()

    # @classmethod
    # def select_name(cls, name_id):
    #     sql = 'SELECT EXISTS(SELECT 1 FROM liep WHERE name_id=%(name_id)s)'
    #     value = {
    #         'name_id': name_id
    #     }
    #     cur.execute(sql, value)
    #     return cur.fetchall()[0]
