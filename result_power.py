import math
import psycopg2
from alg import *


try:
                                     connection = psycopg2.connect(user="us0ak2021",
                                     password="us0ak_2021",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="huawei_loger")

                                     cursor = connection.cursor()

                                     print("Table Before updating record ")
                                     sql_select_query = """select sum(work_power) from month"""
                                     cursor.execute(sql_select_query)
                                     record = cursor.fetchone()
                                     print(record)

                                     rt=recordm[0] 
                                     print(12,rt)   
                                     ost=7278.61


                                     all_month=56 
                                     all_year=rt+ost
                                     all_period=all_year  
        # Update single record now

                                     print(all_year)   

                                     sql_update_query = """Update result_power set all_month =%s, all_year =%s, all_period =%s"""
                                 
                                     cursor.execute(sql_update_query,(recordm,all_year,all_period))
                                     connection.commit()
                                     count = cursor.rowcount
                                     print(count, "Record Updated successfully ")
     
except (Exception, psycopg2.Error) as error:
                                    print("Error in update operation", error)

finally:
        # closing database connection.
                                 if connection:
                                  cursor.close()
                                  connection.close()
                                  print("PostgreSQL connection is closed")
                        
