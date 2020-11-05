import pymysql

Connection = pymysql.connect(
                              host='localhost',
                              user='root',
                              password='9479854532441919Lb',
                              db='instagram_clone'
                            )

Cursor = Connection.cursor()
Insert = "INSERT INTO likes(user_id, photo_id) VALUES(2,6);"
Cursor.execute(Insert)
Connection.commit()
print(Cursor.rowcount, "ok")