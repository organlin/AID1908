'''
注册：输入信息--->存储到数据库
user: id name passwd
name 不能重复
'''
import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="test", charset='utf8')
cur = db.cursor()
def register():
    pass



try:
    register()
except Exception as e:
    print(e)
