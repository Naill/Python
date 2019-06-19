import pymysql
#В целом, как класс, наверное все таки лишнее. Можно было реализовать более интуитивно.
class AptDB():
    """Класс по работе с БД server_stat"""
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def createTable(self):
        """В целом, наверное все таки лишняя функция, т.к. таблица все равно создается только один раз
        и работает программа только локально на одном сервере, распространение не планируется"""
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            sql = 'CREATE TABLE Statistics(id integer not null AUTO_INCREMENT, Date date not null, StartTime time not null, ' \
                  'EndTime time not null, TimeRun integer not null, TotalDelFile integer not null, ' \
                  'TotalRemoveData int(50) not null, Emails varchar(255) not null, unique (ID))'
            with connection.cursor() as cursor:
                cursor.execute(sql)
            connection.commit()

        finally:
            connection.close()

#Функция выполения SQL команд
    def execDB(self, sql):
        """Выполнение переданной команды и возвращение её результата"""
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     db=self.db,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                exeCommand = cursor.fetchall()
            connection.commit()
        finally:
            connection.close()
        return exeCommand






