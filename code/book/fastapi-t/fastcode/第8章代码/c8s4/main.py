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



# sql = "insert into users(name, password) values('liuxu5', '123456');"
#
# cursor.execute(sql)
# # conn.commit()           # 需要手动确认，否则不会保存到数据库


sql = "insert into users(name, password) values(%s, %s);"

item_list = [("lx1", "12345"), ("lx2", "12345567")]

cursor.executemany(sql, args=item_list)

