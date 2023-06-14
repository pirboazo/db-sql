#!/home/pboizot/src/DB-sql/bin/python

# import du driver de connection sqlite3
import sqlite3

# Etablissement de la connection
DBConnection = sqlite3.connect('chinook.db')

if DBConnection :
    print("Connection established ..........")

# remarque le module sqlite3 créera une base sî il ne trouve pas le fichier # DEBUG:
# comment vérifier que nous avons ouvert le bon fichier

DBConnection.close()

exit()
