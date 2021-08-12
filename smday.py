import psycopg2

import datetime


def select_day():
    now = datetime.datetime.now()

#print (now.strftime("%Y-%m-%d"))

priv= (datetime.date.today()-datetime.timedelta(1))

pr= (priv.strftime("%Y-%m-%d"))
pt='2021-07-23'
print (pt)

#print(pr)

try:
        connection = psycopg2.connect(user="us0ak2021",
                                      password="us0ak_2021",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="huawei_loger")

        cursor = connection.cursor()
        print (pt)
        print("Table Before updating record ")
        sql_select_query = """select e_day from statika_order where to_char(datetime, 'YYYY-MM-DD')= to_char( now()-INTERVAL '1 day', 'YYYY-MM-DD' )  AND e_day>0 ORDER BY id DESC LIMIT 1;"""
        
        cursor.execute(sql_select_query)
        record = cursor.fetchone()
        print(record)

except (Exception, psycopg2.Error) as error:
          print("Error in update operation", error)

finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")