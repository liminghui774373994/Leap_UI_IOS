import os
import configparser

#读取配置文件的绝对路径
cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path,"config.ini")
print(configPath)

#实例化并读取配置文件
conf = configparser.ConfigParser()
conf.read(configPath)

#遍历配置文件中的参数
def sql_content(content_sql_name):
    host_ = conf.get(content_sql_name, "host"),
    port_ = conf.get(content_sql_name, "port"),
    user_ = conf.get(content_sql_name, "user"),
    passwd_ = conf.get(content_sql_name, "passwd"),
    database_ = conf.get(content_sql_name, "database"),
    # charset = conf.get("mysql_activity", "charset"),,charset
    host = host_[0]
    port = port_[0]
    user = user_[0]
    passwd = passwd_[0]
    database = database_[0]

    return host, port, user, passwd, database
