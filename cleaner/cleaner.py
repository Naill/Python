#---------------------------------------
#           Program by Dmitriy Penkrat
#
#  Version      Date        Info
#   1.0         04.2019     learn python
#---------------------------------------

import os
import time
import clean_mail

DAYS = 1
DAYS_DB = 10
FOLDERS = ["/var/www/clients/client2/web22/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web20/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web42/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web55/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web63/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web60/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web14/web/DEBUG",
            "/var/www/clients/client2/web44/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web43/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web54/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web47/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web70/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web72/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web52/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web57/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web18/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web67/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web45/web/eshop_old/admin/DEBUG",
            "/var/www/clients/client2/web46/web/eshop/admin/DEBUG",
            "/var/www/clients/client2/web22/web/eshop/admin/FILES",
            "/var/www/clients/client2/web30/web/eshop/admin/FILES",
            "/var/www/clients/client2/web20/web/eshop/admin/FILES",
            "/var/www/clients/client2/web33/web/eshop/admin/FILES",
            "/var/www/clients/client2/web29/web/eshop_OLD/admin/FILES",
            "/var/www/clients/client2/web29/web/eshop/admin/FILES",
            "/var/www/clients/client2/web37/web/eshop/admin/FILES",
            "/var/www/clients/client2/web42/web/eshop/admin/FILES",
            "/var/www/clients/client2/web55/web/eshop/admin/FILES",
            "/var/www/clients/client2/web63/web/eshop/admin/FILES",
            "/var/www/clients/client2/web7/web/eshop/admin/FILES",
            "/var/www/clients/client2/web7/web/eshop.old/admin/FILES",
            "/var/www/clients/client2/web10/web/eshop/admin/FILES",
            "/var/www/clients/client2/web35/web/eshop/admin/FILES",
            "/var/www/clients/client2/web60/web/eshop/admin/FILES",
            "/var/www/clients/client2/web5/web/eshop/admin/FILES",
            "/var/www/clients/client2/web17/web/eshop/admin/FILES",
            "/var/www/clients/client2/web44/web/eshop/admin/FILES",
            "/var/www/clients/client2/web12/web/eshop/admin/FILES",
            "/var/www/clients/client2/web62/web/eshop/admin/FILES",
            "/var/www/clients/client2/web64/web/eshop/admin/FILES",
            "/var/www/clients/client2/web36/web/eshop/admin/FILES",
            "/var/www/clients/client2/web43/web/eshop/admin/FILES",
            "/var/www/clients/client2/web54/web/eshop/admin/FILES",
            "/var/www/clients/client2/web66/web/eshop/admin/FILES",
            "/var/www/clients/client2/web19/web/eshop/admin/FILES",
            "/var/www/clients/client2/web27/web/eshop/admin/FILES",
            "/var/www/clients/client2/web59/web/eshop/admin/FILES",
            "/var/www/clients/client2/web31/web/eshop/admin/FILES",
            "/var/www/clients/client2/web47/web/eshop/admin/FILES",
            "/var/www/clients/client2/web70/web/eshop/admin/FILES",
            "/var/www/clients/client2/web2/web/eshop/admin/FILES",
            "/var/www/clients/client2/web34/web/eshop/admin/FILES",
            "/var/www/clients/client2/web3/web/eshop/admin/FILES",
            "/var/www/clients/client2/web26/web/eshop/admin/FILES",
            "/var/www/clients/client2/web69/web/eshop/admin/FILES",
            "/var/www/clients/client2/web50/web/eshop/admin/FILES",
            "/var/www/clients/client2/web72/web/eshop/admin/FILES",
            "/var/www/clients/client2/web9/web/eshop/admin/FILES",
            "/var/www/clients/client2/web15/web/eshop/admin/FILES",
            "/var/www/clients/client2/web8/web/eshop/admin/FILES",
            "/var/www/clients/client2/web21/web/eshop/admin/FILES",
            "/var/www/clients/client2/web71/web/eshop/admin/FILES",
            "/var/www/clients/client2/web48/web/eshop/admin/FILES",
            "/var/www/clients/client2/web25/web/eshop/admin/FILES",
            "/var/www/clients/client2/web52/web/eshop/admin/FILES",
            "/var/www/clients/client2/web28/web/eshop/admin/FILES",
            "/var/www/clients/client2/web51/web/eshop/admin/FILES",
            "/var/www/clients/client2/web57/web/eshop/admin/FILES",
            "/var/www/clients/client2/web49/web/eshop/admin/FILES",
            "/var/www/clients/client2/web18/web/eshop/admin/FILES",
            "/var/www/clients/client2/web67/web/eshop/admin/FILES",
            "/var/www/clients/client2/web13/web/eshop/admin/FILES",
            "/var/www/clients/client2/web45/web/eshop/admin/FILES",
            "/var/www/clients/client2/web45/web/eshop_old/admin/FILES",
            "/var/www/clients/client2/web46/web/eshop/admin/FILES"
           ]
FOLDER_DB = '/var/sql/bd'
TOTAL_DELETED_FILE    = 0            #Общее количество удаленных файлов
TOTAL_DELETED_FOLDER  = 0            #Общее количество удаленных папок
TOTAL_DELETED_SIZE    = 0            #Размер удаленных файлов
TOTAL_DELETED_SIZE_DB = 0

#dirsFile = "dirs"                   #Файл с информацией о директориях для очистки мусора
nowTime = time.time()               #Получение текущего времени в секундах
ageTime = nowTime - 60*60*24*DAYS   #Лимит в секундах после которого
                                    #условие неверно будет и файлы будут удаляться
ageTimeDb = nowTime - 60*60*24*DAYS_DB

#С помощью os.walk реализовать модуль поиска директории и возврата списка директорий
def Delete_Files(folder):
    """Удаление файлов старше X DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    nameFile = 'removed.log'
    logFile = open(nameFile, mode='w', encoding='utf-8')
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file) # Получение полного пути к файлу с указанием имени файла
            fileDate = os.path.getmtime(fileName)
            if fileDate < ageTime:
                if file[0:3] == 'in_' and file[-4:] == '.txt' or file[0:4] == 'out_' and file[-4:] == '.txt' or file[0:7] == 'changes':
                    logFile.write(file + '\n')
                    sizeFile = os.path.getsize(fileName)
                    TOTAL_DELETED_SIZE += sizeFile # подсчитать размер удаленных файлов
                    TOTAL_DELETED_FILE += 1        # Подсчитать количество удаленных файлов
                    os.remove(fileName)
    logFile.close()

def Delete_DB(folder):
    """Удаление бэкапов БД старше X DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE_DB
    nameFile = 'removed.log'
    logFile = open(nameFile, mode='a', encoding='utf-8')
    for  path, dirs, files  in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)  # Получение полного пути к файлу с указанием имени файла
            fileDate = os.path.getmtime(fileName)
            if fileDate < ageTimeDb:
                logFile.write(file + '\n')
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE_DB += sizeFile  # подсчитать размер удаленных файлов
                TOTAL_DELETED_FILE += 1  # Подсчитать количество удаленных файлов
                os.remove(fileName)
    logFile.close()
#=================MAIN====================
startTime = time.asctime()

for line in FOLDERS:
    Delete_Files(line)   # Удаление старых файлов которые старше DAYS дней

Delete_DB(FOLDER_DB)

endTime = time.asctime()

TOTAL_DELETED_SIZE += TOTAL_DELETED_SIZE_DB

mailtext = "------------------------------------------------------------------------------------\n" \
    + "START TIME:                                   " + str(startTime) + '\n' \
    + "Количество удаленных файлов:                  " + str(TOTAL_DELETED_FILE) + " шт. \n" \
    + "Размер удаленных бэкапов БД                 : " +str(round(TOTAL_DELETED_SIZE_DB/1024/1024/1024,3)) + " Gb.\n" \
    + "Размер освобожденного дискового пространства: " +str(round(TOTAL_DELETED_SIZE/1024/1024/1024,3)) + " Gb.\n" \
    + "END TIME:                                     " + str(endTime) + '\n' \
    + "-----------------------------------------------------------------------------------\n"

clean_mail.CleanMail(mailtext)