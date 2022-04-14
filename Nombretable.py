#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
nbtable = ltable.execute("select count(*) from sqlite_master where type= ?",['table']).fetchone()
print(nbtable)

ltable.close()
DBCon.close()
exit()
