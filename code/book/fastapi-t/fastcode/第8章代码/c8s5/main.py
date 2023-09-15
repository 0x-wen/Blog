import pymysql


# 获取链接对象
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="12345",
    database="db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

# 获取游标
cursor = conn.cursor()



# sql = "update users set password='11111' where id=7;"
# cursor.execute(sql)



sql = "delete from users where id>=6;"
print(cursor.execute(sql))

