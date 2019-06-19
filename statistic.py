# Модуль ведения статистики по удаленным файлам
"""
Последовательность выполнения задачи:
1. БД в которой будут храниться данные
    а) Разработать схему хранения данных
    б) Извлекать данные для выборки из БД
2. Данные статистики будут записываться в конце выполнения cleaner
3. Данные передаются в функцию, в которой они записываются в БД
4. Функция извлечения данных из файла за период времени(неделя, 2 недели календарный месяц)
5. Построение графика за период времени(неделя, 2 недели календарный месяц)
    а) График по объёму удаленных файлов
    б) График по объйму данных
    в) Итоговый размер удаленных файлов за период времени(неделя, 2 недели календарный месяц)
"""

from dbCleaner import AptDB
import pymysql

def passRead():
    fileName = '/etc/dpenkrat/cleaner/pass'
    passFile = open(fileName, mode='r', encoding='utf8')
    password = passFile.read()
    return password.strip()

def writeStat(*args):
    """Date, startTime, endTime, timeRun, totalDelFile, totalRemoveData, sendEmails"""
    dbwrite = AptDB('localhost','python', passworddb, 'server_stat')
    #Формирование SQL запроса для записи в БД
    sql = 'INSERT INTO Statistics(Date, StartTime, EndTime, TimeRun, TotalDelFile, TotalRemoveData, Emails) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, "%s") '%(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
    dbwrite.execDB(sql)

passworddb = passRead()
db1 = AptDB('localhost','python', passworddb,'server_stat')
#print(db1.execDB('SHOW TABLES'))
#db1.createTable()
#Date, startTime, endTime, timeRun, totalDelFile, totalRemoveData, sendEmails
writeStat(20190619, 145200, 145300, 60, 123000, 23141223, 'admin@gmail.com')

#print(db1.execDB('EXPLAIN Statistics'))


