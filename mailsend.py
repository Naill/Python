# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def CleanMail(body):
    # Импортируем библиотеку по работе с SMTP
    # Добавляем необходимые подклассы - MIME-типы

    addr_from = "stat@apt.by"  # Адресат
    addr_to = "penkrat.dm@gmail.com"  # Получатель
    password = "nEP0lpwAXX"  # Пароль

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header('[APT.BY Очистка системы]', 'utf-8')
    msg['From'] = addr_from
    msg['To'] = addr_to

    server = smtplib.SMTP('smtp.apt.by', 587)  # Создаем объект SMTP
    #server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    server.starttls()  # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)  # Получаем доступ
    server.sendmail(msg['From'], msg['To'], msg.as_string())  # Отправляем сообщение
    server.quit()


def message_send(startTime, total_del_file, total_del_size, endTime):
    mailtext = "------------------------------------------------------------------------------------\n" \
               + "START TIME:                                   " + str(startTime) + '\n' \
               + "Количество удаленных файлов:                  " + str(total_del_file) + " шт. \n" \
               + "Размер освобожденного дискового пространства: " + str(
        round(total_del_size / 1024 / 1024 / 1024, 3)) + " Gb.\n" \
               + "END TIME:                                     " + str(endTime) + '\n' \
               + "-----------------------------------------------------------------------------------\n"
    CleanMail(mailtext)