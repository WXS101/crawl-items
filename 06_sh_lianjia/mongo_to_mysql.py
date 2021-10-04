import pymongo
import pymysql

mongo_py = pymongo.MongoClient()

collection = mongo_py['lianjia_sh']['data']

try:
    # 1,链接 数据库 链接对象 connection()
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           db="lianjia_sh",
                           user="root",
                           passwd="root",
                           charset="utf8")
    # 2,建库 建表, 插入数据
    cur = conn.cursor()

    # 建库
    create_dbs = "CREATE DATABASE lianjia_sh"

    # 建表
    create_table = '''CREATE TABLE data (
      title VARCHAR (128) NOT NULL,
      price VARCHAR (20) NOT NULL,
      area VARCHAR (20) NOT NULL,
      house VARCHAR (20) NOT NULL,
      img_url VARCHAR (200) NOT NULL
    )'''

    data_lianjia = []
    for item in collection.find():
        data_lianjia.append([item['简介'], item['房租'], item['面积'], item['户型'], item['img_url']])

    for i in range(10200):
        print(i)
        insert_sub = f'insert into data values ("{data_lianjia[i][0]}","{data_lianjia[i][1]}","{data_lianjia[i][2]}","{data_lianjia[i][3]}","{data_lianjia[i][4]}")'
        cur.execute(insert_sub)

        # 提交事务
        conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()
except Exception as e:
    print(e)
