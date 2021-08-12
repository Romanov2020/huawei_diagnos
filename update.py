
import psycopg2
from psycopg2 import Error
from diagnos import faza1,faza2,faza3,fr,temp,pik,real,ef,last,lastd,pv1,pv2,pv3,pv4,pv5,pv6,pv7,pv8,pv1a,pv2a,pv3a,pv4a,pv5a,pv6a,pv7a,pv8a,fazA,fazB,fazC

b=34.3


try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="us0ak2021",
                                  # пароль, который указали при установке PostgreSQL
                                  password="us0ak_2021",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="huawei_loger")

    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO STATIKA_order (vfaza_a,vfaza_b,vfaza_c,afaza_a,afaza_b,afaza_c,work_ferq,temp_cab,power_pik,power_real,inv_eff,e_hour,e_day,e_month,e_total,pv1_v,pv2_v,pv3_v,pv4_v,pv5_v,pv6_v,pv7_v,pv8_v,pv1_a,pv2_a,pv3_a,pv4_a,pv5_a,pv6_a ,pv7_a ,pv8_a)
                                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
 
    record_to_insert = (faza1,faza2,faza3,fazA,fazB,fazC,fr,temp,pik,real,ef,last,lastd,600,1200,pv1,pv2,pv3,pv4,pv5,pv6,pv7,pv8,pv1a,pv2a,pv3a,pv4a,pv5a,pv6a,pv7a,pv8a)
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
