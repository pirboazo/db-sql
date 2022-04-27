#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection psycopg2
import psycopg2

# Etablissement de la connection
DBCon = psycopg2.connect(database="chinook", user="chinook", password="chinook", host="192.168.10.131", port="5432")

print("Connection established ..........")

# lister les tables

# Ouvrir un curseur
verif = DBCon.cursor()
verif.execute("select version()")
version = verif.fetchone()
print(version)

DBCon.close()
