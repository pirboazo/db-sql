#!/home/pboizot/src/DB-sql/bin/python

# lister les tables

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection au fichier DB sqlite
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")


# Ouvrir un curseur
ltable = DBCon.cursor()
liste = ltable.execute("select name from sqlite_master where name  NOT LIKE 'sqlite_%' and type= ?",['table']).fetchall()

ltable.close()

for table in liste:
    print(table[0])

DBCon.close()

exit()
