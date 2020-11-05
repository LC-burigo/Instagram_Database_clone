import pymysql


class Instagram_Database_Clone:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(
                                  host='localhost',
                                  user='root',
                                  password='9479854532441919Lb',
                                  db='instagram_clone'
                                )
        self.Cursor = Connection.cursor()

    def Insert_into_Likes(self, a, b):
        insert = "INSERT INTO likes(user_id, photo_id) VALUES({}, {});".format(a, b)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")


first_insert = Instagram_Database_Clone
first_insert.Insert_into_Likes('2', '20')


# def Connect_to_Database():
#
#
#     Connection = pymysql.connect(
#                                   host='localhost',
#                                   user='root',
#                                   password='9479854532441919Lb',
#                                   db='instagram_clone'
#                                 )
#
#     Cursor = Connection.cursor()
#     Insert = "INSERT INTO likes(user_id, photo_id) VALUES(2,7);"
#     Cursor.execute(Insert)
#     Connection.commit()
#     print(Cursor.rowcount, "ok")

