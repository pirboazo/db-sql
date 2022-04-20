import sqlite3 as sql
import os
import csv
from sqlite3 import Error

try:

  # Connect to database
  conn=sql.connect('chinook.db')


  ltable = conn.cursor()
  liste = ltable.execute("select name,sql from sqlite_master where type= ?",['table']).fetchall()

  ltable.close()
  cursor = conn.cursor()

  sqlfile = open("createtable.sql", 'w')

  # Export data into CSV file
  for table in liste:
      print ("Exporting data into CSV............")
      sqlfile.write(table[1])
      sqlfile.write("\n;\n")
      requete= "select * from "+ table[0]
      cursor.execute(requete)
      with open("csv/"+table[0]+"_data.csv", "w", newline='') as csv_file:
          csv_writer = csv.writer(csv_file,delimiter=",", quotechar='"')
          csv_writer.writerow([i[0] for i in cursor.description])
          csv_writer.writerows(cursor)
          dirpath = os.getcwd() + "csv/"+table[0]+"_data.csv"
          print ("Data exported Successfully into {}".format(dirpath))

  sqlfile.close()

except Error as e:
  print(e)

# Close database connection
finally:
  conn.close()
