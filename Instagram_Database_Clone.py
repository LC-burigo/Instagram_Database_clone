import pymysql


class Instagram_Database_Clone:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(host='localhost', user='root', password='9479854532441919Lb', db='instagram_clone')
        self.Cursor = Connection.cursor()

    # Insert section
    def Insert_Into_users(self, name):
        insert = "INSERT INTO users(username) VALUES({});".format(name)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_photo(self, image, user_id):
        insert = "INSERT INTO photo(user_id, photo_id) VALUES({}, {});".format(image, user_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_likes(self, user_id, photo_id):
        insert = "INSERT INTO likes(user_id, photo_id) VALUES({}, {});".format(user_id, photo_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_comments(self, text, photo_id, user_id):
        insert = "INSERT INTO comments(comment_text, user_id, photo_id) VALUES({}, {});".format(text, user_id, photo_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_follows(self, follower_id, followee_id):
        insert = "INSERT INTO follows(follower_id, followee_id) VALUES({}, {});".format(follower_id, followee_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_tags(self, tags):
        insert = "INSERT INTO tags(tag_name) VALUES({});".format(tags)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_photo_tags(self, photo_id, tag_id):
        insert = "INSERT INTO photos_tags(photo_id, tag_id) VALUES({});".format(photo_id, tag_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    # Delete section
    def Delete_user(self, name):
        delete = "DELETE from users WHERE username = {};".format(name)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_photo(self, image):
        delete = "DELETE from photos WHERE image_url = {};".format(image)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_likes(self, what, id):
        delete = "DELETE from likes WHERE {} = {};".format(what, id)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_follows(self, what, follow_id):
        delete = "DELETE from follows WHERE {} = {};".format(what, follow_id)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_comments(self, what, id_or_text):
        delete = "DELETE from comments WHERE {} = {};".format(what, id_or_text)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_tags(self, tag):
        delete = "DELETE from tags WHERE {} = {};".format(what, id_or_text)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

first_insert = Instagram_Database_Clone()
first_insert.Delete_comments('photo_id', 1)


# def Connect_to_Database(a, b):
#     Connection = pymysql.connect(
#                                   host='localhost',
#                                   user='root',
#                                   password='9479854532441919Lb',
#                                   db='instagram_clone'
#                                 )
#
#     Cursor = Connection.cursor()
#     Insert = "INSERT INTO likes(user_id, photo_id) VALUES({},{});".format(a, b)
#     Cursor.execute(Insert)
#     Connection.commit()
#     print(Cursor.rowcount, "ok")
#
#
# Connect_to_Database(2, 20)

