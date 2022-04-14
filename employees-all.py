#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBCon = sqlite3.connect('chinook.db')

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
ltable = DBCon.cursor()
liste = ltable.execute("select lastname, FirstName, BirthDate from employees").fetchall()

ltable.close()

print(" sans formatage")
print(liste)

print("Ligne par ligne") #ligne à ligne
for employe in liste:
    print(employe)

DBCon.close()
