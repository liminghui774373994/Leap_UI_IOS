import pymysql
from monitor import readConfig


class dbconn():

    #连接数据库
    def open(self,content_sql_name):
        self.host, self.port, self.user, self.passwd, self.database = readConfig.sql_content(content_sql_name)
        self.db = pymysql.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd,database=self.database,charset='utf8')
        self.cursor = self.db.cursor()



    # 关闭数据库
    def close(self):
            self.cursor.close()
            self.db.close()

    #执行数据库
    def execute(self,sql,content_sql_name):
        try:
            self.open(content_sql_name)
            self.cursor.execute(sql)
            self.db.commit()
            a = self.cursor.fetchall()
            return a
            print("执行成功！")
        except Exception as e:
            self.db.rollback()
            print("执行失败",e)
        self.close()



if __name__ == "__main__":
    dbconn()
