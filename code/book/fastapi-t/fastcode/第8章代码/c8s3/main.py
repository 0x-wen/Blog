import pymysql


# 获取链接对象
conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="12345",
    database="db",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# 获取游标
cursor = conn.cursor()

sql = "select * from users where id>=%(start)s and id<=%(end)s;"

cursor.execute(sql, {"start": 1, "end": 2})
print(cursor.fetchall())
