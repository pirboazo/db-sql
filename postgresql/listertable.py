#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import psycopg2

DBCon = None

# Etablissement de la connection
try:
    DBCon = psycopg2.connect(database="chinook", user="chinook", password="chinook", host="192.168.10.84", port="5432")
    print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
    ltable = DBCon.cursor()
    ltable.execute("select table_name from information_schema.tables where table_schema='public'")
    liste = ltable.fetchall()

    ltable.close()

    for table in liste:
        print(table[0])

    if DBCon is not None:
        DBCon.close()
        print('Database connection closed.')

except (Exception, psycopg2.DatabaseError) as error:
        print("error de connection")
        print(error)
exit()
