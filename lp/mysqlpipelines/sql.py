import mysql.connector
from lp import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)



class Sql:
    @classmethod
    def insert_lp(cls, title, area, edu, exp, salary, stype, comname, welfarekey):
        sql = 'INSERT INTO lp(`title`, `area`, `edu`, `exp`, `salary`, `stype`, `comname`, `welfarekey`) VALUES (%(title)s, %(area)s, %(edu)s, %(exp)s, %(salary)s, %(stype)s, %(comname)s, %(welfarekey)s)'

        value = {
            'title': title,
            'area': area,
            'edu': edu,
            'exp': exp,
            'salary': salary,
            'stype': stype,
            'comname': comname,
            'welfarekey': welfarekey
        }
        cur.execute(sql, value)
        cnx.commit()
