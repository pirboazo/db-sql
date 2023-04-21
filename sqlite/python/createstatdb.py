#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBConnection = sqlite3.connect('chinook.db')

if DBConnection :
    print("Connection established ..........")

cur = DBConnection.cursor()
cur.execute('create table IF NOT EXISTS statdb (nomtable text not NULL unique, nbligne integer not null, nbattr integer )')
cur.close()

DBConnection.close()

exit()
