#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
ltable.execute("select lastname, FirstName, BirthDate from employees")
employe = ltable.fetchone()

while employe != None:
    print(employe)
    employe = ltable.fetchone()
    
ltable.close()

DBCon.close()
exit()
