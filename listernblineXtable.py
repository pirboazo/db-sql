#!/home/oboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
liste = ltable.execute("select name from sqlite_master where type= ?",['table']).fetchall()

ltable.close()

# ouvrir un curseur pour compter

nblinCursor=DBCon.cursor()

for table in liste:
    # construire la chaine pour le select
    requet="select count(*) from " + table[0]
    nbline=nblinCursor.execute(requet).fetchone()
    print(table[0], nbline[0])

nblinCursor.close()

DBCon.close()

exit()
