import pymysql


class Instagram_Database_Clone:
    def __init__(self):
        self.Connection = Connection = pymysql.connect(host='localhost', user='root', password='9479854532441919Lb', db='instagram_clone')
        self.Cursor = Connection.cursor()

    # Insert section
    def Insert_Into_users(self, name):
        insert = "INSERT INTO users(username) VALUES('{}');".format(name)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_photo(self, image, user_id):
        insert = "INSERT INTO photos(image_url, user_id) VALUES('{}', {});".format(image, user_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_likes(self, user_id, photo_id):
        insert = "INSERT INTO likes(user_id, photo_id) VALUES({}, {});".format(user_id, photo_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_comments(self, text, photo_id, user_id):
        insert = "INSERT INTO comments(comment_text, photo_id, user_id) VALUES('{}', {}, {});".format(text, photo_id, user_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_follows(self, follower_id, followee_id):
        insert = "INSERT INTO follows(follower_id, followee_id) VALUES({}, {});".format(follower_id, followee_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Many_into_follows(self, content):
        insert = "INSERT INTO follows(follower_id, followee_id) VALUES(%S, %S);"
        datas = content
        self.Cursor.executemany(insert, datas)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_tags(self, tags):
        insert = "INSERT INTO tags(tag_name) VALUES('{}');".format(tags)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Insert_Into_photo_tags(self, photo_id, tag_id):
        insert = "INSERT INTO photos_tags(photo_id, tag_id) VALUES({}, {});".format(photo_id, tag_id)
        self.Cursor.execute(insert)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    # Delete section
    def Delete_user(self, name):
        delete = "DELETE from users WHERE username = '{}';".format(name)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_photo(self, image):
        delete = "DELETE from photos WHERE image_url = '{}';".format(image)
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
        delete = "DELETE from comments WHERE {} = '{}';".format(what, id_or_text)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_tags(self, tag):
        delete = "DELETE from tags WHERE tag_name = '{}';".format(tag)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    def Delete_photo_tags(self, what, id):
        delete = "DELETE from photo_tags WHERE {} = {};".format(what, id)
        self.Cursor.execute(delete)
        self.Connection.commit()
        print(self.Cursor.rowcount, "ok")

    # Some exercises
    def The_Five_Longest(self):
        get = "SELECT * FROM users ORDER BY created_at LIMIT 5;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def More_Registration_Day(self):
        get = "SELECT username, dayname(created_at) as day, COUNT(*) as registrations FROM users GROUP BY day ORDER BY registrations DESC LIMIT 1;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Inactive_Users(self):
        get = "SELECT username FROM users left join photos on users.id = photos.user_id WHERE photos.user_id is null ORDER BY username;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Photo_With_More_Likes(self):
        get = "SELECT image_url, photo_id, COUNT(*) as total_likes from photos JOIN likes ON photos.id = likes.photo_id GROUP BY photo_id ORDER BY total_likes DESC LIMIT 1;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Photo_Per_Users(self):
        get = "SELECT (SELECT COUNT(*) from photos) / (SELECT COUNT(*) from users);"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Most_Common_Tags(self):
        get = "SELECT tag_name, COUNT(*) as total FROM photo_tags left JOIN tags ON photo_tags.tag_id = tags.id GROUP BY tag_name ORDER BY total DESC limit 5;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Users_Most_Likers(self):
        get = "SELECT username, COUNT(*) as total_likes FROM users RIGHT JOIN likes ON users.id = likes.user_id GROUP BY username HAVING total_likes = 257;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)

    def Users_Most_Commenter(self):
        get = "select username, COUNT(*) as total from comments LEFT JOIN users ON comments.user_id = users.id GROUP BY username HAVING total = 258;"
        self.Cursor.execute(get)
        self.Connection.commit()
        for x in self.Cursor:
            print(x)



operations = Instagram_Database_Clone()
operations.Insert_Many_into_follows([(1, 2), (1, 3)])
