import pymysql

class AptDB():
    """Класс по работе с БД server_stat"""
    def __init__(self, host, user, password, db, cursorclass):
        self.host = host
        self.user - user
        self.password - password
        self.db = db
        self.cursorclass = cursorclass

    def write(self):
        pass
    def read(self):
        pass
    def





connection = pymysql.connect(host='localhost',
                             user='python',
                             password='Python!33',
                             db='server_stat',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    db_stat = connection.cursor()
    #db_stat.execute("CREATE TABLE table2( h VARCHAR(10))")
    connection.commit()
    db_stat.execute("SHOW TABLES;")
    version = db_stat.fetchall()

    print (version)