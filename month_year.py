import datetime
import calendar
import psycopg2
from psycopg2 import Error

def select_day2():
    now = datetime.datetime.now()

tud=datetime.date.today()

pr= (datetime.date.today()-datetime.timedelta(1))






date=datetime.datetime.now()
month_end_date=datetime.datetime(date.year,date.month,1) + datetime.timedelta(days=calendar.monthrange(date.year,date.month)[1] - 1)
name_mon = (datetime.date.today().strftime('%B'))

print('сегодня',tud)
print('последний день месяца',month_end_date)
print(name_mon)


try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="us0ak2021",
                                  # пароль, который указали при установке PostgreSQL
                                  password="us0ak_2021",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="huawei_loger")

    cursor = connection.cursor()



    postgres_insert_query = """ INSERT INTO mon_years (work_month,work_power)
                                       VALUES (%s,%s)"""
    
 
    record_to_insert = ('июль',3282.42)
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



