import psycopg2
import datetime
now = datetime.datetime.now()

realdata= (now.strftime("%d-%m-%Y"))

m1=now.month

print(realdata)

print(now)

nm=(m1)

print(nm)

try:
        connection = psycopg2.connect(user="us0ak2021",
                                      password="us0ak_2021",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="huawei_loger")

        cursor = connection.cursor()
       
        print("Table Before updating record ")
        sql_select_query = """SELECT sum(work_power) FROM month WHERE work_day LIKE '%08%';"""
        
        cursor.execute(sql_select_query)
        recordm = cursor.fetchone()
        print(recordm)

except (Exception, psycopg2.Error) as error:
          print("Error in update operation", error)

finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
