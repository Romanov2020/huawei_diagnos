import datetime

import psycopg2
from psycopg2 import Error
from smday import record,select_day




now = datetime.datetime.now()

print (now.strftime("%d-%m-%Y"))

priv= (datetime.date.today()-datetime.timedelta(1))

pr= (priv.strftime("%d-%m-%Y"))

dr='21-07-2021'


try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="us0ak2021",
                                  # пароль, который указали при установке PostgreSQL
                                  password="us0ak_2021",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="huawei_loger")

    cursor = connection.cursor()



    postgres_insert_query = """ INSERT INTO month (work_day,work_power)
                                       VALUES (%s,%s)"""
    
 
    record_to_insert = (pr,record)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print (count, "Запись успешно добавлена ​​в таблицу mobile")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")











