import pymysql
from Common.config import cfg

class DB:
    def __init__(self,host,port,user,password):
    # 连接数据库
        self.con = pymysql.connect(host= host,
                              port= port,
                              user= user,
                              password=password,
                              charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor
                                   )
        self.cur = self.con.cursor()

    def find_data(self,sql):
        """查询数据"""
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def updata_data(self,sql):
        """修改数据：增删改"""
        self.cur.execute(sql)
        self.con.commit()

db = DB(host=cfg.get("mysql","host"),
        port=cfg.getint("mysql","port"),
        user=cfg.get("mysql","user"),
        password=cfg.get("mysql","password")
        )
# 如果存在多个数据库的操作，可以实例化很多数据库对象（db2），然后取配置文件中不同的IP地址和账号密码进行使用

if __name__ == "__main__":
    db.find_data("select id,name,type from table_name limit 10;")
    db.updata_data("updata table_name set colum = 'value1' where id = 1233;")

