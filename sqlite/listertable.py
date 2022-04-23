#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
liste = ltable.execute("select name from sqlite_master where name  NOT LIKE 'sqlite_%' and type= ?",['table']).fetchall()

ltable.close()

for table in liste:
    print(table[0])

DBCon.close()

exit()
